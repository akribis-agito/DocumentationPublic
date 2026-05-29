# keyword-docgen

Generates version/product-aware YAML frontmatter on keyword docs from the firmware
`KeywordsTableArray` in `AG300_CTL01Params.c`. It only updates docs that already exist
and lists undocumented keywords in a manifest. See the design spec at
`docs/superpowers/specs/2026-05-27-keyword-documentation-system-design.md`.

## Install

    cd tools/keyword-docgen
    python3 -m venv .venv
    .venv/bin/python -m pip install -e ".[dev]"

## Usage

Run once per branch checkout, asserting the version manually.

    # On the LTS branch checkout (assert as v4):
    keyword-docgen append --version v4 \
      --params /path/to/Firmware-Main/CommonC/AG300_CTL01Params.c \
      --defines /path/to/Firmware-Main/CommonIncludes/AG300_CTL01Params.h \
                /path/to/Firmware-Main/CommonIncludes/AG300_CTL01ParamsCommon.h \
                /path/to/Firmware-Main/CommonIncludes/CentraliLib.h \
                /path/to/Firmware-Main/CommonIncludes/AG300_CTL01Interpreter.h \
                /path/to/Firmware-Main/CommonIncludes/AG300_CTL01UProgFuncs.h \
      --docs-root "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
      --manifest  "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/_manifest/undocumented.md"

    # On the develop branch checkout (assert as v5):
    keyword-docgen append --version v5 ...

- `append` errors if the version is already recorded in a doc (safe first add).
- `overwrite` re-scans and replaces that version's facts (idempotent refresh).
- **Pass the full `--defines` header set.** Range/default/scaling macros chain across
  several headers; omitting one silently regresses the affected keywords to `null`:
  - `AG300_CTL01Interpreter.h` — `LONG64_MAX`/`LONG64_MIN` (= ±(2^51 − 1)); the 64-bit
    range macros expand to `(long double) LONG64_MAX`.
  - `AG300_CTL01UProgFuncs.h` — `USER_PROGRAM_NUMERIC_STACK_DEPTH`,
    `USER_PROGRAM_CALL_STACK_DEPTH`, etc., used by the user-program stack keyword ranges.
- The resolver handles floats (e.g. scaling `1.526`, float defaults, `1000.0f`), treats
  the float-type limit `±3.4e38` (`FLOAT_MIN`/`FLOAT_MAX` and aliases) as unbounded
  (`range: null`), and `overwrite` never downgrades a previously-resolved numeric
  range/default to `null` when a re-scan can't resolve it (e.g. a constant that moved
  from `#define` to an enum). A few constants are firmware enums, not `#define`s
  (`MAX_FUNCS`, `MAX_TASKS`, the PWM-range terms), so those ranges rely on that guard.

## Tests

    .venv/bin/python -m pytest -q
