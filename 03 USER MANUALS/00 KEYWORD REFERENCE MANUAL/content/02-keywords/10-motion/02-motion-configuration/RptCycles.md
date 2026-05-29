---
keyword: RptCycles
summary: Number of repetitions for repetitive point-to-point motion; 0 repeats indefinitely.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 713
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 731
---
# RptCycles

Number of repetitions for repetitive point-to-point motion; `0` repeats indefinitely.

## Overview

`RptCycles` defines the number of repetitions for a repetitive point-to-point move. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion). What counts as one repetition depends on [RptMode](RptMode.md). Once the count reaches `RptCycles`, the motion ends; if `RptCycles=0`, the motion repeats indefinitely (until [StopRep](../04-motion-command/StopRep.md)). The running repetition count is reported by [RptCounter](../05-motion-status/RptCounter.md). It cannot be changed while the axis is in motion.

## How it works

`Begin` resets [RptCounter](../05-motion-status/RptCounter.md) to `0` when a repetitive move starts. At the end of each individual move — after the smoothing tail (`2^Jerk` cycles) has flushed — the controller increments `RptCounter` and then decides whether to continue:

```text
continue  if  MotionMode == 2
          and StopRep not requested
          and ( RptCycles == 0  OR  RptCycles != RptCounter )
```

When the condition holds the axis enters the dwell state ([MotionStat](../05-motion-status/MotionStat.md) bit 1 set, the wait counter reset) and another move follows after [RptWait](RptWait.md); otherwise all in-motion bits are cleared and the move ends. Because the comparison is `RptCycles != RptCounter`, a value of `0` never matches the counter and so repeats forever, while a positive value stops exactly when `RptCounter` reaches it.

Note how the count interacts with [RptMode](RptMode.md): in **bidirectional** mode each leg (out, then back) is one count, so a full there-and-back cycle is two counts; in **unidirectional** mode each step is one count.

## Examples

```text
ARptCycles=10        ; perform 10 repetitions
ARptCycles=0         ; repeat indefinitely
ARptCycles          ; query current value
```

A worked example. With `RptMode = 0` (bidirectional) and `RptCycles = 4`, the axis does two round-trips: out, back, out, back (4 legs total). With `RptMode = 1` (unidirectional) and `RptCycles = 4`, the axis advances by the same delta four times (one direction only).

### Edge cases

- **Motor off:** value is held; read on the next `Begin`.
- **Out-of-range write:** the parameter system rejects negative values; valid range is `0`–`2^31−1`.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** unrelated; the cycle counter is incremented per-leg regardless of wrap events during the leg.
- **Active fault:** the axis is disabled and the running repetition is abandoned; on re-enable and next `Begin`, [RptCounter](../05-motion-status/RptCounter.md) is reset to `0`.
- **Other motion modes:** `RptCycles` is ignored outside [MotionMode](MotionMode.md) `= 2`; non-repetitive PTP completes once regardless.
- **`RptCycles = 0`:** repeats forever; only [StopRep](../04-motion-command/StopRep.md) (or [Stop](../04-motion-command/Stop.md)/[Abort](../04-motion-command/Abort.md)/a fault) ends it.
- **Cannot change in motion:** writes are rejected while the axis is in motion; queueing a new value only takes effect on the next `Begin`.
- **Value reduced below current RptCounter (between moves):** because the test is `RptCycles != RptCounter`, lowering `RptCycles` to a value already exceeded by `RptCounter` would only stop the move on the *next* increment — but this is moot because `RptCycles` cannot be written while in motion; if the axis is between `Begin`s, the next `Begin` resets `RptCounter` anyway.

## See also

- [RptMode](RptMode.md) — defines what counts as one repetition
- [RptWait](RptWait.md) — dwell time between repetitions
- [RptCounter](../05-motion-status/RptCounter.md) — running repetition count (compared against `RptCycles`)
- [StopRep](../04-motion-command/StopRep.md) — stops repetitive motion before the count is reached
- [MotionStat](../05-motion-status/MotionStat.md) — bit 1 marks the dwell between counted repetitions
