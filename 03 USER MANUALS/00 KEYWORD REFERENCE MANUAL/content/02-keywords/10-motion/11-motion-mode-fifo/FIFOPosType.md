---
keyword: FIFOPosType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 659
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
# FIFOPosType

**Definition:**

FIFOPosType selects the operating mode of the FIFO position tracking feature. Different values select the source and interpretation of the position segments pushed into the FIFO (for example, absolute or incremental, with or without velocity feedforward). It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[FIFOPosPush](FIFOPosPush.md), [FIFOPosFIFOEn](FIFOPosFIFOEn.md), [FIFOPosStatus](FIFOPosStatus.md)
