---
keyword: StopCNCA
summary: Command that stops execution of the CNC motion queue A.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 456
attributes:
  access: ro
  scope: non-axis
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
# StopCNCA

Command that stops execution of the CNC motion queue A.

## Overview

`StopCNCA` is a command function that stops the CNC motion engine driving queue A. The motion is brought to rest in a controlled way and no further queued segments are taken. Because it is a command, it can be issued at any time, including during motion.

Use `StopCNCA` to halt motion while leaving the queue intact, as opposed to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the segment queue. The companion command for the second engine is [StopCNCB](StopCNCB.md).

## How it works

- `StopCNCA` does nothing if queue A is not in motion.
- When queue A is in motion, the engine is flagged to stop: the CNC motion status (element 10 of [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md)) sets its stop-in-progress bit (bit 12, mask `0x00001000`), and CNC step mode is cancelled so the stop always takes effect.
- Every axis that is a member of CNCA has its [MotionStat](../05-motion-status/MotionStat.md) **CNCA-stop bit (bit 12, mask `0x00001000`)** set, and its [MotionReason](../05-motion-status/MotionReason.md) set to **12** (motion ended due to `StopCNCA`).
- The motion engine then ends the move at the next opportunity to take a segment rather than continuing the path: the segments remaining in the queue are not played, but they are **not** removed — clear them with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) if you want to start fresh. To pause and later resume on the same path instead, use [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md).

## Examples

```text
AStopCNCA            ; stop CNC motion on queue A
```

## See also

- [StopCNCB](StopCNCB.md) — stop command for the second CNC engine
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments from the queue
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — pause/resume on the same path instead of stopping
- [MotionStat](../05-motion-status/MotionStat.md) — CNCA-stop bit (bit 12)
- [MotionReason](../05-motion-status/MotionReason.md) — set to 12 after `StopCNCA`
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — inspect queued segment data
