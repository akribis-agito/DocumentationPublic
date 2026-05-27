---
keyword: AccShapeFact
summary: Array of per-segment acceleration scaling factors for the acceleration-shaping profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 164
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeFact

Array of per-segment acceleration scaling factors for the acceleration-shaping profile.

## Overview

`AccShapeFact` is an array (10 usable entries, indices 1–10) that defines the acceleration scaling factor for each segment of the acceleration-shaping profile. Each element specifies the fraction of the maximum acceleration applied during the corresponding segment whose distance-to-target band is set by [AccShapeDist](AccShapeDist.md). The shaping is only applied when [AccShapeOn](AccShapeOn.md) is enabled. It is an axis-related array saved to flash and can be changed at any time.

## How it works

When the remaining distance to target falls within a band defined by [AccShapeDist](AccShapeDist.md), the matching `AccShapeFact` entry is read as a **fixed-point fraction scaled by 65536** and multiplied into the acceleration and deceleration limits for that cycle:

```text
factor      = AccShapeFact[n] / 65536
AccelFinal  = Accel × AccelFact × factor
DecelFinal  = Decel × AccelFact × factor
```

| AccShapeFact value | Resulting factor |
|---|---|
| 65536 | ×1.0 (full acceleration) |
| 49152 | ×0.75 |
| 32768 | ×0.5 |
| 16384 | ×0.25 |
| 0 | ×0 (no acceleration in this band) |

The factors are paired with their distances and re-sorted into ascending distance order whenever the table is written, so the value in `AccShapeFact[n]` always travels with `AccShapeDist[n]`. The array size is 11 to allow 1-based command indexing; only indices 1–10 are used. See [AccShapeOn](AccShapeOn.md) for the full mechanism.

## Examples

```text
AAccShapeFact[1]=32768   ; first (nearest-target) band runs at half acceleration
AAccShapeFact[2]=65536   ; second band at full acceleration
AAccShapeFact[1]        ; query first segment factor
```

## See also

- [AccShapeOn](AccShapeOn.md) — enables acceleration shaping
- [AccShapeDist](AccShapeDist.md) — per-segment distances
