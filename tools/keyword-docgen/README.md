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

The generator indexes keyword pages under `02-keywords/**`, `03-special-features/**`
and `05-legacy-keywords/**`. On a stem collision (a keyword documented in two places)
it targets the canonical entry — the one already carrying a `keyword:` field — and
leaves cross-ref stubs / legacy aliases (e.g. `JerkMode`, `AOutShifts`) untouched.

## Versioning (`version`)

Stamps each page's frontmatter with `last_updated` (git last-commit date) and
`doc_revision` (corpus CalVer), and writes `manifest.json` (path, keyword,
last_updated, doc_revision, body SHA-256) + `VERSION`.

    keyword-docgen version \
      --content-root "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
      --repo-root . --corpus-version 2026.06 --generated 2026-06-02 \
      --manifest-out ".../manifest.json" --version-file ".../VERSION"

- Stamps go AFTER the generator-owned facts and never disturb them; legacy
  frontmatter-less pages are manifest-only (not stamped on disk).
- **Incremental:** the existing `manifest.json` is loaded as a baseline. A page
  whose body SHA is unchanged keeps its prior `last_updated` and `doc_revision`;
  only changed/new pages get the current version + git date. So a stamp commit
  never pushes `last_updated` forward, and a release bumps `doc_revision` only
  for pages whose prose actually changed.

## RAG export (`rag-export`)

Emits one **document-level** JSON chunk per page (`rag-chunks.jsonl`, gitignored
— regenerate on demand), driven by `manifest.json`:

    keyword-docgen rag-export \
      --content-root ".../content" --manifest ".../manifest.json" \
      --out ".../rag-chunks.jsonl"

Each record is `{id, keyword, text, metadata, related}` where:
- `text` is the page body prefixed with a synthesized **fact header**
  (`Keyword X (CAN n; scope; access; units; range; v4/v5): summary`) so the
  embedding captures the structured facts, not just prose;
- `metadata` carries the frontmatter facts (availability, scope, units,
  can_code, range, …) plus `doc_revision`/`last_updated`/`sha256` for filtering,
  citation and **incremental re-embedding** (diff `sha256` vs the last index);
- `related` is the list of keywords this page links to, for graph-aware
  re-ranking.

Recommendation: index at the document level (each keyword page is a focused
unit); for the few very long pages, split by `##` section as child chunks.

See [`RAG-INDEXING.md`](RAG-INDEXING.md) for the full chunking design, the
chunk-size/embedder decision, the diagram-transcript plan, and the resume
checklist.

## Tests

    .venv/bin/python -m pytest -q
