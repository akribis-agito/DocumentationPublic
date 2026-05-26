# Keyword Frontmatter Generator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI that parses the firmware `KeywordsTableArray` from `AG300_CTL01Params.c` and maintains version/product-aware YAML frontmatter on existing keyword docs, plus a manifest of undocumented keywords.

**Architecture:** A small Python package (`keyworddocgen`) with focused modules: a `#define` resolver, a table parser, a frontmatter reader/writer that preserves prose bodies verbatim, a merge engine that computes the primary cell + overrides + availability across `(product, version)` cells, a manifest writer, and an argparse CLI exposing `append` and `overwrite`. The generator is invoked once per branch checkout with the version asserted manually (`--version v4|v5`). It never creates, moves, or deletes doc files.

**Tech Stack:** Python 3.10+, `pytest`, `PyYAML`. No other runtime dependencies.

This plan implements **subsystem A (the generator)** from the design spec
(`docs/superpowers/specs/2026-05-27-keyword-documentation-system-design.md`). The pilot
content enrichment (subsystem B) and downstream renderers (subsystem C) are separate
follow-on efforts that depend on this tool.

---

## Key design decisions locked for this plan

- **Tool location:** `tools/keyword-docgen/` inside the documentation repo.
- **Version ordering:** `VERSION_ORDER = ["v4", "v5"]`; "latest" = highest index present.
- **Products:** `["standalone", "central-i"]`, mapped from `CONTROLLER` / `CI_MASTER` tables.
  `standalone` is the primary product (the cell shown in full).
- **`append` vs `overwrite`:** both scan one version's facts into existing docs.
  `append` **errors** if that version is already recorded in a doc (it is the safe
  first-time-add op). `overwrite` proceeds regardless (the idempotent refresh op).
- **`data_type`:** the LTS source encodes every keyword as 32-bit `long`, so the generator
  emits `int32` for all keywords for now. `infer_data_type()` is the single extension point
  for when the develop-branch encoding of `float32`/`int64`/`float64` is confirmed.
- **Body preservation:** the prose body after the closing `---` fence is captured and
  re-emitted byte-for-byte; only the YAML block is rewritten.
- **Absent keywords:** a doc whose keyword is absent from the current version's scan gets
  that version recorded in `removed_in`, with availability/primary recomputed from the
  remaining cells.

---

## File structure

```
tools/keyword-docgen/
  pyproject.toml                  # package metadata + pytest config
  README.md                       # usage (Task 9)
  keyworddocgen/
    __init__.py
    defines.py                    # Task 2 — parse headers, resolve #define expressions
    model.py                      # Task 3 — version/product constants + helpers
    table_parser.py               # Task 4 — parse KeywordsTableArray per product
    frontmatter.py                # Task 5 — read/split/write .md, preserve body
    merge.py                      # Task 6 — append/overwrite cell merge engine
    manifest.py                   # Task 7 — undocumented-keyword manifest
    cli.py                        # Task 8 — argparse entrypoint
  tests/
    fixtures/
      defs.h                      # tiny header with the #defines used in tests
      params_sample.c             # tiny KeywordsTableArray with both product tables
    test_defines.py
    test_table_parser.py
    test_frontmatter.py
    test_merge.py
    test_manifest.py
    test_cli.py
```

---

## Task 1: Project scaffold

**Files:**
- Create: `tools/keyword-docgen/pyproject.toml`
- Create: `tools/keyword-docgen/keyworddocgen/__init__.py`
- Create: `tools/keyword-docgen/tests/test_smoke.py`

- [ ] **Step 1: Create the package metadata**

`tools/keyword-docgen/pyproject.toml`:
```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "keyworddocgen"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["PyYAML>=6.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0"]

[project.scripts]
keyword-docgen = "keyworddocgen.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: Create the package init with the version constant**

`tools/keyword-docgen/keyworddocgen/__init__.py`:
```python
"""Generator that mines firmware KeywordsTableArray into doc frontmatter."""

__version__ = "0.1.0"
```

- [ ] **Step 3: Write a smoke test**

`tools/keyword-docgen/tests/test_smoke.py`:
```python
import keyworddocgen


def test_package_imports():
    assert keyworddocgen.__version__ == "0.1.0"
```

- [ ] **Step 4: Install dev deps and run the smoke test**

Run (from `tools/keyword-docgen/`):
```bash
python -m pip install -e ".[dev]"
python -m pytest -q
```
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add tools/keyword-docgen
git commit -m "feat(docgen): scaffold keyword generator package"
```

---

## Task 2: `#define` resolver

Resolves symbols like `POSGAIN_MAX` and arithmetic expressions like `CONTROL_SIZE-1`
to integers, from the firmware headers.

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/defines.py`
- Create: `tools/keyword-docgen/tests/fixtures/defs.h`
- Create: `tools/keyword-docgen/tests/test_defines.py`

- [ ] **Step 1: Create the fixture header**

`tools/keyword-docgen/tests/fixtures/defs.h`:
```c
#define CONTROL_SIZE        6          // 5 sets of gains + 1
#define POSGAIN_MIN         0
#define POSGAIN_MAX         20000      // range opened for overflow protection
#define POSGAIN_DFLT        0
#define DERIVED_MAX         (POSGAIN_MAX * 2)
#define DONTCARE            "n/a"
```

- [ ] **Step 2: Write failing tests**

`tools/keyword-docgen/tests/test_defines.py`:
```python
from pathlib import Path

from keyworddocgen.defines import DefineTable

FIX = Path(__file__).parent / "fixtures"


def make_table():
    return DefineTable.from_headers([FIX / "defs.h"])


def test_parses_plain_int():
    assert make_table().resolve("POSGAIN_MAX") == 20000


def test_strips_trailing_comment():
    assert make_table().resolve("CONTROL_SIZE") == 6


def test_resolves_arithmetic_expression():
    assert make_table().resolve("CONTROL_SIZE-1") == 5


def test_resolves_symbol_arithmetic():
    assert make_table().resolve("DERIVED_MAX") == 40000


def test_non_numeric_returns_none():
    assert make_table().resolve("DONTCARE") is None


def test_unknown_symbol_returns_none():
    assert make_table().resolve("NOPE") is None
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_defines.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'keyworddocgen.defines'`.

- [ ] **Step 4: Implement the resolver**

`tools/keyword-docgen/keyworddocgen/defines.py`:
```python
"""Parse C #define constants from headers and resolve integer expressions."""

from __future__ import annotations

import ast
import operator
import re
from pathlib import Path

_DEFINE_RE = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)\s+(.+?)\s*$")
_LINE_COMMENT = re.compile(r"//.*$")
_BLOCK_COMMENT = re.compile(r"/\*.*?\*/")

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.floordiv,
    ast.USub: operator.neg,
}


class DefineTable:
    def __init__(self, raw: dict[str, str]):
        self._raw = raw
        self._cache: dict[str, int | None] = {}

    @classmethod
    def from_headers(cls, paths: list[Path]) -> "DefineTable":
        raw: dict[str, str] = {}
        for path in paths:
            text = Path(path).read_text(errors="replace")
            for line in text.splitlines():
                m = _DEFINE_RE.match(line)
                if not m:
                    continue
                name, value = m.group(1), m.group(2)
                value = _LINE_COMMENT.sub("", value)
                value = _BLOCK_COMMENT.sub("", value)
                value = value.strip()
                if value:
                    raw[name] = value
        return cls(raw)

    def resolve(self, expr: str) -> int | None:
        """Resolve an expression to an int, or None if non-numeric/unknown."""
        expr = expr.strip()
        if expr in self._cache:
            return self._cache[expr]
        result = self._resolve(expr, set())
        if isinstance(expr, str) and re.fullmatch(r"[A-Za-z_]\w*", expr):
            self._cache[expr] = result
        return result

    def _resolve(self, expr: str, seen: set[str]) -> int | None:
        # Substitute known symbols with their raw definitions, recursively.
        def repl(m: re.Match) -> str:
            name = m.group(0)
            if name in seen:
                raise ValueError(f"cyclic define: {name}")
            if name in self._raw:
                inner = self._resolve(self._raw[name], seen | {name})
                if inner is None:
                    raise ValueError("non-numeric")
                return str(inner)
            raise ValueError(f"unknown symbol: {name}")

        try:
            substituted = re.sub(r"[A-Za-z_]\w*", repl, expr)
            node = ast.parse(substituted, mode="eval").body
            return self._eval(node)
        except (ValueError, SyntaxError, TypeError):
            return None

    def _eval(self, node: ast.AST) -> int:
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](self._eval(node.left), self._eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](self._eval(node.operand))
        raise ValueError("unsupported expression")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_defines.py -q`
Expected: 6 passed.

- [ ] **Step 6: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/defines.py tools/keyword-docgen/tests/test_defines.py tools/keyword-docgen/tests/fixtures/defs.h
git commit -m "feat(docgen): #define resolver with arithmetic expressions"
```

---

## Task 3: Model constants and helpers

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/model.py`
- Create: `tools/keyword-docgen/tests/test_model.py`

- [ ] **Step 1: Write failing tests**

`tools/keyword-docgen/tests/test_model.py`:
```python
from keyworddocgen.model import (
    PRODUCTS,
    PRIMARY_PRODUCT,
    VERSION_ORDER,
    cell_key,
    latest_version,
    infer_data_type,
)


def test_constants():
    assert VERSION_ORDER == ["v4", "v5"]
    assert PRODUCTS == ["standalone", "central-i"]
    assert PRIMARY_PRODUCT == "standalone"


def test_latest_version_picks_highest_rank():
    assert latest_version(["v4", "v5"]) == "v5"
    assert latest_version(["v4"]) == "v4"


def test_latest_version_empty_is_none():
    assert latest_version([]) is None


def test_cell_key_format():
    assert cell_key("standalone", "v4") == "standalone.v4"


def test_infer_data_type_defaults_int32():
    assert infer_data_type({}) == "int32"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_model.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement the model**

`tools/keyword-docgen/keyworddocgen/model.py`:
```python
"""Shared constants and helpers for products, versions, and data types."""

from __future__ import annotations

VERSION_ORDER = ["v4", "v5"]
PRODUCTS = ["standalone", "central-i"]
PRIMARY_PRODUCT = "standalone"


def version_rank(version: str) -> int:
    return VERSION_ORDER.index(version)


def latest_version(versions: list[str]) -> str | None:
    if not versions:
        return None
    return max(versions, key=version_rank)


def cell_key(product: str, version: str) -> str:
    return f"{product}.{version}"


def infer_data_type(record: dict) -> str:
    """Numeric type of a keyword.

    The LTS source encodes every keyword as 32-bit long, so we return int32.
    This is the single extension point for develop-branch float32/int64/float64
    encoding once it is confirmed (see spec risks).
    """
    return "int32"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_model.py -q`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/model.py tools/keyword-docgen/tests/test_model.py
git commit -m "feat(docgen): model constants and helpers"
```

---

## Task 4: Table parser

Parses both product tables out of a `Params.c` and converts each entry into a
`{mnemonic: {"can_code": int, "attributes": {...}}}` map per product.

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/table_parser.py`
- Create: `tools/keyword-docgen/tests/fixtures/params_sample.c`
- Create: `tools/keyword-docgen/tests/test_table_parser.py`

- [ ] **Step 1: Create the fixture Params.c**

`tools/keyword-docgen/tests/fixtures/params_sample.c`:
```c
#if (PRODUCT_TYPE == CONTROLLER) && (IS_BOOT_IMAGE == 0)
const struct STRUCT_KEYWORDS_TABLE KeywordsTableArray[NUM_OF_CAN_CODES] = \
{ \
    {0,   "ZZZZ",    0,     0,     0,             0,  0,        0,      0,       0,       0,       0,    0, 0,             ZZ_MIN,      ZZ_MAX,    ZZ_DFLT,    1, &glZZ,      NULL, NULL},\
    {100, "PosGain", PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON,ISARRAY, FLASH,   AXIS,    FINAL,0, CONTROL_SIZE-1,POSGAIN_MIN, POSGAIN_MAX,POSGAIN_DFLT,1, &glPosGain, NULL, NULL},\
    {101, "PosKi",   PARAM, PARAM, NO_USER_UNITS, RW, NOMOTN,   OKMTRON,NOARRAY, NOFLASH, NON_AXIS,FINAL,0, 0,             POSKI_MIN,   POSKI_MAX, POSKI_DFLT, 1, &glPosKi,   NULL, NULL},\
};
#endif
#if (PRODUCT_TYPE == CI_MASTER) && (IS_BOOT_IMAGE == 0)
const struct STRUCT_KEYWORDS_TABLE KeywordsTableArray[NUM_OF_CAN_CODES] = \
{ \
    {100, "PosGain", PARAM, PARAM, NO_USER_UNITS, RW, OKINMOTN, OKMTRON,ISARRAY, FLASH,   AXIS,    FINAL,0, CONTROL_SIZE-1,POSGAIN_MIN, POSGAIN_MAX,POSGAIN_DFLT,1, &glPosGain, NULL, NULL},\
};
#endif
```

Add the matching defines to `tools/keyword-docgen/tests/fixtures/defs.h` (append):
```c
#define POSKI_MIN           0
#define POSKI_MAX           1000
#define POSKI_DFLT          5
```

- [ ] **Step 2: Write failing tests**

`tools/keyword-docgen/tests/test_table_parser.py`:
```python
from pathlib import Path

from keyworddocgen.defines import DefineTable
from keyworddocgen.table_parser import parse_params

FIX = Path(__file__).parent / "fixtures"


def parse():
    defines = DefineTable.from_headers([FIX / "defs.h"])
    return parse_params(FIX / "params_sample.c", defines)


def test_splits_two_products():
    tables = parse()
    assert set(tables) == {"standalone", "central-i"}


def test_skips_sentinel_zzzz_row():
    assert "ZZZZ" not in parse()["standalone"]


def test_posgain_attributes_standalone():
    pg = parse()["standalone"]["PosGain"]
    assert pg["can_code"] == 100
    a = pg["attributes"]
    assert a["access"] == "rw"
    assert a["scope"] == "axis"
    assert a["flash"] is True
    assert a["type"] == "array"
    assert a["array_size"] == 6          # CONTROL_SIZE-1 -> 5, +1
    assert a["data_type"] == "int32"
    assert a["ok_in_motion"] is True
    assert a["ok_motor_on"] is True
    assert a["units"] == "none"
    assert a["range"] == [0, 20000]
    assert a["default"] == 0
    assert a["scaling"] == 1.0
    assert a["implemented"] == "final"


def test_poski_scalar_non_axis_nomotion():
    pk = parse()["standalone"]["PosKi"]
    a = pk["attributes"]
    assert a["type"] == "scalar"
    assert a["array_size"] == 1
    assert a["scope"] == "non-axis"
    assert a["flash"] is False
    assert a["ok_in_motion"] is False
    assert a["range"] == [0, 1000]


def test_central_i_has_only_posgain():
    assert set(parse()["central-i"]) == {"PosGain"}
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_table_parser.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 4: Implement the parser**

`tools/keyword-docgen/keyworddocgen/table_parser.py`:
```python
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_table_parser.py -q`
Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/table_parser.py tools/keyword-docgen/tests/test_table_parser.py tools/keyword-docgen/tests/fixtures
git commit -m "feat(docgen): parse KeywordsTableArray into per-product records"
```

---

## Task 5: Frontmatter reader/writer (preserves body)

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/frontmatter.py`
- Create: `tools/keyword-docgen/tests/test_frontmatter.py`

- [ ] **Step 1: Write failing tests**

`tools/keyword-docgen/tests/test_frontmatter.py`:
```python
from keyworddocgen.frontmatter import split_doc, render_doc


BODY = "# PosGain\n\n**Definition:**\n\nProportional gain.\n"


def test_split_no_frontmatter_returns_empty_and_full_body():
    fm, body = split_doc(BODY)
    assert fm == {}
    assert body == BODY


def test_split_existing_frontmatter():
    text = "---\nkeyword: PosGain\ncan_code: 100\n---\n" + BODY
    fm, body = split_doc(text)
    assert fm["keyword"] == "PosGain"
    assert fm["can_code"] == 100
    assert body == BODY


def test_render_roundtrips_body_verbatim():
    fm = {"keyword": "PosGain", "can_code": 100}
    out = render_doc(fm, BODY)
    fm2, body2 = split_doc(out)
    assert fm2 == fm
    assert body2 == BODY


def test_render_preserves_key_order():
    fm = {"keyword": "PosGain", "summary": "x", "can_code": 100}
    out = render_doc(fm, BODY)
    assert out.index("keyword") < out.index("summary") < out.index("can_code")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_frontmatter.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement the frontmatter module**

`tools/keyword-docgen/keyworddocgen/frontmatter.py`:
```python
"""Read and write Obsidian-style frontmatter while preserving the prose body."""

from __future__ import annotations

import yaml

_FENCE = "---\n"


def split_doc(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Body is preserved exactly."""
    if not text.startswith(_FENCE):
        return {}, text
    rest = text[len(_FENCE):]
    end = rest.find("\n" + _FENCE.strip() + "\n")
    if end == -1:
        return {}, text
    yaml_block = rest[:end]
    body = rest[end + len("\n" + _FENCE.strip() + "\n"):]
    data = yaml.safe_load(yaml_block) or {}
    return data, body


def render_doc(frontmatter: dict, body: str) -> str:
    """Render frontmatter + body back into a document string."""
    dumped = yaml.safe_dump(
        frontmatter, sort_keys=False, default_flow_style=False, allow_unicode=True
    )
    return f"{_FENCE}{dumped}{_FENCE}{body}"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_frontmatter.py -q`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/frontmatter.py tools/keyword-docgen/tests/test_frontmatter.py
git commit -m "feat(docgen): frontmatter read/write preserving prose body"
```

---

## Task 6: Merge engine (append / overwrite)

The heart of the tool: incorporate one version's scanned cells into a doc's frontmatter,
then recompute `availability`, `attributes` (primary cell), `overrides`, and `removed_in`.

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/merge.py`
- Create: `tools/keyword-docgen/tests/test_merge.py`

- [ ] **Step 1: Write failing tests**

`tools/keyword-docgen/tests/test_merge.py`:
```python
import pytest

from keyworddocgen.merge import merge_version, VersionAlreadyRecorded


def attrs(**over):
    base = {
        "access": "rw", "scope": "axis", "flash": True, "type": "array",
        "array_size": 6, "data_type": "int32", "ok_in_motion": True,
        "ok_motor_on": True, "units": "none", "range": [0, 20000],
        "default": 0, "scaling": 1.0, "implemented": "final",
    }
    base.update(over)
    return base


def scan_present(**over):
    return {
        "standalone": {"can_code": 100, "attributes": attrs(**over)},
        "central-i": {"can_code": 100, "attributes": attrs(**over)},
    }


def test_first_append_sets_primary_and_availability():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    assert fm["availability"] == {"standalone": ["v4"], "central-i": ["v4"]}
    assert fm["attributes"]["range"] == [0, 20000]
    assert fm.get("overrides", {}) == {}


def test_appending_v5_makes_v5_primary_and_demotes_v4():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(range=[0, 100000]), "v5", mode="append")
    assert fm["attributes"]["range"] == [0, 100000]          # v5 is primary
    assert fm["overrides"]["standalone.v4"]["range"] == [0, 20000]
    assert fm["availability"]["standalone"] == ["v4", "v5"]


def test_append_errors_if_version_already_present():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    with pytest.raises(VersionAlreadyRecorded):
        merge_version(fm, scan_present(), "v4", mode="append")


def test_overwrite_replaces_existing_version():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(default=9), "v4", mode="overwrite")
    assert fm["attributes"]["default"] == 9


def test_data_type_divergence_recorded_in_overrides():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(data_type="float64"), "v5", mode="append")
    assert fm["attributes"]["data_type"] == "float64"
    assert fm["overrides"]["standalone.v4"]["data_type"] == "int32"


def test_absent_keyword_records_removed_in():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    absent = {"standalone": None, "central-i": None}
    fm = merge_version(fm, absent, "v5", mode="append")
    assert fm["removed_in"] == ["v5"]
    assert fm["availability"]["standalone"] == ["v4"]


def test_preserves_existing_summary_and_category():
    fm = {"summary": "Proportional gain.", "category": "control-tuning"}
    fm = merge_version(fm, scan_present(), "v4", mode="append")
    assert fm["summary"] == "Proportional gain."
    assert fm["category"] == "control-tuning"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_merge.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement the merge engine**

`tools/keyword-docgen/keyworddocgen/merge.py`:
```python
"""Merge a scanned version's facts into a doc's frontmatter."""

from __future__ import annotations

from .model import (
    PRODUCTS,
    PRIMARY_PRODUCT,
    VERSION_ORDER,
    cell_key,
    latest_version,
    version_rank,
)


class VersionAlreadyRecorded(Exception):
    """Raised by append when the version is already present in the doc."""


def _reconstruct_cells(fm: dict) -> dict[tuple[str, str], dict]:
    """Rebuild {(product, version): attributes} from primary + overrides."""
    cells: dict[tuple[str, str], dict] = {}
    primary = fm.get("attributes")
    availability = fm.get("availability", {})
    overrides = fm.get("overrides", {})
    for product in PRODUCTS:
        for version in availability.get(product, []):
            attrs = dict(primary) if primary else {}
            attrs.update(overrides.get(cell_key(product, version), {}))
            cells[(product, version)] = attrs
    return cells


def _recorded_versions(fm: dict) -> set[str]:
    versions: set[str] = set()
    for vs in fm.get("availability", {}).values():
        versions.update(vs)
    return versions


def merge_version(fm: dict, scan_cells: dict, version: str, mode: str) -> dict:
    """Return a new frontmatter dict with `version`'s facts merged in.

    `scan_cells` maps product -> {"can_code", "attributes"} or None if absent.
    `mode` is "append" (errors if version already present) or "overwrite".
    """
    fm = dict(fm or {})
    if mode == "append" and version in _recorded_versions(fm):
        raise VersionAlreadyRecorded(version)

    cells = _reconstruct_cells(fm)
    can_codes = {k: fm.get("can_code") for k in cells}

    # Drop any prior cells for this version, then apply the scan.
    for product in PRODUCTS:
        cells.pop((product, version), None)
        cell = scan_cells.get(product)
        if cell is not None:
            cells[(product, version)] = cell["attributes"]
            can_codes[(product, version)] = cell["can_code"]

    # removed_in: a version we scanned but where the keyword is now absent,
    # while older cells still exist.
    removed_in = set(fm.get("removed_in", []))
    removed_in.discard(version)
    scanned_absent = all(scan_cells.get(p) is None for p in PRODUCTS)
    if scanned_absent and cells:
        removed_in.add(version)

    availability = {
        product: sorted(
            [v for (p, v) in cells if p == product], key=version_rank
        )
        for product in PRODUCTS
    }

    primary_cell = _pick_primary(cells)
    result = dict(fm)
    result["availability"] = availability
    if primary_cell is not None:
        primary_attrs = cells[primary_cell]
        result["can_code"] = can_codes.get(primary_cell, fm.get("can_code"))
        result["attributes"] = primary_attrs
        result["overrides"] = _compute_overrides(cells, primary_cell, primary_attrs)
    if removed_in:
        result["removed_in"] = sorted(removed_in, key=version_rank)
    else:
        result.pop("removed_in", None)
    return result


def _pick_primary(cells: dict[tuple[str, str], dict]) -> tuple[str, str] | None:
    for product in [PRIMARY_PRODUCT] + [p for p in PRODUCTS if p != PRIMARY_PRODUCT]:
        versions = [v for (p, v) in cells if p == product]
        latest = latest_version(versions)
        if latest is not None:
            return (product, latest)
    return None


def _compute_overrides(cells, primary_cell, primary_attrs) -> dict:
    overrides: dict[str, dict] = {}
    for (product, version), attrs in cells.items():
        if (product, version) == primary_cell:
            continue
        diff = {k: v for k, v in attrs.items() if v != primary_attrs.get(k)}
        if diff:
            overrides[cell_key(product, version)] = diff
    return overrides
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_merge.py -q`
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/merge.py tools/keyword-docgen/tests/test_merge.py
git commit -m "feat(docgen): version merge engine with primary/overrides/removed_in"
```

---

## Task 7: Undocumented-keyword manifest

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/manifest.py`
- Create: `tools/keyword-docgen/tests/test_manifest.py`

- [ ] **Step 1: Write failing tests**

`tools/keyword-docgen/tests/test_manifest.py`:
```python
from keyworddocgen.manifest import render_manifest


def test_lists_undocumented_with_products_and_version():
    scanned = {
        "standalone": {"PosGain", "PosKi"},
        "central-i": {"PosGain"},
    }
    documented = {"PosGain"}
    out = render_manifest(scanned, documented, version="v5")
    assert "PosKi" in out
    assert "PosGain" not in out.split("\n\n", 1)[-1]   # documented excluded
    assert "standalone" in out
    assert "v5" in out


def test_empty_when_all_documented():
    scanned = {"standalone": {"PosGain"}, "central-i": set()}
    out = render_manifest(scanned, {"PosGain"}, version="v5")
    assert "PosKi" not in out
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_manifest.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement the manifest**

`tools/keyword-docgen/keyworddocgen/manifest.py`:
```python
"""Render a manifest of keywords present in the scan but missing a doc."""

from __future__ import annotations

from .model import PRODUCTS


def render_manifest(
    scanned: dict[str, set[str]], documented: set[str], version: str
) -> str:
    """Return a markdown manifest listing undocumented keywords.

    `scanned` maps product -> set of mnemonics found in that product's table.
    `documented` is the set of mnemonics that already have a doc file.
    """
    all_scanned: set[str] = set()
    for names in scanned.values():
        all_scanned |= names
    undocumented = sorted(all_scanned - documented)

    lines = [
        "# Undocumented keywords",
        "",
        f"Generated from the {version} scan. Each keyword below exists in "
        "`Params.c` but has no doc file yet.",
        "",
        "| Keyword | Products | First seen |",
        "| --- | --- | --- |",
    ]
    for name in undocumented:
        products = ", ".join(p for p in PRODUCTS if name in scanned.get(p, set()))
        lines.append(f"| {name} | {products} | {version} |")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_manifest.py -q`
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/manifest.py tools/keyword-docgen/tests/test_manifest.py
git commit -m "feat(docgen): undocumented-keyword manifest renderer"
```

---

## Task 8: CLI wiring + integration test

Ties the modules together: parse a `Params.c`, walk the docs tree, merge frontmatter into
existing docs only, and write the manifest. Exposes `append` and `overwrite`.

**Files:**
- Create: `tools/keyword-docgen/keyworddocgen/cli.py`
- Create: `tools/keyword-docgen/tests/test_cli.py`

- [ ] **Step 1: Write failing integration test**

`tools/keyword-docgen/tests/test_cli.py`:
```python
from pathlib import Path

import yaml

from keyworddocgen.cli import run
from keyworddocgen.frontmatter import split_doc

FIX = Path(__file__).parent / "fixtures"


def setup_docs(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    kw = docs / "02-keywords" / "11-control-tuning"
    kw.mkdir(parents=True)
    # Only PosGain has a doc; PosKi will land in the manifest.
    (kw / "PosGain.md").write_text(
        "---\nsummary: Proportional gain.\n---\n# PosGain\n\nProportional gain.\n"
    )
    return docs


def run_v4(docs, mode="append"):
    return run([
        mode, "--version", "v4",
        "--params", str(FIX / "params_sample.c"),
        "--defines", str(FIX / "defs.h"),
        "--docs-root", str(docs),
        "--manifest", str(docs / "_manifest" / "undocumented.md"),
    ])


def test_updates_existing_doc_frontmatter(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    fm, body = split_doc((docs / "02-keywords/11-control-tuning/PosGain.md").read_text())
    assert fm["can_code"] == 100
    assert fm["attributes"]["range"] == [0, 20000]
    assert fm["availability"]["standalone"] == ["v4"]
    assert fm["summary"] == "Proportional gain."        # preserved
    assert "Proportional gain." in body                  # body preserved


def test_does_not_create_doc_for_undocumented_keyword(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    assert not (docs / "02-keywords/11-control-tuning/PosKi.md").exists()


def test_writes_manifest_with_undocumented(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    manifest = (docs / "_manifest" / "undocumented.md").read_text()
    assert "PosKi" in manifest
    assert "PosGain" not in manifest


def test_append_twice_same_version_errors(tmp_path, capsys):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    rc = run_v4(docs)                # second append of v4
    assert rc != 0
    assert "already recorded" in capsys.readouterr().err.lower()


def test_overwrite_twice_is_idempotent(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs, mode="append")
    rc = run_v4(docs, mode="overwrite")
    assert rc == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_cli.py -q`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement the CLI**

`tools/keyword-docgen/keyworddocgen/cli.py`:
```python
"""Command-line entrypoint: append/overwrite frontmatter + write manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .defines import DefineTable
from .frontmatter import render_doc, split_doc
from .manifest import render_manifest
from .merge import VersionAlreadyRecorded, merge_version
from .model import PRODUCTS
from .table_parser import parse_params


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="keyword-docgen")
    sub = parser.add_subparsers(dest="mode", required=True)
    for mode in ("append", "overwrite"):
        p = sub.add_parser(mode)
        p.add_argument("--version", required=True, choices=["v4", "v5"])
        p.add_argument("--params", required=True, type=Path)
        p.add_argument("--defines", required=True, type=Path, nargs="+",
                       help="Header file(s) defining MIN/MAX/DFLT/sizes")
        p.add_argument("--docs-root", required=True, type=Path)
        p.add_argument("--manifest", required=True, type=Path)
    return parser


def _index_docs(docs_root: Path) -> dict[str, Path]:
    """Map mnemonic -> doc path for every existing keyword .md."""
    index: dict[str, Path] = {}
    keywords_dir = docs_root / "02-keywords"
    for path in keywords_dir.rglob("*.md"):
        if path.stem.startswith("00-"):
            continue
        index[path.stem] = path
    return index


def run(argv: list[str]) -> int:
    args = _build_parser().parse_args(argv)
    defines = DefineTable.from_headers(list(args.defines))
    tables = parse_params(args.params, defines)
    docs = _index_docs(args.docs_root)

    # Build per-keyword scan cells across products.
    all_keywords = set()
    for names in tables.values():
        all_keywords |= set(names)

    for mnemonic in sorted(all_keywords):
        path = docs.get(mnemonic)
        if path is None:
            continue  # undocumented -> handled by the manifest below
        scan_cells = {p: tables.get(p, {}).get(mnemonic) for p in PRODUCTS}
        fm, body = split_doc(path.read_text())
        fm.setdefault("keyword", mnemonic)
        try:
            new_fm = merge_version(fm, scan_cells, args.version, mode=args.mode)
        except VersionAlreadyRecorded:
            print(
                f"error: {mnemonic}: version {args.version} already recorded "
                f"(use 'overwrite' to refresh)",
                file=sys.stderr,
            )
            return 1
        path.write_text(render_doc(new_fm, body))

    scanned = {p: set(tables.get(p, {})) for p in PRODUCTS}
    manifest = render_manifest(scanned, set(docs), args.version)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(manifest)
    return 0


def main() -> None:
    sys.exit(run(sys.argv[1:]))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_cli.py -q`
Expected: 5 passed.

- [ ] **Step 5: Run the full suite**

Run: `python -m pytest -q`
Expected: all tests pass (defines, model, table_parser, frontmatter, merge, manifest, cli, smoke).

- [ ] **Step 6: Commit**

```bash
git add tools/keyword-docgen/keyworddocgen/cli.py tools/keyword-docgen/tests/test_cli.py
git commit -m "feat(docgen): CLI wiring append/overwrite + manifest"
```

---

## Task 9: Usage documentation + real-source dry run

**Files:**
- Create: `tools/keyword-docgen/README.md`

- [ ] **Step 1: Write the README**

`tools/keyword-docgen/README.md`:
```markdown
# keyword-docgen

Generates version/product-aware YAML frontmatter on keyword docs from the firmware
`KeywordsTableArray` in `AG300_CTL01Params.c`. It only updates docs that already exist
and lists undocumented keywords in a manifest. See the design spec at
`docs/superpowers/specs/2026-05-27-keyword-documentation-system-design.md`.

## Install

    cd tools/keyword-docgen
    python -m pip install -e ".[dev]"

## Usage

Run once per branch checkout, asserting the version manually.

    # On the LTS branch checkout (assert as v4):
    keyword-docgen append --version v4 \
      --params /path/to/Firmware-Main/CommonC/AG300_CTL01Params.c \
      --defines /path/to/Firmware-Main/CommonIncludes/AG300_CTL01Params.h \
                /path/to/Firmware-Main/CommonIncludes/AG300_CTL01ParamsCommon.h \
                /path/to/Firmware-Main/CommonIncludes/CentraliLib.h \
      --docs-root "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
      --manifest  "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/_manifest/undocumented.md"

    # On the develop branch checkout (assert as v5):
    keyword-docgen append --version v5 ...

- `append` errors if the version is already recorded in a doc (safe first add).
- `overwrite` re-scans and replaces that version's facts (idempotent refresh).
```

- [ ] **Step 2: Dry run against the real firmware source**

Run (adjust paths to the actual `Firmware-Main` checkout, currently on the LTS branch),
writing into a scratch copy so nothing is committed accidentally:
```bash
cd tools/keyword-docgen
python -m keyworddocgen.cli append --version v4 \
  --params /Users/cj/Dev/Firmware-Main/CommonC/AG300_CTL01Params.c \
  --defines /Users/cj/Dev/Firmware-Main/CommonIncludes/AG300_CTL01Params.h \
            /Users/cj/Dev/Firmware-Main/CommonIncludes/AG300_CTL01ParamsCommon.h \
            /Users/cj/Dev/Firmware-Main/CommonIncludes/CentraliLib.h \
  --docs-root "/Users/cj/Dev/DocumentationPublic/03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
  --manifest /tmp/undocumented-v4.md
```
Expected: command exits 0; `/tmp/undocumented-v4.md` lists keywords with no doc;
`git diff` in the docs repo shows frontmatter added to existing keyword pages with no
change to their prose bodies. Inspect `PosGain.md` to confirm `range: [0, 20000]`,
`default: 0`, `availability.standalone: [v4]`. Review the diff, then revert it
(`git checkout -- "03 USER MANUALS"`) since real enrichment is a later effort.

- [ ] **Step 3: Commit the README**

```bash
git add tools/keyword-docgen/README.md
git commit -m "docs(docgen): usage README and dry-run notes"
```

---

## Self-review notes

- **Spec coverage:** schema fields (§4) → Task 4 attribute mapping + Task 6 frontmatter
  shape; `data_type` vocabulary (§4) → `infer_data_type` (Task 3) + override handling
  (Task 6); generated facts (§4 source) → Tasks 2/4; append/overwrite + `--version`
  (§6) → Tasks 6/8; both product tables (§6) → Task 4; macro resolution (§6) → Task 2;
  body preservation (§6) → Task 5/Task 8; manifest (§6) → Task 7/8; "never create/move
  files" (§3) → Task 8 `_index_docs` only updates existing docs + Task 8 test
  `test_does_not_create_doc_for_undocumented_keyword`. Acceptance criteria §10 items
  1–4 are covered here; item 5 (pilot enrichment + render) is the separate follow-on.
- **Deferred deliberately:** pilot content enrichment of `11-control-tuning` and any
  renderer — out of this plan's scope per the spec.
- **Known follow-up:** `data_type` for v5's `float32`/`int64`/`float64` returns `int32`
  until the develop-branch encoding is confirmed (spec risk); only `infer_data_type`
  changes when it is.
```
