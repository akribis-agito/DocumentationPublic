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

## 2026.11 — 2026-11-01

The firmware 5.3.0 additions since 2026.09, with every page checked against
firmware 5.3.0-rc7 and corrected where it disagreed.

### Added

- **Push events** (`PushEv*`) on AGM800 and AGM800-EC, with each product's tick.
- **AGM800-EC:** product type 16 in `Identity`, six-axis motion, and the
  keyword conversions at its 16 kHz control rate.
- **Friction feedforward for 5.3.0:** `FricMethod` and its parameter pages, in
  the 5.3.0 numbering (0 off, 1 Stribeck, 2 linear, 3 hysteresis, 4 play,
  5 LuGre), with a note for values saved on 5.3.0-rc4 or rc5.
- **Lock capture:** coordinates across `SetPosition` and `ZeroPosErr`, the
  before-map capture tables, FIFO capture and its loss accounting.
- **Event generation:** the hardware-table preload (`EventLoad`,
  `EventType = 3`), finite and endless by-gap runs, pulse-width quantization.
- **Encoders:** the virtual encoder, Central-i status against feedback
  validity, absolute-feedback startup and the AGM800 Tamagawa startup rule.
- Smaller pages: `CIStatus` codes 15 and 16, `Map*` writes with the motor on
  at standstill, `UPMCalcCoeff` with the motor on, `DOutMode`, homing with
  tracking, AGD101 `MaxPWM`, `DOUBLE` math precision, `CalcIden` indices,
  logger upload, the AGM800 Ethernet port policy, the P/D count direction.

### Fixed — checked against firmware 5.3.0-rc7

- **Friction numbering:** the pages used the earlier numbering, so the
  documented replacement for `StribOn` selected LuGre.
- **`Identity[62]`:** no bit advertises the friction numbering; the page no
  longer tells hosts to refuse firmware without one.
- **Lock capture:** the AGM800 re-arm behaviour, the `LockFifoKeep = 1` case in
  `LockLost`, and the `EventType = 3` exception on `SetPosition`.
- **Event generation:** later table-point widths keep only their low 13 bits
  instead of clamping; the 1024-row legacy limit, which no released firmware
  has, is gone; preload width range, Ready and fault reporting corrected; the
  overlap fault applies from FPGA 5.5.0.
- **Encoders and AGM800-EC:** absolute-encoder startup, the missing friction
  rows in the AGM800-EC conversion table, and the Ethernet port policy, which
  ships in firmware 5.3.0.
- **Scope:** push events and the event-table preload exist on AGM800-EC as
  well as AGM800; `ForceInTStat` names EtherCAT object 0x2001.

## 2026.06 — 2026-06-02

First versioned release: a baseline of the corpus (926 pages) plus the
versioning machinery itself.

### Added

- **Documentation versioning.** Per-page `last_updated` (git last-commit date)
  and `doc_revision` (corpus CalVer) frontmatter stamps, a corpus `VERSION`
  file, and a machine-readable `manifest.json` (path, keyword, last_updated,
  doc_revision, body SHA-256) for incremental re-indexing. Stamps are derived
  automatically from git via `keyword-docgen version`.
- **58 previously-undocumented legacy keyword pages** (the `AutoG*`, `Spring*`,
  `UPM*`, `MotorLearn*`, `BurnIn*`, `Indirect*` and related families) gained
  generated firmware frontmatter.
- **New v5 data-capture documentation.** Documented the Central-i signal scope
  (`ScopeOn`, `ScopeGap`, `ScopeParams`, `ScopeStatus`, `ScopeAbout`,
  `ScopeUpload`) and the user-program `Print` statement, and reframed the
  **Data recording** overview to group its three capture mechanisms — the
  triggered recorder (`Rec*`), the continuous logger (`Logger*`), and the
  Central-i scope (`Scope*`).

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
