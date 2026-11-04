"""Parse KeywordsTableArray entries from a Params.c into per-product maps.

Handles three source formats:
  * LTS branch: backslash line-continuations, 11 inline attribute tokens, no
    data-type field (treated as int32).
  * pre-KW_ROW develop: one table per PRODUCT_TYPE, attributes wrapped in a
    nested {...} brace with 12 fields including a data-type field (bParamType),
    and the pointer wrapped in {...}.
  * v5 (`parse_kw_row_table`): one positional KW_ROW table for every product,
    read per product through a real C preprocessor.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from .defines import DefineTable


class TableError(RuntimeError):
    """The firmware keyword table could not be found, expanded or read."""


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
    text = Path(path).read_text(encoding="utf-8", errors="replace")
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
    if not tables:
        raise TableError(f"{path}: no per-product KeywordsTableArray; a v5 KW_ROW "
                         "table is read with --firmware-root")
    return tables


# ---------------------------------------------------------------------------
# v5: one KW_ROW table, expanded per product by a real C preprocessor.
#
# Which rows a build gets, and with which widths and scopes, is decided by the
# row wrappers (KW_ROW_CIM_ONLY, KW_ROW_EC, ...) and by macros such as AXIS_CIM
# and CW_TYPETAG_POS under the product's configuration. Following those by regex
# would drift, so the file is expanded once per product the way the
# PC-simulation build configures it (Platform/PC/CMakeLists.txt: PROCESSOR=4,
# -DPRODUCT=PRODUCT_...), and the expanded rows are read. A row's min/max/
# default/scaling cells are indexes into the value pools (CommonIncludes/
# KeywordPool.h); they resolve through the pool arrays of the same expansion,
# which hold what the controller serves.
# ---------------------------------------------------------------------------

V5_PARAMS_C = Path("CommonC") / "AG300_CTL01Params.c"
V5_PRODUCT_CONFIG_H = Path("CommonIncludes") / "ProductConfig.h"
# The PC-simulation include path, as Tools/Cyclops/kwpool_check.py's PC arm.
_PC_SIM_INCLUDES = (
    "Platform/PC", "Platform/PC/stubs", "CommonIncludes", "CommonC", "Platform/Common/uip", ".",
    "Platform/PC/lwip",
    "Platform/Zynq/MAS02bsp/ps7_cortexa9_0/libsrc/lwip211_v1_0/src/lwip-2.1.1/src/include",
)
_PC_SIM_DEFINES = ("-DPROCESSOR=4",)
PREPROCESSOR_ENV = "KEYWORD_DOCGEN_CC"
_PREPROCESSOR_CANDIDATES = ("clang", "gcc")

# Firmware PRODUCT_TYPE values (CONTROLLER = 1, CI_MASTER = 2) -> product type.
V5_PRODUCT_TYPES = {1: "controller", 2: "ci-master"}

_V5_PRODUCT_RE = re.compile(r"^\s*#\s*(?:el)?if\s+PRODUCT\s*==\s*(PRODUCT_\w+)", re.M)
_V5_TABLE_RE = re.compile(r"KeywordsTableArray\s*\[\s*\d+\s*\]\s*=\s*\{")
_V5_TYPE_PROBE = "__DOCGEN_PRODUCT_TYPE__"
_V5_POOLS = (("KW_VALUE_INDEX", "gldKwValues"), ("KW_SCALE_INDEX", "gfKwScalings"))
# FUNC_UNITS and NO_USER_UNITS both expand to 0, so "func" is read from the raw row.
_V5_FUNC_UNITS_ROW = re.compile(
    r'^\s*KW_ROW\w*\s*\(\s*(\d+)\s*,\s*"(\w+)"\s*,\s*\{\s*\w+\s*,\s*\w+\s*,\s*FUNC_UNITS\b', re.M)

# Expanded attribute values (CommonIncludes/AG300_CTL01Interpreter.h).
_V5_ACCESS = {0: "rw", 1: "ro"}
_V5_SCOPE = {0: "non-axis", 1: "axis"}
_V5_UNITS = {0: "none", 1: "user", 2: "aux_user_units", 3: "pd_user_units", 4: "scaling"}
_V5_IMPL = {0: "not_implemented", 1: "partial", 2: "final", 3: "future"}
_V5_DATA_TYPE = {0: "int32", 1: "float32", 2: "float64", 3: "int64"}


def catalog_id(product: str) -> str:
    """`PRODUCT_AGD155_EC` -> `agd155-ec`, the catalog-ID form of the #18 ruling."""
    return product[len("PRODUCT_"):].lower().replace("_", "-")


def find_preprocessor() -> str:
    cc = os.environ.get(PREPROCESSOR_ENV)
    if cc:
        return cc
    for cand in _PREPROCESSOR_CANDIDATES:
        path = shutil.which(cand)
        if path:
            return path
    raise TableError(f"no C preprocessor found: install clang or gcc, or set {PREPROCESSOR_ENV}")


def list_v5_products(firmware_root: Path) -> list[str]:
    """Every `PRODUCT_*` that `CommonIncludes/ProductConfig.h` configures."""
    text = (Path(firmware_root) / V5_PRODUCT_CONFIG_H).read_text(encoding="utf-8", errors="replace")
    return _V5_PRODUCT_RE.findall(text)


def _preprocess_v5(root: Path, product: str, cc: str) -> str:
    fd, tu = tempfile.mkstemp(suffix=".c")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(f'#include "{(root / V5_PARAMS_C).as_posix()}"\n{_V5_TYPE_PROBE} PRODUCT_TYPE\n')
    try:
        cmd = [cc, "-E", "-P", "-x", "c", "-std=gnu11", "-w", "-funsigned-char",
               *_PC_SIM_DEFINES, f"-DPRODUCT={product}",
               *[f"-I{(root / inc).as_posix()}" for inc in _PC_SIM_INCLUDES], tu]
        res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    finally:
        os.unlink(tu)
    if res.returncode != 0 or not res.stdout:
        raise TableError(f"{product}: {cc} -E failed:\n{res.stderr[-2000:]}")
    return res.stdout


def _v5_value(cell: str, numbers: DefineTable):
    return numbers.resolve(cell)


def _v5_pool_table(pp: str) -> DefineTable:
    """Pool entry name -> its value expression, from the expansion's index enums and pool arrays."""
    raw: dict[str, str] = {}
    for enum, array in _V5_POOLS:
        e = re.search(r"enum\s+%s\s*\{" % enum, pp)
        a = re.search(r"\b%s\s*\[\s*\w+\s*\]\s*=\s*\{" % array, pp)
        if not e or not a:
            raise TableError(f"value pool {enum}/{array} not found in the expansion")
        names = [n for n in _split_fields(_extract_balanced(pp, e.end() - 1)[1:-1]) if n]
        exprs = [x for x in _split_fields(_extract_balanced(pp, a.end() - 1)[1:-1]) if x]
        if names[-1].endswith("_COUNT"):
            names.pop()
        if len(names) != len(exprs):
            raise TableError(f"{enum} has {len(names)} entries but {array} has {len(exprs)}")
        raw.update(zip(names, exprs))
    return DefineTable(raw)


def _v5_record(code: int, entry: str, numbers: DefineTable, func_units) -> tuple[str, dict] | None:
    cols = _split_fields(entry)
    mnemonic = cols[0].strip('"')
    if set(mnemonic) == {"Z"}:
        return None  # the ZZZ placeholder: this build does not implement this code
    attr = [numbers.resolve(a) for a in _split_fields(cols[1].strip("{} "))]
    if len(cols) < 9 or len(attr) != 12 or None in attr:
        raise TableError(f"CAN {code} {mnemonic}: unreadable expanded row {entry[:200]}")
    is_array = attr[6] == 1
    maxidx = numbers.resolve(cols[2])
    units = "func" if attr[2] == 0 and (code, mnemonic) in func_units else _V5_UNITS.get(attr[2], str(attr[2]))
    scaling = _v5_value(cols[6], numbers)
    return mnemonic, {
        "can_code": code,
        "attributes": {
            "access": _V5_ACCESS.get(attr[3], str(attr[3])),
            "scope": _V5_SCOPE.get(attr[8], str(attr[8])),
            "flash": attr[7] == 1,
            "type": "array" if is_array else "scalar",
            "array_size": (maxidx + 1) if (is_array and maxidx is not None) else 1,
            "data_type": _V5_DATA_TYPE.get(attr[11], "int32"),
            "ok_in_motion": attr[4] == 1,
            "ok_motor_on": attr[5] == 0,  # OKMTRON = 0, NOMTRON = 1
            "units": units,
            "range": _range(_v5_value(cols[3], numbers), _v5_value(cols[4], numbers)),
            "default": _v5_value(cols[5], numbers),
            "scaling": float(scaling) if scaling is not None else 1.0,
            "implemented": _V5_IMPL.get(attr[9], str(attr[9])),
        },
    }


def parse_v5_expansion(pp: str, func_units=frozenset()) -> tuple[str, dict[str, dict]]:
    """-> (product type, {mnemonic: {can_code, attributes}}) from one product's expansion.
    The CAN code is the row's position: the table is positional."""
    m = re.search(_V5_TYPE_PROBE + r"\s+(\d+)", pp)
    if not m or int(m.group(1)) not in V5_PRODUCT_TYPES:
        raise TableError("PRODUCT_TYPE did not expand to CONTROLLER or CI_MASTER")
    table = _V5_TABLE_RE.search(pp)
    if not table:
        raise TableError("KeywordsTableArray initializer not found in the expansion")
    numbers = _v5_pool_table(pp)
    keywords: dict[str, dict] = {}
    entries = _iter_entries(_extract_balanced(pp, table.end() - 1))
    for code, entry in enumerate(entries):
        rec = _v5_record(code, entry, numbers, func_units)
        if rec:
            keywords[rec[0]] = rec[1]
    if not keywords:
        raise TableError("the expanded KeywordsTableArray has no keyword rows")
    return V5_PRODUCT_TYPES[int(m.group(1))], keywords


def parse_kw_row_table(firmware_root: Path, products: list[str] | None = None,
                       cc: str | None = None) -> dict[str, dict]:
    """Return {catalog id: {"product_type", "keywords": {mnemonic: {can_code, attributes}}}}
    for every product ProductConfig.h configures (or the given `PRODUCT_*` keys)."""
    root = Path(firmware_root).resolve()
    cc = cc or find_preprocessor()
    source = (root / V5_PARAMS_C).read_text(encoding="utf-8", errors="replace")
    func_units = {(int(i), n) for i, n in _V5_FUNC_UNITS_ROW.findall(source)}
    products = products or list_v5_products(root)
    if not products:
        raise TableError(f"no PRODUCT_* blocks in {root / V5_PRODUCT_CONFIG_H}")
    out: dict[str, dict] = {}
    for product in products:
        ptype, keywords = parse_v5_expansion(_preprocess_v5(root, product, cc), func_units)
        out[catalog_id(product)] = {"product_type": ptype, "keywords": keywords}
    return out


# The product whose facts a product-type cell carries: the PC-simulation build's
# default product (Platform/PC/CMakeLists.txt) for controller, the AGM800 for ci-master.
V5_REFERENCE_PRODUCTS = {"controller": "agd301-et-2d05", "ci-master": "agm800"}


def collapse_by_product_type(per_product: dict[str, dict]) -> dict[str, dict[str, dict]]:
    """Fold `parse_kw_row_table` output into {product type: {mnemonic: cell}}.

    A cell is {can_code, attributes, products}. Its facts come from the type's
    reference product, or from the first product of the type that has the
    keyword when the reference does not. `products` lists the catalog IDs of
    the type's products that have the keyword, or is empty when all of them do.
    """
    out: dict[str, dict[str, dict]] = {}
    for ptype in V5_PRODUCT_TYPES.values():
        ids = [pid for pid, p in per_product.items() if p["product_type"] == ptype]
        if not ids:
            continue
        ref = V5_REFERENCE_PRODUCTS[ptype]
        order = ([ref] if ref in ids else []) + [pid for pid in ids if pid != ref]
        cells: dict[str, dict] = {}
        for pid in order:
            for name, rec in per_product[pid]["keywords"].items():
                cells.setdefault(name, {**rec, "products": []})
        for name, cell in cells.items():
            have = [pid for pid in ids if name in per_product[pid]["keywords"]]
            cell["products"] = [] if len(have) == len(ids) else have
        out[ptype] = cells
    return out
