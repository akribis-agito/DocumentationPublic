"""Parse KeywordsTableArray entries from a Params.c into per-product maps.

Handles two source formats:
  * LTS branch: backslash line-continuations, 11 inline attribute tokens, no
    data-type field (treated as int32).
  * develop branch: no continuations, attributes wrapped in a nested {...}
    brace with 12 fields including a data-type field (bParamType), and the
    pointer wrapped in {...}.
"""

from __future__ import annotations

import re
from pathlib import Path

from .defines import DefineTable

_PRODUCT_GUARDS = {
    "CONTROLLER": "standalone",
    "CI_MASTER": "central-i",
}

_TABLE_OPEN = re.compile(
    r"#if\s*\(PRODUCT_TYPE\s*==\s*(\w+)\)\s*&&\s*\(IS_BOOT_IMAGE\s*==\s*0\)"
)

# Attribute-token maps (shared by both formats).
_ACCESS = {"RW": "rw", "RO": "ro"}
_TYPE = {"ISARRAY": "array", "NOARRAY": "scalar"}
_FLASH = {"FLASH": True, "NOFLASH": False}
_SCOPE = {"AXIS": "axis", "NON_AXIS": "non-axis"}
_IMPL = {"FINAL": "final", "PARTIAL": "partial"}
_UNITS = {"USER_UNITS": "user", "NO_USER_UNITS": "none", "FUNC_UNITS": "func"}
# The float-type limit (+/-3.4e38, FLOAT_MIN/FLOAT_MAX and aliases like VQ_MIN/VQ_MAX)
# is not a real bound; a keyword whose min/max resolves to it accepts any float, so
# its range is reported as null (unbounded). Detected by value so aliases are caught.
_FLOAT_TYPE_LIMIT = 3.0e38


# develop bParamType tokens
_DATA_TYPE = {
    "0": "int32", "LONG32": "int32",
    "1": "float32", "FLOAT": "float32",
    "2": "float64", "DOUBLE": "float64",
    "3": "int64", "LONG64": "int64",
}


def _split_fields(body: str) -> list[str]:
    """Split a comma-separated list into top-level fields, respecting quotes
    and (), [], {} nesting."""
    fields, depth, buf, in_str = [], 0, [], False
    for ch in body:
        if ch == '"':
            in_str = not in_str
        if in_str:
            buf.append(ch)
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            fields.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        fields.append("".join(buf).strip())
    return fields


def _extract_balanced(text: str, open_idx: int) -> str:
    """Return the substring of a balanced {...} group starting at open_idx
    (which must be a '{'), inclusive of both braces. Respects strings."""
    depth = 0
    in_str = False
    esc = False
    for i in range(open_idx, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[open_idx : i + 1]
    return text[open_idx:]


def _iter_entries(table_block: str):
    """Yield the inner text of each top-level entry {...} inside a table block.

    `table_block` includes the table's outer braces; entries are the next
    nesting level. Nested braces inside an entry (attribute/pointer groups)
    are preserved in the yielded text."""
    depth = 0
    buf: list[str] = []
    collecting = False
    in_str = False
    esc = False
    for ch in table_block:
        if in_str:
            if collecting:
                buf.append(ch)
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
            if collecting:
                buf.append(ch)
            continue
        if ch == "{":
            depth += 1
            if depth == 2:
                collecting = True
                buf = []
            elif depth > 2:
                buf.append(ch)
            continue
        if ch == "}":
            if depth == 2 and collecting:
                yield "".join(buf)
                collecting = False
            elif depth > 2:
                buf.append(ch)
            depth -= 1
            continue
        if collecting and depth >= 2:
            buf.append(ch)


def _range(lo, hi):
    """Build a [lo, hi] range, or None when unresolved or at the float-type limit."""
    if lo is None or hi is None:
        return None
    if abs(lo) >= _FLOAT_TYPE_LIMIT or abs(hi) >= _FLOAT_TYPE_LIMIT:
        return None
    return [lo, hi]


def _attrs_from_tokens(
    units_tok, access_tok, motion_tok, motoron_tok, array_tok, flash_tok,
    axis_tok, impl_tok, maxidx, lo, hi, dflt, scaling, data_type,
) -> dict:
    is_array = _TYPE.get(array_tok, "scalar") == "array"
    array_size = (maxidx + 1) if (is_array and maxidx is not None) else 1
    return {
        "access": _ACCESS.get(access_tok, access_tok.lower()),
        "scope": _SCOPE.get(axis_tok, axis_tok.lower()),
        "flash": _FLASH.get(flash_tok, False),
        "type": "array" if is_array else "scalar",
        "array_size": array_size,
        "data_type": data_type,
        "ok_in_motion": motion_tok == "OKINMOTN",
        "ok_motor_on": motoron_tok == "OKMTRON",
        "units": _UNITS.get(units_tok, units_tok.lower()),
        "range": _range(lo, hi),
        "default": dflt,
        "scaling": float(scaling) if scaling is not None else 1.0,
        "implemented": _IMPL.get(impl_tok, impl_tok.lower()),
    }


def _entry_to_record(fields: list[str], defines: DefineTable) -> dict | None:
    mnemonic = fields[1].strip().strip('"')
    if not mnemonic or mnemonic.startswith("ZZ"):
        return None

    if fields[2].startswith("{"):
        # develop format: attributes nested brace + data-type field
        attr = _split_fields(fields[2].strip("{} "))
        if len(attr) < 12:
            return None
        maxidx = defines.resolve(fields[3])
        attributes = _attrs_from_tokens(
            units_tok=attr[2], access_tok=attr[3], motion_tok=attr[4],
            motoron_tok=attr[5], array_tok=attr[6], flash_tok=attr[7],
            axis_tok=attr[8], impl_tok=attr[9], maxidx=maxidx,
            lo=defines.resolve(fields[4]), hi=defines.resolve(fields[5]),
            dflt=defines.resolve(fields[6]), scaling=defines.resolve(fields[7]),
            data_type=_DATA_TYPE.get(attr[11], "int32"),
        )
    else:
        # LTS format: 11 inline attribute tokens, no data-type field
        if len(fields) < 18:
            return None
        maxidx = defines.resolve(fields[13])
        attributes = _attrs_from_tokens(
            units_tok=fields[4], access_tok=fields[5], motion_tok=fields[6],
            motoron_tok=fields[7], array_tok=fields[8], flash_tok=fields[9],
            axis_tok=fields[10], impl_tok=fields[11], maxidx=maxidx,
            lo=defines.resolve(fields[14]), hi=defines.resolve(fields[15]),
            dflt=defines.resolve(fields[16]), scaling=defines.resolve(fields[17]),
            data_type="int32",
        )
    return {"can_code": int(fields[0]), "attributes": attributes}


def _parse_one_table(table_block: str, defines: DefineTable) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for entry in _iter_entries(table_block):
        fields = _split_fields(entry)
        if len(fields) < 8:
            continue
        record = _entry_to_record(fields, defines)
        if record:
            result[fields[1].strip().strip('"')] = record
    return result


def parse_params(path: Path, defines: DefineTable) -> dict[str, dict[str, dict]]:
    """Return {product: {mnemonic: {can_code, attributes}}}."""
    text = Path(path).read_text(errors="replace")
    tables: dict[str, dict[str, dict]] = {}
    for guard in _TABLE_OPEN.finditer(text):
        product = _PRODUCT_GUARDS.get(guard.group(1))
        if product is None:
            continue
        def_idx = text.index("KeywordsTableArray[NUM_OF_CAN_CODES]", guard.end())
        eq_idx = text.index("=", def_idx)
        brace_idx = text.index("{", eq_idx)
        table_block = _extract_balanced(text, brace_idx)
        tables[product] = _parse_one_table(table_block, defines)
    return tables
