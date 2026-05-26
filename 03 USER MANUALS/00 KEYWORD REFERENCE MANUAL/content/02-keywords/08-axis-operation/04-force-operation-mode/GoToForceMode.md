---
keyword: GoToForceMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 575
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
# GoToForceMode

**Definition:**

GoToForceMode command instructs the controller to enter force operation mode a graceful manner. The preparations include halting motion, clearing counters, variable initialisation, etc.

**Note:**

GoToForceMode cannot be used if axis is in current operation mode (OperationMode = 0).
