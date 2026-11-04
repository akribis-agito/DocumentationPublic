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
panel + availability strip; the body is the article.

## Frontmatter fields

- `keyword`, `summary`, `category`
- `can_code` — CAN code of the **primary** cell. If the other product type numbers the
  keyword differently, its `can_code` appears in its `overrides` entry (render it like any
  divergent field).
- `availability: [controller, ci-master]` — the v5 product types the keyword exists on.
  `controller` is every drive and controller (32-bit), `ci-master` the AGM800 Central-i
  master family (64-bit). A type that is not listed is "not available".
- `products: [catalog IDs]` — present only when some products of a listed type lack the
  keyword: then it names the products that have it (e.g. `agd155-ec`). A listed type with
  none of its products here means every product of that type.
- `attributes` — facts for the primary cell (`controller` when available, else
  `ci-master`): `access` (ro/rw), `scope` (axis/non-axis), `flash` (bool), `type`
  (scalar/array), `array_size`, `data_type` (int32/float32/int64/float64), `ok_in_motion`,
  `ok_motor_on`, `units`, `range` ([min,max] or null), `default`, `scaling`, `implemented`.
- `overrides` — partial maps of ONLY the fields that differ (any `attributes` field and
  `can_code`), under two kinds of key:
  - a product type (`ci-master` / `controller`): the non-primary type's deltas from the
    primary cell;
  - a catalog ID (`agd155-ec`): one product's deltas from its own type's cell, such as a
    current range that follows the drive's full-scale current.

## Rendering rules

1. Layout: article body left, sticky info sidebar right.
2. `availability` → a one-row strip of two cells, `controller` then `ci-master`, labelled
   "Drives & controllers (32-bit)" and "AGM800 Central-i master (64-bit)". Cell = present /
   present-but-differs / not-available; a cell whose type has products listed in
   `products` names them.
3. Quick Facts panel: one row per `attributes` field (plus `can_code`), showing the
   primary cell's values.
4. Divergence: a field in `overrides.ci-master` (or `overrides.controller`) gets a marker
   and shows the other type's value on hover/expand. A field in any catalog-ID override is
   product-dependent: its row lists each such product with its own value, plus the cell
   value for the type's other products. Never show it as one value for the whole type.
5. `data_type` display labels: int32 = "32-bit integer (long)", float32 = "32-bit float",
   int64 = "64-bit integer (long long)", float64 = "64-bit double".
6. Arrays are **1-indexed**. Show indexes from `[1]`; index `[0]` does not exist.
   `array_size` counts a reserved slot 0, so the highest usable index = `array_size - 1`.
   (Note: bit-packed variables like `DInPort`/`DOutPort` use 0-based **bit** positions —
   that is a separate concept from array indexing; follow each page's wording.)
7. `range` may be null (unresolved) → omit the range row, don't print "null".
8. Behaviour that differs between product types and that the facts can't express is
   authored in the body prose; render the body as written.

## Markdown specifics

- Relative `.md` links between keyword files.
- Diagrams: drawio exported as `.drawio.svg`, embedded as images.
- LaTeX for equations; some pages use `desmos-graph` code blocks.
- Command/example syntax in `## Examples` blocks: keywords are addressed with an
  **axis-letter prefix** (e.g. `APos`, `APosGain[1]`); read is the bare prefixed keyword
  (no `?` suffix), write is `AKeyword[index]=value`. Every keyword takes a prefix, including
  non-axis ones (for those the letter is don't-care).

## Status

- The schema is v2 and the generator writes it (`tools/keyword-docgen`). The pages still
  carry v1 front matter (`availability` as a product × version map) until they are
  regenerated (DocumentationPublic#20).
- Fully enriched bodies: `01-system`, `05-inputs-outputs`.
- `control-tuning` is intentionally NOT enriched yet.
- Good test pages: `01-system/01-status/Identity.md` (index table),
  `05-inputs-outputs/02-analog-inputs/AInDB.md` (desmos graph).
