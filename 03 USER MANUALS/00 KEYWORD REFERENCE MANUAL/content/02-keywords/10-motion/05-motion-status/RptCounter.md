---
keyword: RptCounter
summary: Counts repetitions made during repetitive point-to-point (PTP) motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 714
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
    can_code: 732
---
# RptCounter

Counts repetitions made during repetitive point-to-point (PTP) motion.

## Overview

`RptCounter` reports the number of repetitions made in repetitive PTP motion. It is used only when [MotionMode](../02-motion-configuration/MotionMode.md) `= 2` (repetitive PTP motion). How a repetition is defined depends on [RptMode](../02-motion-configuration/RptMode.md). Once `RptCounter` equals the non-zero [RptCycles](../02-motion-configuration/RptCycles.md), the repetitive PTP motion stops.

## How it works

`RptCounter` is reset to `0` when a new motion is commanded (the `Begin` handler resets it alongside `MotionReason` and `InTargetStat`). The controller then increments it by one at the end of each repetition — specifically once the end-of-smoothing wait for a repetition has elapsed, and only while in repetitive PTP mode.

After incrementing, the controller decides whether to start another repetition: it continues only if no [StopRep](../04-motion-command/StopRep.md) is pending and either [RptCycles](../02-motion-configuration/RptCycles.md) `= 0` (run indefinitely) or `RptCounter ≠ RptCycles`. When `RptCounter` reaches a non-zero `RptCycles` the motion ends instead of looping. The next target for each repetition is set from [RptMode](../02-motion-configuration/RptMode.md): mode 1 reflects the target about the current reference (back-and-forth), otherwise it returns toward the previous start position.

## Examples

```text
ARptCounter         ; read the number of repetitions completed
```

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects repetitive PTP motion (`= 2`)
- [RptCycles](../02-motion-configuration/RptCycles.md) — target repetition count that stops the motion
- [RptMode](../02-motion-configuration/RptMode.md) — defines how a repetition is counted
- [StopRep](../04-motion-command/StopRep.md) — ends repetitive PTP motion after the current repetition
