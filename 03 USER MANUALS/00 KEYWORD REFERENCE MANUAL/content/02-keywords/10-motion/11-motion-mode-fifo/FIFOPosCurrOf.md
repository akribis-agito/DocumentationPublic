---
keyword: FIFOPosCurrOf
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 664
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosCurrOf

**Definition:**

FIFOPosCurrOf sets a current (torque) feedforward offset added to every FIFO position segment. It provides a constant bias current feedforward applied to all tracked segments. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosVelOf](FIFOPosVelOf.md), [FIFOPosTrgt](FIFOPosTrgt.md)
