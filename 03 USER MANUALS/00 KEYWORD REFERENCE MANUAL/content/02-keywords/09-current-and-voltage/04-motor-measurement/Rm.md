---
keyword: Rm
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 373
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
  - 1
  - 100000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# Rm

**Definition:**

Rm records the resistance measurement in terms of milliohm. PCSuite will update this value after measurement.
