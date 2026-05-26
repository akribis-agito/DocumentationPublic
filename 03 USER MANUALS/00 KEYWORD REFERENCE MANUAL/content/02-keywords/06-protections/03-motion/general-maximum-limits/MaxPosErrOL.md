---
keyword: MaxPosErrOL
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# MaxPosErrOL

**Definition:**

MaxPosErrOL defines maximum allowable absolute position error ([PosErr](../../../../02-keywords/10-motion/01-kinematics-status/PosErr.md)) while in open loop condition during [injection](../../../../02-keywords/13-injection/00-overview.md). If the absolute value of PosErr exceeds MaxPosErrOL, the axis will be instantaneously disabled, and an error is thrown to ConFlt.
