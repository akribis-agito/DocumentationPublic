---
keyword: RptWait
summary: Dwell time, in milliseconds, between repetitions of repetitive point-to-point motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 147
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
---
# RptWait

Dwell time, in milliseconds, between repetitions of repetitive point-to-point motion.

## Overview

`RptWait` is the dwell time, in milliseconds, inserted between successive point-to-point motions during a repetitive move. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion), and it governs the pause between the individual repetitions counted by [RptCycles](RptCycles.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

When one repetition finishes and another is due, the controller sets bit 1 (dwell) of [MotionStat](../05-motion-status/MotionStat.md) and clears a dwell counter. While that bit is set the profiler is in the dwell branch: each control cycle it increments the dwell counter and compares it to `RptWait`. Until the counter reaches `RptWait` the profiler holds the axis at rest (profiler velocity forced to zero) and runs the normal in-target/settling bookkeeping, exactly as between separate moves.

When the dwell counter reaches `RptWait` the controller clears bit 1, loads the next target ([RptMode](RptMode.md) decides whether that is the original start or the next step), re-arms the in-target status and friction-compensation flag, and the next move begins. With `RptWait = 0` the wait branch is satisfied immediately, so the next move starts on the very next cycle with no dwell.

The value you set is in milliseconds; the controller converts it to a whole number of servo cycles using the sample-time scaling factor (the dwell counter advances every control cycle and counts up to that converted target), so the actual pause is approximately `RptWait` milliseconds rounded to the nearest control cycle. If [StopRep](../04-motion-command/StopRep.md) (or a fault stop) arrives during the dwell, the motion ends immediately without starting the next repetition.

### Edge cases

- **Motor off:** value is held; the dwell branch is not entered while the axis is disabled.
- **Out-of-range write:** the parameter system rejects negative values; range is `0`–`2^31−1` in scaled units.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** unrelated; the dwell counter is independent of position.
- **Active fault:** the axis is disabled and the dwell ends immediately; the repetition is abandoned.
- **Other motion modes:** `RptWait` is ignored outside [MotionMode](MotionMode.md) `= 2`.
- **`RptWait = 0`:** no dwell — the next move starts on the very next control cycle. The settling/in-target bookkeeping that normally runs during the dwell is folded into the move transition.
- **Stop/Abort during dwell:** [Stop](../04-motion-command/Stop.md), [Abort](../04-motion-command/Abort.md) and [StopRep](../04-motion-command/StopRep.md) all end the repetition at the next cycle (no further motion).
- **Can change in motion:** unlike `RptCycles`/`RptMode`, `RptWait` can be changed while the axis is in motion — changing it during a dwell takes effect immediately (compared against the running counter).

## Examples

```text
ARptWait=500         ; dwell 500 ms between repetitions
ARptWait            ; query current value
```

## See also

- [MotionMode](MotionMode.md) — must be 2 for `RptWait` to apply
- [RptCycles](RptCycles.md) — number of repetitions
- [RptMode](RptMode.md) — repetition direction
- [MotionStat](../05-motion-status/MotionStat.md) — bit 1 reports the dwell
- [StopRep](../04-motion-command/StopRep.md) — ends repetitive motion (also during the dwell)
