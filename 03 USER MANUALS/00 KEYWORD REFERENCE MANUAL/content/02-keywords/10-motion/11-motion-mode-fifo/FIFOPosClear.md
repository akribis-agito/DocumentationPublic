---
keyword: FIFOPosClear
summary: Command that clears all pending segments from the FIFO position queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOPosClear` empties the position-tracking queue, discarding every target that has been pushed but not yet consumed and resetting the free space to the full queue depth. It is the counterpart of [FIFOPosPush](FIFOPosPush.md), which fills the queue. It can be issued at any time, including during motion.

## How it works

Clearing resets the queue's internal bookkeeping so that all slots are free and there is no oldest or newest entry — the queue reports empty on the next read of [FIFOPosStatus](FIFOPosStatus.md). It only discards queued targets; it does not stop the axis. With the queue active ([FIFOPosFIFOEn](FIFOPosFIFOEn.md) set to `1`), clearing during motion leaves nothing to pop, so the axis holds its last working target until new targets are pushed or motion is stopped.

This is the command to flush a stale trajectory before streaming a new one, or to recover after a planned set of targets is no longer wanted.

## Examples

```text
AFIFOPosClear        ; discard all queued targets
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable queue streaming
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
