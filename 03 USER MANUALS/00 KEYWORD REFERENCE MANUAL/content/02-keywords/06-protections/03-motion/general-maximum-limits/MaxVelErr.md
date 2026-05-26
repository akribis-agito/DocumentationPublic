---
keyword: MaxVelErr
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# MaxVelErr

**Definition:**

MaxVelErr defines maximum allowable absolute velocity error ([VelErr](../../../../02-keywords/10-motion/01-kinematics-status/VelErr.md)) while in closed loop condition. If the absolute value of VelErr exceeds MaxVelErr, the axis will be instantaneously disabled, and an error is thrown to ConFlt.
