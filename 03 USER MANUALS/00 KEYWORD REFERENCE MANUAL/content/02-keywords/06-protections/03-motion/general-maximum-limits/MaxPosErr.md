---
keyword: MaxPosErr
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

MaxPosErr defines maximum allowable absolute position error ([PosErr](../../../../02-keywords/10-motion/01-kinematics-status/PosErr.md)) while in closed loop condition. If the absolute value of PosErr exceeds MaxPosErr, the axis will be instantaneously disabled, and an error is thrown to ConFlt.
