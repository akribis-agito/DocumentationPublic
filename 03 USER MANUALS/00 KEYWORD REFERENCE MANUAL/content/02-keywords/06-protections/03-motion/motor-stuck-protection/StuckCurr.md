---
keyword: StuckCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 86
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
  - 64000
  default: 4000
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckCurr

**Definition:**

StuckCurr defines the current threshold used for motor stuck detection.
