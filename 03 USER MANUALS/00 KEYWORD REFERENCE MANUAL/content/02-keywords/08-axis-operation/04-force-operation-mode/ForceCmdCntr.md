---
keyword: ForceCmdCntr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 574
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
# ForceCmdCntr

**Definition:**

ForceCmdCntr is the time elapsed, in milliseconds,

1.  (if ForceCmdSrc = 0) under force operation mode.

2.  (if ForceCmdSrc = 1 or 2) under the existing ForceCmdVal array entry. This value will reset to 0 upon switching to the next ForceCmdVal entry.

ForceCmdCntr will reset to 0 only

1.  upon receipt of GoToForceMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to force operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value beforehand and begin the timer from such value.

**Note:**

User can overwrite ForceCmdCntr at any time under force operation mode.
