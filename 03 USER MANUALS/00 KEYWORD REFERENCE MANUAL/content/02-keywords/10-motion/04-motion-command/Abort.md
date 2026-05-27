---
keyword: Abort
summary: Immediately stops motion using the emergency deceleration rate (EmrgDec).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 133
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
# Abort

Stops motion immediately by clearing the motion state, with no profiler deceleration ramp.

## Overview

`Abort` stops axis motion **immediately**. Unlike [Stop](Stop.md) — which sets a request bit and lets the profiler ramp the velocity down over a controlled [Decel](../03-kinematics-configuration/Decel.md) deceleration — `Abort` clears the whole [MotionStat](../05-motion-status/MotionStat.md) word to `NOT_IN_MOTION` (0) in the same call. From the next control cycle the profiler is no longer in motion: it sets its internal velocity to zero and freezes [PosRef](../01-kinematics-status/PosRef.md) at its current value (`AG300_CTL01Profiler.c:10274`). The actual physical deceleration is then whatever the position/velocity loop produces while holding the now-frozen reference, not a planned `EmrgDec` ramp. `Abort` is an axis-related command function handled by `Abort()` in `AG300_CTL01Funcs.c:2673`, and may be issued at any time during motion.

> **Note on `EmrgDec`:** in this firmware the profiler's emergency-deceleration rate [EmrgDec](../03-kinematics-configuration/EmrgDec.md) is selected by **motion-reason** codes — limit switches, software position limits and the controlled-stop digital input (`AG300_CTL01Profiler.c:1066`). The `Abort` command itself does not run that deceleration path; it ends the move at once. Use a controlled-stop input or a software limit if a planned `EmrgDec` ramp is required.

## How it works

### Single-axis motion

For a normal single-axis move, `Abort` (under interrupts disabled) ends the motion immediately, but only if the axis is in motion (`AG300_CTL01Funcs.c:2857`):

| Action by `Abort` | Effect |
|---|---|
| [MotionReason](../05-motion-status/MotionReason.md) = 2 (`MOTION_REASON_END_ABORT`) | Records that the move ended because of `Abort` |
| [MotionStat](../05-motion-status/MotionStat.md) = `NOT_IN_MOTION` (0) | Forces immediate end of motion — clears `IN_MOTION_BIT` and every other status bit at once |
| `glMotionSamples[PROFILER_INDEX]` = current sample count | Latches the profiler run time into [MotionSamples](../05-motion-status/MotionSamples.md) |

Clearing [MotionStat](../05-motion-status/MotionStat.md) to 0 is what makes the stop immediate: with no motion bit set, the profiler's no-motion branch zeroes its velocity and holds [PosRef](../01-kinematics-status/PosRef.md), so no further trajectory is generated.

### Group motion

If the axis belongs to a group, `Abort` tears the whole group down at once (`AG300_CTL01Funcs.c:2684`–`2866`):

- **CNCA / CNCB member**: clears every member's motion bits (`MotionStat & ALL_IN_MOTION_BITS_CLEAR`) and resets the CNC status to `CNC_NOT_IN_MOTION`; the commanding axis gets reason `MOTION_REASON_END_ABORT`, the others `..._CNC_ONE_MEMBER_WAS_ABORTED`. CNC step mode is disabled.
- **Vector member**: clears all member motion bits and sets the master vector status to `VECTOR_NOT_IN_MOTION`; the commanding axis gets `MOTION_REASON_END_ABORT`, others `..._VEC_ONE_MEMBER_WAS_ABORTED`.
- **Spline-buffer member**: forces each member's [MotionStat](../05-motion-status/MotionStat.md) to `NOT_IN_MOTION`; the commanding axis gets `MOTION_REASON_END_ABORT`, others `..._SPLINE_BUFFER_ONE_MEMBER_WAS_ABORTED`.

In all cases the profiler run time is latched into [MotionSamples](../05-motion-status/MotionSamples.md) for every affected axis.

## Examples

```text
AAbort               ; immediately end motion on axis A
```

## See also

- [Stop](Stop.md) — controlled stop that ramps down over `Decel`
- [Decel](../03-kinematics-configuration/Decel.md) — deceleration used by `Stop` (not by `Abort`)
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency rate, selected by limit/fault reasons rather than by `Abort`
- [MotionStat](../05-motion-status/MotionStat.md) — cleared to 0 by `Abort`
- [MotionReason](../05-motion-status/MotionReason.md) — reason code 2 set by `Abort`
