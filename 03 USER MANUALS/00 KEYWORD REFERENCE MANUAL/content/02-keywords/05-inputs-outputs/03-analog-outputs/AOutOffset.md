---
keyword: AOutOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 227
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -500
  - 500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutOffset

**Definition:**

AOutOffset defines the offset value (in millivolts) that is added to the scaled analog output. The array index corresponds to the index of the analog output. (i.e.: AOutOffset\[2\] refers to analog output 2).
