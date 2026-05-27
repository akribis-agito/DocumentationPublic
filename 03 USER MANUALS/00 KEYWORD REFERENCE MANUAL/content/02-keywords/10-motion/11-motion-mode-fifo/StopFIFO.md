---
keyword: StopFIFO
summary: Command that makes the currently executing FIFO segment the last one, ending the sequence.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 291
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
# StopFIFO

Command that makes the currently executing FIFO segment the last one, ending the sequence.

## Overview

`StopFIFO` stops a FIFO motion by making the segment currently being played the last segment of the sequence. Unlike the general [Stop](../04-motion-command/Stop.md) command, which decelerates the axis to zero speed, `StopFIFO` lets the active segment finish at its programmed velocity and then ends the motion, so the trajectory completes gracefully and any segments still queued behind it are discarded.

`StopFIFO` only acts when the axis is currently running a FIFO motion; otherwise it has no effect.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

When accepted, `StopFIFO`:

- Sets the FIFO-stop bit in [MotionStat](../05-motion-status/MotionStat.md) — **bit 8** (mask `0x00000100`) — so the controller and host tools show that the FIFO motion is ending.
- Records the stop reason in [MotionReason](../05-motion-status/MotionReason.md): the value becomes **10** (motion ended due to a StopFIFO command).
- Forces the queue so that the segment in progress becomes the last one: the controller plays it to the end and then ends the motion, exactly as it would on an underrun. Entries queued after it are not played.

Because the active segment runs to completion at its current velocity, the axis is not decelerated to zero by this command. If you need the axis to come to rest, follow `StopFIFO` with a move that brings velocity to zero, or use [Stop](../04-motion-command/Stop.md) instead.

## Examples

```text
AStopFIFO=0          ; let the current segment finish, then end the FIFO motion
```

## See also

- [Stop](../04-motion-command/Stop.md) — decelerate the axis to zero speed
- [MotionStat](../05-motion-status/MotionStat.md) — FIFO-stop bit (bit 8)
- [MotionReason](../05-motion-status/MotionReason.md) — stop reason (= 10 after StopFIFO)
- [FIFOType](FIFOType.md) — full FIFO mode description
- [FIFOStatus](FIFOStatus.md) — queue status
