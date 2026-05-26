---
keyword: FIFOPosFIFOEn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 665
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosFIFOEn

**Definition:**

FIFOPosFIFOEn enables or disables the FIFO position tracking mode. When set to a non-zero value, the controller reads position segments from the FIFO queue and uses them as the axis reference trajectory. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[FIFOPosType](FIFOPosType.md), [FIFOPosPush](FIFOPosPush.md), [FIFOPosCycle](FIFOPosCycle.md)
