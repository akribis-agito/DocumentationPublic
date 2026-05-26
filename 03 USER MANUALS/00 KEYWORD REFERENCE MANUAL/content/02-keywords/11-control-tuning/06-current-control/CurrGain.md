---
keyword: CurrGain
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 104
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 200000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrGain

**Definition:**

CurrGain is the proportional gain of current loop control, acting on the summation of current error and result of current error integral control.
