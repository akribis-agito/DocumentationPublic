---
keyword: GoToCurrMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 335
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GoToCurrMode

**Definition:**

GoToCurrMode command instructs the controller to enter current operation mode in a graceful manner. The preparations include halting motion, clearing counters, variable initialisation, etc.
