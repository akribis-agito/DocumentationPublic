---
keyword: FIFOPosClear
summary: Command that clears all pending segments from the FIFO position queue.
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

Command that clears all pending segments from the FIFO position queue.

## Overview

`FIFOPosClear` clears all pending segments from the FIFO position queue, resetting it to empty. It can be issued at any time, including during motion. It is the position-tracking counterpart of [FIFOPosPush](FIFOPosPush.md), which fills the queue.

## Examples

```text
AFIFOPosClear=0      ; empty the FIFO position queue
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push a position segment
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
