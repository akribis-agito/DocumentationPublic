---
keyword: FIFOPosStatus
summary: Read-only array reporting the state of the FIFO position-tracking queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOPosStatus` is a read-only array that reports the internal state of the position-tracking subsystem: the interpolation control points in use, the cycle counters, the queue occupancy, and the motion/limits state. It is used to monitor the queue fed by [FIFOPosPush](FIFOPosPush.md) while position tracking is enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md). The array is read-only and is not saved to flash.

The array is indexed from 1.

## How it works

Each element reports one piece of the position-tracking state:

| Index | Reports | Notes |
|-------|---------|-------|
| 1 | Target at the start of the previous cycle | Control point used by cubic-spline interpolation. |
| 2 | Target at the start of the current cycle | Position the current cycle interpolates from. |
| 3 | Target at the end of the current cycle | Position the current cycle interpolates toward. |
| 4 | Target at the end of the next cycle | Look-ahead control point used by cubic-spline interpolation. |
| 5 | Cycles counter | Number of cycles completed since motion started. |
| 6 | In-cycle sample counter | Sample index within the current cycle, 0 up to the cycle length minus one (see [FIFOPosCycle](FIFOPosCycle.md)). |
| 7 | Free items in the queue | Number of empty slots. Equals the full queue depth when empty; 0 when full (further pushes are rejected). |
| 8 | Oldest entry index | Internal cyclic-buffer index of the next target to be consumed; -1 when the queue is empty. |
| 9 | Newest entry index | Internal cyclic-buffer index of the most recently pushed target; -1 when the queue is empty. |
| 10 | Motion / limits state | See the table below. |
| 11–12 | Reserved | |

The number of queued targets waiting to play is the queue depth minus the free count at index 7.

### Motion / limits state (index 10)

| Value | Meaning |
|-------|---------|
| 0 | No motion. |
| 1 | Normal motion (tracking). |
| 2 | Decelerating because the forward limit switch was reached. |
| 3 | Stopped and waiting at the forward limit switch (motion in the forward direction is blocked). |
| 4 | Decelerating because the reverse limit switch was reached. |
| 5 | Stopped and waiting at the reverse limit switch (motion in the reverse direction is blocked). |
| 6 | Decelerating to a stop because of a stop request. |
| 7 | Decelerating to a stop because of a controlled-stop request. |
| 8 | Reference clamped by the forward software position limit. |
| 9 | Reference clamped by the reverse software position limit. |

## Examples

```text
AFIFOPosStatus[7]   ; free slots in the queue (queue depth = empty)
AFIFOPosStatus[10]  ; motion / limits state
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosClear](FIFOPosClear.md) — clear the queue
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable queue streaming
- [FIFOPosCycle](FIFOPosCycle.md) — samples per target
- [MotionStat](../05-motion-status/MotionStat.md) — overall axis motion status
