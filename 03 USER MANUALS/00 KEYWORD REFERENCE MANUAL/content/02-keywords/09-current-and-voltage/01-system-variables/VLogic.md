---
keyword: VLogic
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 37
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VLogic

**Definition:**

VLogic reports the 5V logic voltage measurement in millivolts, and has internal protection. Motor is disabled if VLogic is not in the range of \[4500, 5500\] mV.
