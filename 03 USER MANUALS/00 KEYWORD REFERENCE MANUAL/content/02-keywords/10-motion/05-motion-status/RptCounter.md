---
keyword: RptCounter
summary: Counts repetitions made during repetitive point-to-point (PTP) motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# RptCounter

Counts repetitions made during repetitive point-to-point (PTP) motion.

## Overview

`RptCounter` reports the number of repetitions made in repetitive PTP motion. It is used only when [MotionMode](../02-motion-configuration/MotionMode.md) `= 2` (repetitive PTP motion). How a repetition is defined depends on [RptMode](../02-motion-configuration/RptMode.md). Once `RptCounter` equals the non-zero [RptCycles](../02-motion-configuration/RptCycles.md), the repetitive PTP motion stops.

## Examples

```text
ARptCounter         ; read the number of repetitions completed
```

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects repetitive PTP motion (`= 2`)
- [RptCycles](../02-motion-configuration/RptCycles.md) — target repetition count that stops the motion
- [RptMode](../02-motion-configuration/RptMode.md) — defines how a repetition is counted
