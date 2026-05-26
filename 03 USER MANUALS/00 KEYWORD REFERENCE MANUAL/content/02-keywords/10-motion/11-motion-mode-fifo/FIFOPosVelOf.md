---
keyword: FIFOPosVelOf
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 663
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosVelOf

**Definition:**

FIFOPosVelOf sets a velocity feedforward offset added to every FIFO position segment. It biases the velocity feedforward of all tracked segments uniformly. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosCurrOf](FIFOPosCurrOf.md), [FIFOPosTrgt](FIFOPosTrgt.md)
