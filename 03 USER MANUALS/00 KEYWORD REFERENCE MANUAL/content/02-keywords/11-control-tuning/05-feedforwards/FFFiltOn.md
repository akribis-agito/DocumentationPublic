---
keyword: FFFiltOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 728
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FFFiltOn

**Definition:**

FFFiltOn is used to turn on/off the feedforward filters. If FFFiltOn\[1\] = 1, the filter is enabled. If FFFiltOn\[1\] = 0, the filter is disabled (bypassed).
