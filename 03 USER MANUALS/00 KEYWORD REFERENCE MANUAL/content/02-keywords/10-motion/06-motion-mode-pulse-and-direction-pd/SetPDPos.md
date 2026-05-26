---
keyword: SetPDPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 156
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
# SetPDPos

**Definition:**

SetPDPos is a command that resets the pulse-and-direction input position counter to a specified value. It allows the PD position reference to be re-zeroed or preset without physically moving the axis. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[PDSubType](PDSubType.md), [PDFact](PDFact.md), [SetPosition](../03-kinematics-configuration/SetPosition.md)
