---
keyword: MaxPosErrOL
summary: Maximum open-loop (injection) position error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 388
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
  - 1500000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MaxPosErrOL

Maximum open-loop (injection) position error; exceeding it disables the axis.

## Overview

`MaxPosErrOL` is the maximum allowable absolute position error ([PosErr](../../../../02-keywords/10-motion/01-kinematics-status/PosErr.md)) while in **open-loop** operation during [injection](../../../../02-keywords/13-injection/00-overview.md). If `|PosErr|` exceeds `MaxPosErrOL`, the axis is instantaneously disabled and an error is reported to `ConFlt`. It is the open-loop counterpart of [MaxPosErr](MaxPosErr.md) (open-loop error is naturally larger, hence a separate, larger limit).

## Examples

```text
AMaxPosErrOL=1000000 ; max open-loop position error (user units)
```

## See also

- [MaxPosErr](MaxPosErr.md) — closed-loop position-error limit
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit
