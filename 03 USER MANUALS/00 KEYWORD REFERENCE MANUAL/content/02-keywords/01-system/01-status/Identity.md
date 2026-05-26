---
keyword: Identity
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 1
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 63
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Identity

**Definition:**

Identity is an array that includes information about the controller. It is used internally by PCSuite GUI to identify the features implemented by the controller and to adjust the GUI accordingly.
