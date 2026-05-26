---
keyword: PDSubType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 421
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDSubType

**Definition:**

PDSubType selects the sub-type of pulse-and-direction input mode, choosing between different input signal formats (for example, step/direction vs. CW/CCW pulse inputs). It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[PDFact](PDFact.md), [PDFactDen](PDFactDen.md), [SetPDPos](SetPDPos.md)
