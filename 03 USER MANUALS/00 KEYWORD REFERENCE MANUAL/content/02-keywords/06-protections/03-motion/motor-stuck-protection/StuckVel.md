---
keyword: StuckVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 87
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
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckVel

**Definition:**

StuckVel defines the velocity threshold used for motor stuck detection. If velocity is less than StuckVel while current exceeds StuckCurr for StuckTime, the axis is considered stuck.
