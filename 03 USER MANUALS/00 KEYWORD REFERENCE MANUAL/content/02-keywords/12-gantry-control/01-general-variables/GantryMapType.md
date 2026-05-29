---
summary: Selects the type of gantry map correction applied to the yaw axis.
keyword: GantryMapType
availability:
  standalone: []
  central-i:
  - v5
can_code: 749
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapType

Enables the position-dependent gantry decoupling map.

## Overview

`GantryMapType` selects how the controller splits the gantry between its two motors. With the default value `0` the gantry uses a fixed, symmetric split (each motor sits at the mid-point of the linear and yaw commands). With value `1` the controller instead uses a **position-dependent decoupling map**: a table of ratios, looked up by the position from [GantryMapSrc](GantryMapSrc.md), that shifts the effective mid-point of the gantry along the beam. This compensates for an asymmetric mechanism — for example a beam whose stiffness or geometry is not symmetric about its centre — so the linear and yaw axes stay decoupled across the full travel.

| `GantryMapType` | Mode | Effect |
|:---------------:|------|--------|
| 0 | Off (symmetric) | Fixed 50/50 split: linear feedback is the mean of the two motors; yaw current is shared equally. |
| 1 | Mapped (central-i v5) | Decoupling ratio from the map table is applied to both the feedback combination and the motor current split. |

It is axis-scoped, saved to flash, and can be changed with the motor on but not while in motion. The position used to index the map is chosen by [GantryMapSrc](GantryMapSrc.md), the active interpolated ratio is reported by [GantryMapVal](GantryMapVal.md), and the table of ratios is held in [GantryMap](GantryMap.md). Value `1` is available only on central-i (v5); the standalone product supports only `0`.

## How it works

When `GantryMapType` = 0 the gantry common-mode position is simply the mean of the two motor positions, and the yaw-correction current is added to one motor and subtracted from the other in equal measure. When `GantryMapType` = 1 the controller looks up a ratio *r* (between 0 and 1) from the [GantryMap](GantryMap.md) table at the current source position (reported live as [GantryMapVal](GantryMapVal.md)) and uses it both to weight how the two motor positions combine into the linear feedback and to weight how the linear and yaw current commands are distributed to the two motors. A ratio of 0.5 reproduces the symmetric behaviour; values away from 0.5 move the controlled mid-point toward one side of the beam. See [GantryMap](GantryMap.md) for the table geometry and [GantryMapSrc](GantryMapSrc.md) for the lookup index.

## Examples

```text
AGantryMapType=1     ; enable the position-dependent decoupling map (central-i v5)
AGantryMapType=0     ; use the fixed symmetric split
AGantryMapType       ; read the active map mode
```

### Edge cases

- **In motion at write** — rejected (`NOMOTN`); may be changed with the motor on.
- **`GantryMapType = 1` without a configured table** — the map reads zeros and the gantry shifts hard to one side; configure [GantryMap](GantryMap.md), [GantryMapSrc](GantryMapSrc.md), [GantryMapInit](GantryMapInit.md) and the map gap before enabling.
- **Map type changed during gantry-on** — the change takes effect on the next cycle without a smooth ramp; commanding a step in the linear-yaw split can momentarily disturb the beam. Prefer changing the type with [GantryOn](GantryOn.md) = 0.
- **Out of range** — values outside the platform's supported range are rejected (v5 central-i: 0–1; v4 / standalone: 0 only).
- **Set on wrong axis** — read on the master axis only; writes elsewhere are stored but ignored.
- **Save** — flash-saveable.
- **Platform** — `GantryMapType = 1` is v5 central-i only.

## See also

- [GantryMap](GantryMap.md) — table of decoupling ratios
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the map
- [GantryMapVal](GantryMapVal.md) — live interpolated ratio read from the map
- [GantryMapInit](GantryMapInit.md) — position at the first map entry
