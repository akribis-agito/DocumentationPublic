---
keyword: SetPosition
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 154
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# SetPosition

**Definition:**

SetPosition is a command that immediately sets the axis position reference and feedback registers to the specified value without moving the motor. It is used to define a new coordinate origin or to recover from a position discrepancy. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[ZeroPosErr](ZeroPosErr.md)
