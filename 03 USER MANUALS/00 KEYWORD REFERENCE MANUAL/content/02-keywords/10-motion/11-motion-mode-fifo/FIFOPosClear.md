---
keyword: FIFOPosClear
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 667
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosClear

**Definition:**

FIFOPosClear is a command that clears all pending segments from the FIFO position queue, resetting it to empty. It is an axis-related command function that can be issued at any time, including during motion.

**See also:**

[FIFOPosPush](FIFOPosPush.md), [FIFOPosFIFOEn](FIFOPosFIFOEn.md), [FIFOPosStatus](FIFOPosStatus.md)
