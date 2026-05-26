---
keyword: MaxVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 80
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
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVel

**Definition:**

MaxVel defines maximum allowable velocity while in closed loop condition, before an additional buffer of 25%. If the absolute value of Vel\[1\] exceeds (MaxVel \* 125%), the axis will be instantaneously disabled, and an error is thrown to ConFlt.
