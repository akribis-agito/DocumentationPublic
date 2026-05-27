---
keyword: AccShapeDist
summary: Array of per-segment distances defining the acceleration-shaping profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 163
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeDist

Array of per-segment distances defining the acceleration-shaping profile.

## Overview

`AccShapeDist` is an array (size 11) that defines the positional distance of each segment in the acceleration-shaping profile. Together with [AccShapeFact](AccShapeFact.md) it specifies how the acceleration magnitude is distributed over the move to reduce mechanical vibration. The shaping is only applied when [AccShapeOn](AccShapeOn.md) is enabled. It is an axis-related array saved to flash and can be changed at any time.

## Examples

```text
AccShapeDist[1]=5000    ; distance of first shaping segment (user units)
AccShapeDist[2]=8000    ; distance of second shaping segment
AccShapeDist[1]?        ; query first segment distance
```

## See also

- [AccShapeOn](AccShapeOn.md) — enables acceleration shaping
- [AccShapeFact](AccShapeFact.md) — per-segment acceleration scaling factors
