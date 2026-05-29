---
summary: Initialises the gantry map correction feature before gantry motion.
keyword: GantryMapInit
availability:
  standalone: []
  central-i:
  - v5
can_code: 752
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapInit

Position corresponding to the first entry of the gantry decoupling map.

## Overview

`GantryMapInit` sets the position (in the units of the source selected by [GantryMapSrc](GantryMapSrc.md)) at which the **first** entry of the [GantryMap](GantryMap.md) table applies. Together with the map gap it fixes where each table entry sits along the beam: entry 1 is at `GantryMapInit`, entry 2 one gap further on, and so on. It is a 64-bit axis-scoped value, saved to flash, settable with the motor on but not in motion. Default `0`. Available on central-i (v5).

Set `GantryMapInit` to the source position you want the start of the table to represent before building the map; together with the map gap it defines the position window the map covers.

## How it works

When the position-dependent map is active ([GantryMapType](GantryMapType.md) = 1), the controller converts the live source position into a table index by subtracting `GantryMapInit` and dividing by the map gap, then linearly interpolates between the two surrounding [GantryMap](GantryMap.md) entries (the live result is [GantryMapVal](GantryMapVal.md)). A source position equal to `GantryMapInit` lands on entry 1; positions below it clamp to entry 1 and positions beyond the last entry clamp to the last entry.

## Examples

```text
AGantryMapInit=0     ; first map entry corresponds to source position 0
AGantryMapInit       ; read the configured start position
```

### Edge cases

- **In motion at write** — rejected (`NOMOTN`). May be changed with the motor on.
- **Map type off** ([GantryMapType](GantryMapType.md) = 0) — stored but **not consulted**.
- **Position before init** — indexing falls below entry 1 and is clamped to entry 1; the controller does not extrapolate left of the start.
- **Position past last entry** — clamped to the last populated entry; consider increasing [GantryMap](GantryMap.md) entries or moving `GantryMapInit` if the working range exceeds the table.
- **Set on wrong axis** — read on the master axis only; writes elsewhere are stored but ignored.
- **Save** — flash-saveable; reloaded at boot.
- **Platform** — v5 central-i only.

## See also

- [GantryMap](GantryMap.md) — decoupling-ratio table whose first entry this positions
- [GantryMapSrc](GantryMapSrc.md) — source whose units this start position is expressed in
- [GantryMapType](GantryMapType.md) — enables use of the map
- [GantryMapVal](GantryMapVal.md) — live interpolated ratio
