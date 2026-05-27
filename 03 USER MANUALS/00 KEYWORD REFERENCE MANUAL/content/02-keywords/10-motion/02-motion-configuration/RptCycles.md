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

`Begin` resets [RptCounter](../05-motion-status/RptCounter.md) to `0` when a repetitive move starts (`AG300_CTL01Funcs.c:1164`). At the end of each individual move — after the smoothing tail (`2^Jerk` cycles) has flushed — the profiler increments `RptCounter` (`AG300_CTL01Profiler.c:446`) and then decides whether to continue:

```text
continue  if  MotionMode == 2
          and StopRep not requested  (IN_REPETITIVE_STOP_BIT clear)
          and ( RptCycles == 0  OR  RptCycles != RptCounter )
```

(`AG300_CTL01Profiler.c:449`–`451`.) When the condition holds the axis enters the dwell state (`IN_WAITING_BIT` set, the wait counter reset) and another move follows after [RptWait](RptWait.md); otherwise all in-motion bits are cleared and the move ends. Because the comparison is `RptCycles != RptCounter`, a value of `0` never matches the counter and so repeats forever, while a positive value stops exactly when `RptCounter` reaches it.

Note how the count interacts with [RptMode](RptMode.md): in **bidirectional** mode each leg (out, then back) is one count, so a full there-and-back cycle is two counts; in **unidirectional** mode each step is one count.

## Examples

```text
ARptCycles=10        ; perform 10 repetitions
ARptCycles=0         ; repeat indefinitely
ARptCycles          ; query current value
```

## See also

- [RptMode](RptMode.md) — defines what counts as one repetition
- [RptWait](RptWait.md) — dwell time between repetitions
- [RptCounter](../05-motion-status/RptCounter.md) — running repetition count (compared against `RptCycles`)
- [StopRep](../04-motion-command/StopRep.md) — stops repetitive motion before the count is reached
- [MotionStat](../05-motion-status/MotionStat.md) — `IN_WAITING_BIT` marks the dwell between counted repetitions
