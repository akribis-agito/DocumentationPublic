# Changelog

All notable changes to the **Keyword Reference Manual** are recorded here.

Revisions use **CalVer** (`YYYY.MM`). The current corpus revision is in
[`VERSION`](VERSION); each page also carries its own `last_updated` and
`doc_revision` in frontmatter, and [`manifest.json`](manifest.json) lists every
page with its revision and a body content-hash so a consumer can detect exactly
which pages changed between two revisions.

> Documentation versioning is independent of the firmware versions a keyword
> supports (the `availability: v4 / v5` facts in each page's frontmatter). A
> `doc_revision` tells you how current your copy of the *documentation* is; it
> says nothing about firmware compatibility.

## 2026.06 — 2026-06-02

First versioned release: a baseline of the corpus (926 pages) plus the
versioning machinery itself.

### Added

- **Documentation versioning.** Per-page `last_updated` (git last-commit date)
  and `doc_revision` (corpus CalVer) frontmatter stamps, a corpus `VERSION`
  file, and a machine-readable `manifest.json` (path, keyword, last_updated,
  doc_revision, body SHA-256) for incremental re-indexing. Stamps are derived
  automatically from git via `keyword-docgen version`.

### Changed / Fixed — firmware-grounded audit

247 keyword pages were corrected and completed against the firmware that
implements them (v4 and v5), each change verified against the firmware behavior
and independently re-checked:

- **Central-i:** `CIDeviceType` is rejected while a port is connected (error
  214), with the simulation-class encodings, power-on default, and 12-port
  status window corrected; `CIStatus`/`CIDisconnect`/`CIGlobalStat`/
  `CIOfflineSend` aligned to firmware.
- **System / status:** `AllStat` works over all four channels and rejects a
  function-type keyword (error 178); `ParamAbout` returns a single parameter's
  min/max/default (assignment-form mandatory); `ProductSN` updates `Identity`
  only at start-up; `About` streams the keyword-table definition; user-units
  group members conflict-check against embedded scaling (error 338, v5).
- **Control tuning:** filter / feed-forward / input-shaping / gain-scheduling
  pages corrected, including the CalcFilters motor-on gating (errors 102/87),
  force-filter validation (325/326), and the shaping/modulus fault (1032).
- **Gantry tuning:** corrected from a yaw-only model to the firmware's
  **per-axis** common/differential control model; v5 gain-scheduled arrays and
  ranges documented.
- **Auto-gain / auto-tuning:** legacy pages rewritten to firmware-exact
  behavior, ranges, defaults, and array sizes.
