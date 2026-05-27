---
keyword: MaxPosErr
summary: Maximum closed-loop position error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 84
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 80000000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPosErr

Maximum closed-loop position error; exceeding it disables the axis.

## Overview

`MaxPosErr` is the maximum allowable absolute position error ([PosErr](../../../../02-keywords/10-motion/01-kinematics-status/PosErr.md)) in closed-loop operation. If `|PosErr|` exceeds `MaxPosErr`, the axis is **instantaneously** disabled and an error is reported to the fault register `ConFlt`. It is the primary "following error" protection. For the open-loop (injection) equivalent, see [MaxPosErrOL](MaxPosErrOL.md).

## Examples

```text
AMaxPosErr=5000      ; max following error (user units)
```

## See also

- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit
- [MaxVelErr](MaxVelErr.md) — velocity-error limit
