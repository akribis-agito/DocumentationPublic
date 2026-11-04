# keyword-docgen

Generates product-type-aware YAML frontmatter (schema v2,
[`keyword-frontmatter.schema.yml`](keyword-frontmatter.schema.yml)) on keyword docs from
the firmware v5 `KeywordsTableArray` in `AG300_CTL01Params.c`. It only updates docs that
already exist and lists undocumented keywords in a manifest. See the design spec at
`docs/superpowers/specs/2026-05-27-keyword-documentation-system-design.md`.

## Install

    cd tools/keyword-docgen
    python3 -m venv .venv
    .venv/bin/python -m pip install -e ".[dev]"

## Usage

Run against a v5 Firmware-Main checkout (develop, 5.3.0-rc7 and later):

    keyword-docgen overwrite \
      --firmware-root /path/to/Firmware-Main \
      --docs-root "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content" \
      --manifest  "03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/_manifest/undocumented.md"

- `append` errors if a doc already carries generated facts (`availability`), so it is a
  safe first add.
- `overwrite` re-scans and replaces the generated facts (idempotent refresh). On a page
  that still has schema-v1 front matter it replaces the v1 facts; none of them carry over.

### The KW_ROW table

v5 has one positional `KW_ROW(idx, "name", …)` table in `CommonC/AG300_CTL01Params.c`;
the row wrappers (`KW_ROW_CIM_ONLY`, `KW_ROW_CTL_ONLY`, `KW_ROW_EC`, `KW_ROW_7SEG`,
`KW_ROW_AUTOGAIN`, …) and macros such as `AXIS_CIM` and `CW_TYPETAG_POS` decide what each
product gets. The generator does not follow those macros itself: it runs the file through
a C preprocessor once per `PRODUCT_*` in `CommonIncludes/ProductConfig.h`, configured as the
PC-simulation build configures it (`-DPROCESSOR=4 -DPRODUCT=PRODUCT_…`, the
`Platform/PC` include path), and reads the expanded rows.

- **Needs `clang` or `gcc` on `PATH`** (or `KEYWORD_DOCGEN_CC=<path>`), for the tests too.
- The CAN code is the row's position. Min/max/default/scaling resolve through the value
  pools of the same expansion, so they are what that product's build serves.
- Products collapse to the two product types, `controller` (`CONTROLLER`) and `ci-master`
  (`CI_MASTER`). A type's facts come from its reference product (`agd301-et-2d05`, the
  PC-simulation default, and `agm800`), or from the first product that has the keyword
  when the reference does not. A keyword on only some products of a type lists them in
  `products` (catalog IDs, `PRODUCT_AGD155_EC` → `agd155-ec`).
- The primary cell is `controller` when the keyword has one, else `ci-master`; the other
  type's differences go to `overrides.<type>`. `data_type` comes from the row's type tag,
  so it is always one of `int32` / `float32` / `int64` / `float64`; `overwrite` replaces
  the stray v1 `float` / `double` spellings with it.
- The resolver treats the float-type limit `±3.4e38` as unbounded (`range: null`), and
  `overwrite` never downgrades a previously-resolved numeric range/default of the same
  product type to `null` when a re-scan can't resolve it.

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
