---
keyword: PosBeforeMap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 160
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: false
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Read-only feedback position before error-mapping correction.
---
# PosBeforeMap

Read-only feedback position before error-mapping correction.

## Overview

`PosBeforeMap` reports the axis position from the encoder, in user units, **before** any error-mapping correction has been applied. The corrected value is reported by [Pos](../10-motion/01-kinematics-status/Pos.md); the difference between the two is the correction contributed by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) arrays when mapping is enabled with [MapType](MapType.md). Comparing `PosBeforeMap` with `Pos` is useful for diagnostics and for verifying the map correction being added to the feedback.

It is a read-only, axis-scoped status variable that is not saved to flash.

## Examples

```text
APosBeforeMap       ; read the uncorrected feedback position
```

## See also

- [Pos](../10-motion/01-kinematics-status/Pos.md) — feedback position after correction; difference equals the map correction
- [MapType](MapType.md) — enables the correction that creates the difference
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values applied to the feedback
