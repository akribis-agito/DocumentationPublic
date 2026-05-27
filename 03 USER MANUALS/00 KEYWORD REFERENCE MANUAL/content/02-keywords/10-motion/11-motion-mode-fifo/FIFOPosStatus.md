---
keyword: FIFOPosStatus
summary: Read-only array reporting the state of the FIFO position-tracking queue.
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

Read-only array reporting the state of the FIFO position-tracking queue.

## Overview

`FIFOPosStatus` is a read-only array that reports the current state of the FIFO position-tracking queue, such as the number of segments remaining, whether the queue is empty or full, and any error conditions. It is used to monitor the queue fed by [FIFOPosPush](FIFOPosPush.md) while position tracking is enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md). It is not saved to flash.

> **Documentation pending:** The meaning of each individual element of the `FIFOPosStatus` array was not available in the source reference. Verify element assignments against current firmware before relying on specific indices.

## Examples

```text
FIFOPosStatus[1]?   ; query the first status element
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push a position segment
- [FIFOPosClear](FIFOPosClear.md) — clear the queue
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
