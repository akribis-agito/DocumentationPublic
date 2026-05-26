---
keyword: PeakCL
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 52
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
  - 20
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PeakCL

**Definition:**

PeakCL is the peak current limit used in both current command and I2t limitations. If current limitation mode (CurrLimMode) is 0, the absolute value of current command will never exceed this value.
