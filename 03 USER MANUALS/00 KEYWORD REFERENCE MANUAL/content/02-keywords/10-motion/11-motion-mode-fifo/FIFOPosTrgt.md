---
keyword: FIFOPosTrgt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 661
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
# FIFOPosTrgt

**Definition:**

FIFOPosTrgt reports the current target position being tracked from the FIFO position queue. It reflects the position segment currently being followed by the axis. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[FIFOPosPush](FIFOPosPush.md), [FIFOPosStatus](FIFOPosStatus.md), [FIFOPosPosOf](FIFOPosPosOf.md)
