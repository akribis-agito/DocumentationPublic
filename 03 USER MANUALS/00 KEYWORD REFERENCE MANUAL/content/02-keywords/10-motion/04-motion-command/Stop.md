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

`Stop` brings the axis to rest with a **controlled deceleration** using the normal [Decel](../03-kinematics-configuration/Decel.md) rate. Unlike [Abort](Abort.md), which clears the motion immediately, `Stop` does not stop the move itself — it sets a *request* bit that the trajectory profiler picks up on the next control cycle and then ramps the profiler velocity down to zero. It is an axis-related command function handled by `Stop()` in `AG300_CTL01Funcs.c:2509`, and may be issued at any time during motion.

## How it works

### Single-axis motion

For a normal single-axis move, `Stop` (under interrupts disabled) sets the stop-request bit and records the reason — but only if the axis is actually in motion (`AG300_CTL01Funcs.c:2661`):

| Field set by `Stop` | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 3 `IN_STOP_REQUEST_BIT` | 1 | A decelerate-to-stop has been requested |
| [MotionReason](../05-motion-status/MotionReason.md) | 1 (`MOTION_REASON_END_STOP`) | Records that this move is ending because of `Stop` |

On the next cycle the profiler sees `IN_STOP_REQUEST_BIT` and forces its **target speed to zero** (`gfSpeed = 0.0`, `AG300_CTL01Profiler.c:1013`). The velocity then ramps down at `Decel × AccelFact` (`gfDecelFinal`, `AG300_CTL01Profiler.c:1063`), smoothed by [Jerk](../03-kinematics-configuration/Jerk.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) exactly as the trailing slope of a normal move. Because the reason code is `MOTION_REASON_END_STOP` (not a limit/fault reason), the profiler keeps using [Decel](../03-kinematics-configuration/Decel.md) — it does **not** substitute [EmrgDec](../03-kinematics-configuration/EmrgDec.md) (which is reserved for limit-switch, software-limit and controlled-stop-input reasons, `AG300_CTL01Profiler.c:1066`).

When the profiler velocity reaches zero with the stop request pending, the motion enters the end-of-smoothing tail (`IN_WAIT_END_SMOOTH_BIT`) and finally clears all motion bits (`AG300_CTL01Profiler.c:1259`, `:461`). [MotionReason](../05-motion-status/MotionReason.md) keeps the value `1` after the axis comes to rest.

### Group motion

If the axis is a member of a group, `Stop` requests the stop along the whole group instead of the single axis (`AG300_CTL01Funcs.c:2520`–`2657`):

- **CNCA / CNCB member**: sets `IN_STOP_REQUEST_BIT` on every member axis and `CNC_IN_STOP_REQUEST_BIT` on the CNC path; the commanding axis gets reason `MOTION_REASON_END_STOP`, the others `..._CNC_ONE_MEMBER_WAS_STOPPED`. CNC step mode is disabled so the stop can proceed.
- **Vector member**: sets `IN_STOP_REQUEST_BIT` on all members and the master vector status to `VECTOR_IN_STOP`; the commanding axis gets `MOTION_REASON_END_STOP`, others `..._VEC_ONE_MEMBER_WAS_STOPPED`.
- **Spline-buffer member**: sets `IN_STOP_REQUEST_BIT` on all buffer members; the commanding axis gets `MOTION_REASON_END_STOP`, others `..._SPLINE_BUFFER_ONE_MEMBER_WAS_STOPPED`. (To stop a buffer move at the end of its current cycle instead of immediately decelerating, use [StopBuff](StopBuff.md).)

## Examples

```text
AStop                ; controlled stop using the normal Decel rate
```

## See also

- [Abort](Abort.md) — immediate stop (clears motion at once; not a `Decel` ramp)
- [Decel](../03-kinematics-configuration/Decel.md) — deceleration rate used by `Stop`
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency rate (used for limit/fault stops, not by `Stop`)
- [MotionStat](../05-motion-status/MotionStat.md) — bit 3 `IN_STOP_REQUEST_BIT` set by `Stop`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 1 set by `Stop`
- [StopBuff](StopBuff.md) / [StopRep](StopRep.md) — mode-specific stop variants
