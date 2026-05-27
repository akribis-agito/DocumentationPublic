---
keyword: RptWait
summary: Dwell time, in milliseconds, between repetitions of repetitive point-to-point motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
  scaling: 1.0
  implemented: final
overrides: {}
---
# RptWait

Dwell time, in milliseconds, between repetitions of repetitive point-to-point motion.

## Overview

`RptWait` is the dwell time, in milliseconds, inserted between successive point-to-point motions during a repetitive move. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion), and it governs the pause between the individual repetitions counted by [RptCycles](RptCycles.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
ARptWait=500         ; dwell 500 ms between repetitions
ARptWait            ; query current value
```

## See also

- [MotionMode](MotionMode.md) — must be 2 for `RptWait` to apply
- [RptCycles](RptCycles.md) — number of repetitions
- [RptMode](RptMode.md) — repetition direction
