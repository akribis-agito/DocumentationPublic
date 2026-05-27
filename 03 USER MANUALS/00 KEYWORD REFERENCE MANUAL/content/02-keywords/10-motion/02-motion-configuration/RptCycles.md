---
keyword: RptCycles
summary: Number of repetitions for repetitive point-to-point motion; 0 repeats indefinitely.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# RptCycles

Number of repetitions for repetitive point-to-point motion; `0` repeats indefinitely.

## Overview

`RptCycles` defines the number of repetitions for a repetitive point-to-point move. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion). What counts as one repetition depends on [RptMode](RptMode.md). Once the count reaches `RptCycles`, the motion ends; if `RptCycles=0`, the motion repeats indefinitely (until [StopRep](../04-motion-command/StopRep.md)). The running repetition count is reported by [RptCounter](../05-motion-status/RptCounter.md). It cannot be changed while the axis is in motion.

## Examples

```text
ARptCycles=10        ; perform 10 repetitions
ARptCycles=0         ; repeat indefinitely
ARptCycles          ; query current value
```

## See also

- [RptMode](RptMode.md) — defines what counts as one repetition
- [RptWait](RptWait.md) — dwell time between repetitions
- [RptCounter](../05-motion-status/RptCounter.md) — running repetition count
- [StopRep](../04-motion-command/StopRep.md) — stops repetitive motion
