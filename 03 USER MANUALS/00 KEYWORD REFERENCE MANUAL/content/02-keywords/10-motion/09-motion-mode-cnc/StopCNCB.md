---
keyword: StopCNCB
summary: Command that stops execution of the CNC motion queue B.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 688
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
# StopCNCB

Command that stops execution of the CNC motion queue B.

## Overview

`StopCNCB` is a command function that stops the CNC motion engine driving queue B. The motion is brought to rest in a controlled way and no further queued segments are taken. Because it is a command, it can be issued at any time, including during motion.

`StopCNCB` is the second-engine counterpart of [StopCNCA](StopCNCA.md). It halts motion while leaving the queue intact, as opposed to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the segment queue.

## How it works

- `StopCNCB` does nothing if queue B is not in motion.
- When queue B is in motion, the engine is flagged to stop: the CNC motion status (element 10 of [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md)) sets its stop-in-progress bit (bit 12, mask `0x00001000`), and CNC step mode is cancelled so the stop always takes effect.
- Every axis that is a member of CNCB has its [MotionStat](../05-motion-status/MotionStat.md) **CNCB-stop bit (bit 15, mask `0x00008000`)** set, and its [MotionReason](../05-motion-status/MotionReason.md) set to **25** (motion ended due to `StopCNCB` / a CNCB member stopped).
- The motion engine then ends the move at the next opportunity to take a segment rather than continuing the path: the segments remaining in the queue are not played, but they are **not** removed — clear them with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) if you want to start fresh. To pause and later resume on the same path instead, use [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md).

## Examples

```text
AStopCNCB            ; stop CNC motion on queue B
```

## See also

- [StopCNCA](StopCNCA.md) — stop command for the first CNC engine
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments from the queue
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — pause/resume on the same path instead of stopping
- [MotionStat](../05-motion-status/MotionStat.md) — CNCB-stop bit (bit 15)
- [MotionReason](../05-motion-status/MotionReason.md) — set to 25 after `StopCNCB`
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — inspect queued segment data
