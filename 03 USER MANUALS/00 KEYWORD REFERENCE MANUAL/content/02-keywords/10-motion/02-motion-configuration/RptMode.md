---
keyword: RptMode
summary: Selects whether repetitive point-to-point motion is bidirectional or unidirectional.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 712
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RptMode

Selects whether repetitive point-to-point motion is bidirectional or unidirectional.

## Overview

`RptMode` defines whether repetitive motion is bidirectional (to-and-fro) or unidirectional (stepping ever further away), which is useful for repeated step-motion applications. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion), and it also determines what one repetition means for the [RptCycles](RptCycles.md) count. It cannot be changed while the axis is in motion.

## How it works

| RptMode | Descriptions |
|---|---|
| 0 | **Bidirectional motion** Axis will move to AbsTrgt (or relative location defined by RelTrgt) and then back to initial location. 1 repetition number equals to 1 motion to AbsTrgt (or relative location defined by RelTrgt), or 1 motion back to initial position This means RptCycles = 2 equals to one set of to-and-fro motion. |
| 1 | **Unidirectional motion** Axis will always move at the position delta of (AbsTrgt – initial position) or RelTrgt, where axis will move further and further away. 1 repetition number equals 1 delta motion. |

## Examples

```text
RptMode=0           ; bidirectional (to-and-fro)
RptMode=1           ; unidirectional (stepping away)
RptMode?            ; query current value
```

## See also

- [MotionMode](MotionMode.md) — must be 2 for `RptMode` to apply
- [RptCycles](RptCycles.md) — number of repetitions
- [RptWait](RptWait.md) — dwell time between repetitions
