---
keyword: InTargetTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 266
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetTime

**Definition:**

InTargetTime is the minimum time that the absolute value of PosErr or Vel\[1\] needs to be within InTargetTol or InTargetVelTh window, before InTargetStat signals that target is reached (InTargetStat=4).
