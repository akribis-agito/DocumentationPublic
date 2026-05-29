---
summary: Correction value read from the gantry map table at the current indexed position.
keyword: GantryMapVal
availability:
  standalone: []
  central-i:
  - v5
can_code: 750
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1.0
  default: 0.5
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapVal

Live decoupling ratio interpolated from the gantry map at the current position.

## Overview

`GantryMapVal` is the read-only decoupling ratio the controller is applying right now, interpolated from the [GantryMap](GantryMap.md) table at the position taken from [GantryMapSrc](GantryMapSrc.md). It is a ratio in the range **0.0 to 1.0** (it reads **0.5** — the symmetric split — until the map is built). It is reported on the master axis and is not saved to flash. It is meaningful only when the position-dependent map is enabled ([GantryMapType](GantryMapType.md) = 1). Available on central-i (v5).

`GantryMapVal` is the diagnostic that lets you confirm the map is being indexed and interpolated as intended: as the gantry moves, this value should sweep smoothly through the ratios you stored in [GantryMap](GantryMap.md).

## How it works

Each control cycle, when the map is active, the controller reads the source position from [GantryMapSrc](GantryMapSrc.md), finds the surrounding entries in [GantryMap](GantryMap.md) (spaced from [GantryMapInit](GantryMapInit.md) by the map gap) and linearly interpolates between them; the result is `GantryMapVal`. The controller then uses this ratio to weight both the gantry feedback combination and the split of motor currents (see [GantryMapType](GantryMapType.md)). Outside the mapped range it clamps to the first or last table entry.

## Examples

```text
AGantryMapVal        ; read the live decoupling ratio at the current position
```

### Edge cases

- **Map type off** ([GantryMapType](GantryMapType.md) = 0) — `GantryMapVal` is not updated by the lookup; it holds whatever value the table interpolation last produced (typically `0.5`).
- **Source not configured** ([GantryMapSrc](GantryMapSrc.md) = 0) — the lookup reads from a zero pointer and produces the first table entry; treat the readout with caution.
- **Outside the table** — values past the last entry clamp to the last entry; below the first entry clamp to the first entry. The diagnostic will plateau when the gantry leaves the mapped range.
- **Read-only** — writes are rejected.
- **Non-master axis** — reading on an axis that is not a gantry master returns the master's most recent value or `0` if no master is configured.
- **Platform** — v5 central-i only.

## See also

- [GantryMap](GantryMap.md) — table this value is interpolated from
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the table
- [GantryMapType](GantryMapType.md) — enables use of the map
- [GantryMapInit](GantryMapInit.md) — position corresponding to the first table entry
