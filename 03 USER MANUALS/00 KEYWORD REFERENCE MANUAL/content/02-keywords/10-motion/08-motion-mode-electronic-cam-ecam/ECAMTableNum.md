---
keyword: ECAMTableNum
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 311
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMTableNum

**Definition:**

ECAMTableNum is used to select the active cam pattern/look-up table in use. Each cam pattern will have its own unique set of parameters to full define the cam pattern.
