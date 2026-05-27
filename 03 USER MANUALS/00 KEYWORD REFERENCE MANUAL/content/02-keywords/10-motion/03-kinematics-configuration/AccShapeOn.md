---
keyword: AccShapeOn
summary: Enables acceleration shaping to reduce vibration via a shaped acceleration curve.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 162
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeOn

Enables acceleration shaping to reduce vibration via a shaped acceleration curve.

## Overview

`AccShapeOn` enables the acceleration-shaping feature, which modifies the acceleration profile to reduce mechanical vibration by applying a shaped (filtered) acceleration curve. When set to `1`, the [AccShapeDist](AccShapeDist.md) and [AccShapeFact](AccShapeFact.md) arrays define the shaping profile applied on top of the base [Accel](Accel.md) ramp. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
AAccShapeOn=1        ; enable acceleration shaping
AAccShapeOn=0        ; disable acceleration shaping
AAccShapeOn         ; query state
```

## See also

- [AccShapeDist](AccShapeDist.md) — per-segment shaping distances
- [AccShapeFact](AccShapeFact.md) — per-segment shaping factors
- [Accel](Accel.md) — base acceleration that shaping modifies
