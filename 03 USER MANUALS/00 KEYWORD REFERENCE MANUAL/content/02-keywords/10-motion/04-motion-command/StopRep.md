---
keyword: StopRep
summary: Stops repetitive (repeat) motion and clears the repeat-motion state.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 148
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
# StopRep

Ends repetitive point-to-point motion after the repetition in progress, instead of running to RptCycles.

## Overview

`StopRep` ends repetitive point-to-point motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 2`, PTP-repetitive). It does not stop the axis mid-move: it requests that the repetition cycle **not be restarted**, so the current repetition completes normally and the move then ends — rather than continuing until [RptCycles](../02-motion-configuration/RptCycles.md) is reached. The remaining motion (the in-progress repetition or the dwell between repetitions) still uses the normal [Decel](../03-kinematics-configuration/Decel.md) profile. It is an axis-related command function and may be issued during motion.

## How it works

### Requesting the stop

`StopRep` (under interrupts disabled) sets the repetitive-stop request bit and records the reason:

| Field set by `StopRep` | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 2 (repetitive-stop) | 1 | Request to end the repetitive motion |
| [MotionReason](../05-motion-status/MotionReason.md) | 3 | Records that the move is ending because of `StopRep` |

### How the profiler ends the repetition

Repetitive motion alternates between a moving phase and a dwell (the waiting bit, held for [RptWait](../02-motion-configuration/RptWait.md) cycles), counting completed repetitions in [RptCounter](../05-motion-status/RptCounter.md). At the end of each repetition's smoothing tail the profiler decides whether to start another one. That decision requires the repetitive-stop bit to be **clear**: a new repetition is started only while the repetitive-stop bit is clear and [RptCycles](../02-motion-configuration/RptCycles.md) is either 0 (endless) or not yet reached; otherwise the motion ends and all motion bits are cleared.

So once `StopRep` has set the bit, the next time a repetition finishes the profiler ends the move instead of starting the dwell. If the bit is set while the axis is already in the inter-repetition dwell, the dwell is ended and the motion is cleared on that cycle. Either way [MotionReason](../05-motion-status/MotionReason.md) keeps the value `3`. The direction/return behaviour of the repetitions is configured by [RptMode](../02-motion-configuration/RptMode.md).

## Examples

```text
AStopRep             ; finish the current repetition, then stop (do not start another)
```

## See also

- [Stop](Stop.md) — general controlled stop (decelerates to rest now)
- [RptMode](../02-motion-configuration/RptMode.md) — repetition direction (back-and-forth vs unidirectional)
- [RptCycles](../02-motion-configuration/RptCycles.md) — programmed repetition count `StopRep` cuts short
- [RptWait](../02-motion-configuration/RptWait.md) — dwell between repetitions
- [RptCounter](../05-motion-status/RptCounter.md) — completed-repetition count
- [MotionStat](../05-motion-status/MotionStat.md) — bit 2 (repetitive-stop) set by `StopRep`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 3 set by `StopRep`
