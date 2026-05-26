---
keyword: dPosRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 155
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# dPosRef

**Definition:**

dPosRef is the velocity reference, calculated as the filtered derivative of position reference (PosRef). The filter used is of first-order low-pass and is defined by dPosRefFilt.
