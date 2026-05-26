---
keyword: FIFOPosPosOf
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 662
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosPosOf

**Definition:**

FIFOPosPosOf sets a position offset added to every FIFO position segment before it is applied as the axis reference target. It allows a global shift of the entire FIFO trajectory without modifying the individual segment data. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[FIFOPosTrgt](FIFOPosTrgt.md), [FIFOPosVelOf](FIFOPosVelOf.md), [FIFOPosCurrOf](FIFOPosCurrOf.md)
