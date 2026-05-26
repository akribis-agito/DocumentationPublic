---
keyword: FIFOPosStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 668
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 13
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
# FIFOPosStatus

**Definition:**

FIFOPosStatus is a read-only array that reports the current state of the FIFO position tracking queue. The elements indicate the number of segments remaining in the queue, whether the queue is empty or full, and any error conditions. It is an axis-related, read-only array that is not saved to flash.

**See also:**

[FIFOPosPush](FIFOPosPush.md), [FIFOPosClear](FIFOPosClear.md), [FIFOPosFIFOEn](FIFOPosFIFOEn.md)
