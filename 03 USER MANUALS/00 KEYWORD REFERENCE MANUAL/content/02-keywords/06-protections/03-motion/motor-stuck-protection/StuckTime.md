---
keyword: StuckTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 88
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
  - 2147483647
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckTime

**Definition:**

StuckTime defines the duration used for motor stuck detection.
