---
keyword: FIFOPosCycle
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 660
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1600
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosCycle

**Definition:**

FIFOPosCycle sets the cycle time (in servo samples) for FIFO position tracking. It defines the time interval between consecutive position segments popped from the FIFO and applied as the axis reference. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[FIFOPosType](FIFOPosType.md), [FIFOPosPush](FIFOPosPush.md), [FIFOPosFIFOEn](FIFOPosFIFOEn.md)
