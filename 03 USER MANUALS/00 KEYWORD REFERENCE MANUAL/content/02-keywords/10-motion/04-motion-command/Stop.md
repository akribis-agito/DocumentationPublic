---
keyword: Stop
summary: Controlled stop; decelerates the axis to rest using the normal Decel rate.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 132
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
# Stop

Controlled stop; decelerates the axis to rest using the normal `Decel` rate.

## Overview

`Stop` brings the axis to rest with a **controlled deceleration** using the normal [Decel](../03-kinematics-configuration/Decel.md) rate. Unlike [Abort](Abort.md), which clears the motion immediately, `Stop` does not stop the move itself — it sets a *request* bit that the trajectory profiler picks up on the next control cycle and then ramps the profiler velocity down to zero. It is an axis-related command function and may be issued at any time during motion.

## How it works

### Single-axis motion

For a normal single-axis move, `Stop` (under interrupts disabled) sets the stop-request bit and records the reason — but only if the axis is actually in motion:

| Field set by `Stop` | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 3 (stop-request) | 1 | A decelerate-to-stop has been requested |
| [MotionReason](../05-motion-status/MotionReason.md) | 1 | Records that this move is ending because of `Stop` |

On the next cycle the profiler sees the stop-request bit and forces its **target speed to zero**. The velocity then ramps down at `Decel × AccelFact`, smoothed by [Jerk](../03-kinematics-configuration/Jerk.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) exactly as the trailing slope of a normal move. Because the reason code is the controlled-stop reason (1, not a limit/fault reason), the profiler keeps using [Decel](../03-kinematics-configuration/Decel.md) — it does **not** substitute [EmrgDec](../03-kinematics-configuration/EmrgDec.md) (which is reserved for limit-switch, software-limit and controlled-stop-input reasons).

When the profiler velocity reaches zero with the stop request pending, the motion enters the end-of-smoothing tail and finally clears all motion bits. [MotionReason](../05-motion-status/MotionReason.md) keeps the value `1` after the axis comes to rest.

### Group motion

If the axis is a member of a group, `Stop` requests the stop along the whole group instead of the single axis:

- **CNCA / CNCB member**: requests the stop on every member axis and on the CNC path; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 19 (one CNCA member stopped) / 25 for CNCB. CNC step mode is disabled so the stop can proceed.
- **Vector member**: requests the stop on all members and sets the master vector status to stopping; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 31 (one vector member stopped).
- **Spline-buffer member**: requests the stop on all buffer members; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 37 (one spline-buffer member stopped). (To stop a buffer move at the end of its current cycle instead of immediately decelerating, use [StopBuff](StopBuff.md).)

## Examples

```text
AStop                ; controlled stop using the normal Decel rate
```

## See also

- [Abort](Abort.md) — immediate stop (clears motion at once; not a `Decel` ramp)
- [Decel](../03-kinematics-configuration/Decel.md) — deceleration rate used by `Stop`
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency rate (used for limit/fault stops, not by `Stop`)
- [MotionStat](../05-motion-status/MotionStat.md) — bit 3 (stop-request) set by `Stop`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 1 set by `Stop`
- [StopBuff](StopBuff.md) / [StopRep](StopRep.md) — mode-specific stop variants
