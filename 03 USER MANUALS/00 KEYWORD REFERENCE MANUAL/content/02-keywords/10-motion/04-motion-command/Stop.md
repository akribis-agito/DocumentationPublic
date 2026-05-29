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

On the next cycle the profiler sees the stop-request bit and forces its **target speed to zero**. The velocity then ramps down at `Decel × AccelFact`, smoothed by [Jerk](../03-kinematics-configuration/Jerk.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) exactly as the trailing slope of a normal move. Because the reason code is the controlled-stop reason (1, not a limit/fault reason), the profiler keeps using [Decel](../03-kinematics-configuration/Decel.md) — it does **not** substitute [EmrgDec](../03-kinematics-configuration/EmrgDec.md).

The profiler computes its final deceleration from `EmrgDec × AccelFact` for exactly five [MotionReason](../05-motion-status/MotionReason.md) codes — RLS reached (4), FLS reached (5), reverse position-limit reached (6), forward position-limit reached (7), and controlled stop by input (28) — and from `Decel × AccelFact` for every other reason, including the `Stop` command (1). The two stop sources are also distinct in [MotionStat](../05-motion-status/MotionStat.md): `Stop` sets the stop-request bit (bit 3), while the controlled-stop digital input sets the controlled-stop-request bit (bit 16). The profiler treats either request bit as "stop requested", but only the controlled-stop-input reason (28) selects the `EmrgDec` ramp.

When the profiler velocity reaches zero with the stop request pending, the motion enters the end-of-smoothing tail and finally clears all motion bits. [MotionReason](../05-motion-status/MotionReason.md) keeps the value `1` after the axis comes to rest.

### Group motion

If the axis is a member of a group, `Stop` requests the stop along the whole group instead of the single axis:

- **CNCA / CNCB member**: requests the stop on every member axis and on the CNC path; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 19 (one CNC member stopped). CNC step mode is disabled so the stop can proceed.
- **Vector member**: requests the stop on all members and sets the master vector status to stopping; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 31 (one vector member stopped).
- **Spline-buffer member**: requests the stop on all buffer members; the commanding axis gets [MotionReason](../05-motion-status/MotionReason.md) = 1 (Stop command), the other members [MotionReason](../05-motion-status/MotionReason.md) = 37 (one spline-buffer member stopped). (To stop a buffer move at the end of its current cycle instead of immediately decelerating, use [StopBuff](StopBuff.md).)

## Examples

```text
AStop                ; controlled stop using the normal Decel rate
```

### Edge cases

- **Motor off:** `Stop` is accepted but has no effect (there is no profiler running).
- **Not in motion:** `Stop` updates no state — the function checks the in-motion bit before setting the stop-request bit.
- **Out-of-range "write":** function has no value.
- **Simulation mode (`MotorType` = 5):** allowed; the simulated profiler ramps down.
- **ModRev wrap:** the ramp-down works through a wrap; the profiler stops at zero velocity wherever the wrap leaves it.
- **Active fault:** the axis is disabled — `Stop` is a no-op (the motor-off path overrides the ramp).
- **During dwell of repetitive PTP (`MotionMode = 2`):** the stop request is honored and ends the repetition; the dwell's wait counter is abandoned.
- **PTPKeepMoving = 1:** `Stop` still ends the move; the keep-moving flag is overridden by the stop-request bit.
- **Member of CNCA / CNCB / vector / spline-buffer:** the whole group is requested to stop; per-axis reasons are listed above.

## See also

- [Abort](Abort.md) — immediate stop (clears motion at once; not a `Decel` ramp)
- [Begin](Begin.md) — the command this `Stop` ends
- [Decel](../03-kinematics-configuration/Decel.md) — deceleration rate used by `Stop`
- [Jerk](../03-kinematics-configuration/Jerk.md) / [JerkInDec](../03-kinematics-configuration/JerkInDec.md) — smooth the `Stop` trailing slope
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency rate (used for limit/fault stops, not by `Stop`)
- [MotionStat](../05-motion-status/MotionStat.md) — bit 3 (stop-request) set by `Stop`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 1 set by `Stop`
- [StopBuff](StopBuff.md) / [StopRep](StopRep.md) — mode-specific stop variants
