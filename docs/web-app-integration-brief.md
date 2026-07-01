# Web-app integration brief

For the web app / session that renders the keyword documentation from this repo.
Read this together with the canonical schema:
`tools/keyword-docgen/keyword-frontmatter.schema.yml`.

## Where the docs are

- Path: `03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/02-keywords/`
- One markdown file per keyword, in numbered category/subgroup folders.
- `00-overview.md` files are section intros.
- `_manifest/undocumented.md` lists keywords present in firmware but not yet documented.

## File format

Each keyword file = **YAML frontmatter** (machine-readable facts, generated from firmware)
+ **markdown body** (human-authored prose). Render both: frontmatter drives a Quick Facts
panel + availability matrix; the body is the article.

## Frontmatter fields

- `keyword`, `summary`, `category`
- `can_code` — CAN code of the **primary** cell (latest version). **Version-overridable:**
  if the CAN code differs by version, the differing cell's `can_code` appears inside its
  `overrides` entry (render it like any divergent field). Real example: `ProductSN` is 468
  in v4, 348 in v5.
- `availability: { standalone: [v4...], central-i: [...] }` — which product × version
  cells exist. A keyword present in only one version (e.g. `HWTimer` central-i `[v5]`)
  renders with the others marked "not available". **v5 is central-i only** (v5 moved to
  64-bit and dropped the standalone product), so `standalone` never contains `v5` — the
  standalone × v5 matrix cell is always N/A.
- `attributes` — facts for the primary cell: `access` (ro/rw), `scope` (axis/non-axis),
  `flash` (bool), `type` (scalar/array), `array_size`, `data_type`
  (int32/float32/int64/float64), `ok_in_motion`, `ok_motor_on`, `units` (user/none/func),
  `range` ([min,max] or null), `default`, `scaling`, `implemented` (final/partial).
- `overrides: { "<product>.<version>": { field: value, ... } }` — per-cell deltas from the
  primary. Values are a partial map of ONLY the fields that differ — may include any
  `attributes` field **and** `can_code`.
- `removed_in: [versions]` — versions scanned where the keyword is absent though older
  cells exist.

## Rendering rules

1. Layout: article body left, sticky info sidebar right.
2. `availability` → a 2×2 matrix (rows standalone/central-i, cols versions); cell =
   present / present-but-differs / not-available; highlight the primary cell.
3. Quick Facts panel: one row per `attributes` field (plus `can_code`), showing the
   PRIMARY (latest) values.
4. Divergence: if a field (including `can_code`) appears in any `overrides` entry, mark
   that row (dot) and reveal the differing value(s) on hover/expand.
5. `data_type` display labels: int32 = "32-bit integer (long)", float32 = "32-bit float",
   int64 = "64-bit integer (long long)", float64 = "64-bit double".
6. Arrays are **1-indexed**. Show indexes from `[1]`; index `[0]` does not exist.
   `array_size` counts a reserved slot 0, so the highest usable index = `array_size - 1`.
   (Note: bit-packed variables like `DInPort`/`DOutPort` use 0-based **bit** positions —
   that is a separate concept from array indexing; follow each page's wording.)
7. `range` may be null (unresolved) → omit the range row, don't print "null".
8. A `## Changes between versions` body section (when present) describes behavioral changes
   the facts can't express → render it prominently.

## Markdown specifics

- Relative `.md` links between keyword files.
- Diagrams: drawio exported as `.drawio.svg`, embedded as images.
- LaTeX for equations; some pages use `desmos-graph` code blocks.
- Command/example syntax in `## Examples` blocks: keywords are addressed with an
  **axis-letter prefix** (e.g. `APos`, `APosGain[1]`); read is the bare prefixed keyword
  (no `?` suffix), write is `AKeyword[index]=value`. Every keyword takes a prefix, including
  non-axis ones (for those the letter is don't-care).

## Status

- All documented keywords have v4 frontmatter facts (LTS seed).
- Fully enriched bodies: `01-system`, `05-inputs-outputs`.
- `01-system` also carries v5 facts (the v4/v5 matrix). Other categories are v4-only until
  a v5 pass is run for them.
- `control-tuning` is intentionally NOT enriched yet.
- Good test pages: `01-system/01-status/Identity.md` (index table),
  `01-system/01-status/ProductSN.md` (can_code divergence + serial model),
  `05-inputs-outputs/02-analog-inputs/AInDB.md` (desmos graph).
