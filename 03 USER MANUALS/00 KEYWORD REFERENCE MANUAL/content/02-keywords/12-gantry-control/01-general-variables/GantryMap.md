---
summary: Active error-map correction value applied to the gantry yaw axis.
keyword: GantryMap
availability:
  standalone: []
  central-i:
  - v5
can_code: 748
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 1025
  data_type: float64
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMap

Table of position-dependent decoupling ratios for the gantry.

## Overview

`GantryMap` holds the table of decoupling ratios used when the position-dependent gantry map is enabled ([GantryMapType](GantryMapType.md) = 1). Each entry is a ratio in the range **0.0 to 1.0** (default **0.5**), describing how the gantry is split between its two motors at a given position along the beam. A value of 0.5 is the symmetric split; values away from 0.5 move the controlled mid-point toward one side, so a non-uniform mechanism can be linearised across its travel. It is a flash-saved array on the master axis.

The table is **indexed from 1** and provides up to **1024 usable entries**. The position that selects an entry comes from the source chosen by [GantryMapSrc](GantryMapSrc.md); the first entry corresponds to position [GantryMapInit](GantryMapInit.md), and successive entries are spaced one map gap apart (the gap is set by the related `GantryMapGap` keyword). The controller interpolates linearly between entries and reports the live result as [GantryMapVal](GantryMapVal.md). Available on central-i (v5).

## How it works

When the map is active, each control cycle the controller takes the current position from [GantryMapSrc](GantryMapSrc.md), converts it to a fractional table index relative to [GantryMapInit](GantryMapInit.md) and the map gap, and linearly interpolates between the two surrounding `GantryMap` entries to obtain the active ratio. Positions before the first entry clamp to entry 1; positions past the last usable entry clamp to the last entry. The interpolated ratio is then applied two ways:

- **Feedback combination** — it weights how the two motor-encoder positions combine into the gantry linear feedback (instead of a plain 50/50 mean).
- **Current split** — it weights how the combined linear and yaw current commands are distributed to the two motors.

This keeps the linear and yaw axes decoupled even where the mechanism is not symmetric. Build the table so that each entry holds the correct local split for the beam position it represents; the special value 0.5 everywhere reproduces the fixed symmetric gantry.

## Examples

```text
AGantryMap[1]        ; read the first decoupling ratio in the table
AGantryMap[1]=0.5    ; set the first entry to the symmetric split
AGantryMapVal        ; read the live interpolated ratio at the current position
```

### Edge cases

- **Index 0** — invalid; valid indices are `GantryMap[1]`–`GantryMap[1024]`. `GantryMap[0]` does not exist.
- **In motion at write** — rejected (`NOMOTN`). The map may be edited with the motor on but not during a move.
- **Map type off** ([GantryMapType](GantryMapType.md) = 0) — the table is stored but **not consulted**; the gantry uses the symmetric 50/50 split.
- **Outside the table range** — positions before [GantryMapInit](GantryMapInit.md) clamp to entry 1; positions past entry 1024 clamp to the last populated entry.
- **Out-of-range values** — entries outside `[0.0, 1.0]` are accepted by the parameter table but produce unphysical splits; treat 0.5 as the symmetric default.
- **Set on wrong axis** — the engine reads `GantryMap` on the **master** axis. Writes elsewhere are accepted but never consulted.
- **Save** — flash-saveable; large table that persists across reboots.
- **Platform** — v5 central-i only.

## See also

- [GantryMapType](GantryMapType.md) — enables use of this table
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the table
- [GantryMapInit](GantryMapInit.md) — position corresponding to the first table entry
- [GantryMapVal](GantryMapVal.md) — live interpolated ratio read from the table
