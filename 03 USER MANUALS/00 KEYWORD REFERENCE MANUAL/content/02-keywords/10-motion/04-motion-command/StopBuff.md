---
keyword: StopBuff
summary: Stops spline-buffer (Buff) motion, halting playback and decelerating to rest.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 550
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
# StopBuff

Stops spline-buffer (Buff) motion at the end of the current playback cycle.

## Overview

`StopBuff` ends a spline-buffer move ([MotionMode](../02-motion-configuration/MotionMode.md) spline-buffer). Rather than decelerating immediately, it requests the playback to stop **at the end of the cycle currently in progress**: the buffer plays out to the start of the next cycle and then the motion is ended. This keeps the spline trajectory continuous and avoids a velocity discontinuity. It is an axis-related command function and may be issued during motion.

For an immediate halt of a buffer move, use [Abort](Abort.md) (which clears the motion at once); for a `Decel`-ramped stop of all buffer members, use [Stop](Stop.md).

## How it works

### Requesting the stop

`StopBuff` does nothing unless the axis is actually in spline-buffer motion. When it is, the request is placed on the **primary axis** of the buffer group — the primary is read from the low byte of [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md) — under interrupts disabled:

| Field set by `StopBuff` (on the primary axis) | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 17 (spline-buffer-stop request) | 1 | Request to end the buffer motion at the end of the cycle |
| [MotionReason](../05-motion-status/MotionReason.md) | 35 | Records that the move is ending because of `StopBuff` |

### Ending at the cycle boundary

The profiler checks the request only at the **first sample of a playback cycle**. When that boundary is reached with the stop pending, it clears all motion bits, latches the profiler run time into [MotionSamples](../05-motion-status/MotionSamples.md), and propagates [MotionReason](../05-motion-status/MotionReason.md) = 35 (StopBuff command) to every member axis. This is the same end-of-cycle path the controller uses when [BuffCycles](../12-motion-mode-spline-buffer/BuffCycles.md) is exhausted — `StopBuff` simply forces the move to end on the next boundary instead of after the programmed number of cycles.

## Examples

```text
AStopBuff            ; end spline-buffer playback at the end of the current cycle
```

## See also

- [Stop](Stop.md) — controlled stop (decelerates buffer members over `Decel`)
- [Abort](Abort.md) — immediate end of a buffer move
- [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md) — spline-buffer playback status (primary axis, cycle/index)
- [BuffCycles](../12-motion-mode-spline-buffer/BuffCycles.md) — programmed cycle count `StopBuff` cuts short
- [MotionStat](../05-motion-status/MotionStat.md) — bit 17 (spline-buffer-stop request) set by `StopBuff`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 35 set by `StopBuff`
