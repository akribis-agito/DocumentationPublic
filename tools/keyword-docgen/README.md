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
      --docs-root "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
      --manifest  "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/_manifest/undocumented.md"

    # On the develop branch checkout (assert as v5):
    keyword-docgen append --version v5 ...

- `append` errors if the version is already recorded in a doc (safe first add).
- `overwrite` re-scans and replaces that version's facts (idempotent refresh).

## Tests

    .venv/bin/python -m pytest -q
