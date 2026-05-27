---
keyword: MaxVelErrOL
summary: Maximum open-loop (injection) velocity error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 389
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
  default: 20000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# MaxVelErrOL

Maximum open-loop (injection) velocity error; exceeding it disables the axis.

## Overview

`MaxVelErrOL` is the maximum allowable absolute velocity error ([VelErr](../../../../02-keywords/10-motion/01-kinematics-status/VelErr.md)) while in **open-loop** operation during [injection](../../../../02-keywords/13-injection/00-overview.md). If `|VelErr|` exceeds `MaxVelErrOL`, the axis is instantaneously disabled and an error is reported to `ConFlt`. It is the open-loop counterpart of [MaxVelErr](MaxVelErr.md).

## Examples

```text
AMaxVelErrOL=20000000 ; max open-loop velocity error (user units)
```

## See also

- [MaxVelErr](MaxVelErr.md) — closed-loop velocity-error limit
- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit
