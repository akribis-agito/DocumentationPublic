"""Parse KeywordsTableArray entries from a Params.c into per-product maps."""

from __future__ import annotations

import re
from pathlib import Path

from .defines import DefineTable
from .model import infer_data_type

# Maps the #if guard product macro to our product name.
_PRODUCT_GUARDS = {
    "CONTROLLER": "standalone",
    "CI_MASTER": "central-i",
}

_TABLE_OPEN = re.compile(
    r"#if\s*\(PRODUCT_TYPE\s*==\s*(\w+)\)\s*&&\s*\(IS_BOOT_IMAGE\s*==\s*0\)"
)
# One table entry: a brace group on a single logical line.
_ENTRY = re.compile(r"\{(.*?)\}", re.DOTALL)

# Token -> value maps for the attribute columns.
_ACCESS = {"RW": "rw", "RO": "ro"}
_TYPE = {"ISARRAY": "array", "NOARRAY": "scalar"}
_FLASH = {"FLASH": True, "NOFLASH": False}
_SCOPE = {"AXIS": "axis", "NON_AXIS": "non-axis"}
_IMPL = {"FINAL": "final", "PARTIAL": "partial"}
_UNITS = {"USER_UNITS": "user", "NO_USER_UNITS": "none", "FUNC_UNITS": "func"}


def _split_fields(body: str) -> list[str]:
    """Split a brace-body into top-level comma fields, respecting quotes."""
    fields, depth, buf, in_str = [], 0, [], False
    for ch in body:
        if ch == '"':
            in_str = not in_str
        if in_str:
            buf.append(ch)
            continue
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            fields.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        fields.append("".join(buf).strip())
    return fields


def _bool_motion(token: str) -> bool:
    return token == "OKINMOTN"


def _bool_motoron(token: str) -> bool:
    return token == "OKMTRON"


def _entry_to_record(fields: list[str], defines: DefineTable) -> dict | None:
    mnemonic = fields[1].strip().strip('"')
    if not mnemonic or mnemonic.startswith("ZZ"):
        return None
    max_index = defines.resolve(fields[13])
    array_size = (max_index + 1) if max_index is not None else 1
    is_array = _TYPE.get(fields[8], "scalar") == "array"
    lo = defines.resolve(fields[14])
    hi = defines.resolve(fields[15])
    attributes = {
        "access": _ACCESS.get(fields[5], fields[5].lower()),
        "scope": _SCOPE.get(fields[10], fields[10].lower()),
        "flash": _FLASH.get(fields[9], False),
        "type": "array" if is_array else "scalar",
        "array_size": array_size if is_array else 1,
        "data_type": infer_data_type({}),
        "ok_in_motion": _bool_motion(fields[6]),
        "ok_motor_on": _bool_motoron(fields[7]),
        "units": _UNITS.get(fields[4], fields[4].lower()),
        "range": [lo, hi] if lo is not None and hi is not None else None,
        "default": defines.resolve(fields[16]),
        "scaling": float(defines.resolve(fields[17]) or 1),
        "implemented": _IMPL.get(fields[11], fields[11].lower()),
    }
    return {"can_code": int(fields[0]), "attributes": attributes}


def _parse_one_table(block: str, defines: DefineTable) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for m in _ENTRY.finditer(block):
        fields = _split_fields(m.group(1))
        if len(fields) < 18:
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
        open_brace = text.index("{ \\", guard.end())
        end = text.index("};", open_brace)
        # Skip the table's own opening brace so the per-entry regex only sees
        # the individual {..} entries (which contain no nested braces).
        tables[product] = _parse_one_table(text[open_brace + 1 : end], defines)
    return tables
