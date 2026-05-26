---
keyword: CurrCmdCntr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 334
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdCntr

**Definition:**

CurrCmdCntr is the time elapsed, in milliseconds,

1.  (if CurrCmdSrc = 0 or 3) under current operation mode.

2.  (if CurrCmdSrc = 1 or 2) under the existing CurrCmdVal array entry. This value will reset to 0 upon switching to the next CurrCmdVal entry.

CurrCmdCntr will reset to 0

1.  upon receipt of GoToCurrMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to current operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value beforehand and begin the timer from such value.

**Note:**

User can overwrite CurrCmdCntr at any time under current operation mode.
