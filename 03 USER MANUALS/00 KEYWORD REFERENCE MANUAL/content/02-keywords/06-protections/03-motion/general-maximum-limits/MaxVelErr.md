---
keyword: MaxVelErr
summary: Maximum closed-loop velocity error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 85
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
  - 1300000000
  default: 32768
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MaxVelErr

Maximum closed-loop velocity error; exceeding it disables the axis.

## Overview

`MaxVelErr` is the maximum allowable absolute velocity error ([VelErr](../../../../02-keywords/10-motion/01-kinematics-status/VelErr.md)) in closed-loop operation. If `|VelErr|` exceeds `MaxVelErr`, the axis is instantaneously disabled and an error is reported to `ConFlt`. For the open-loop (injection) equivalent, see [MaxVelErrOL](MaxVelErrOL.md).

## Examples

```text
AMaxVelErr=100000    ; max velocity error (user units)
```

## See also

- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit
- [MaxPosErr](MaxPosErr.md) — position-error limit
