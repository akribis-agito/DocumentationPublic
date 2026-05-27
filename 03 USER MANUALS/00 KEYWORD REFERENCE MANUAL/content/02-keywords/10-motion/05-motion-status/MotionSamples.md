---
keyword: MotionSamples
summary: Move and settle times of the last completed motion, in controller cycles.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 267
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotionSamples

Move and settle times of the last completed motion, in controller cycles.

## Overview

`MotionSamples` reports the move and settle times of the last completed motion, used to characterise motion timing and settling performance. It is only used in position or velocity control operation mode (`OperationMode = 2` or `3`). Each value is a count of controller cycles (typically $T_{s} = \frac{1}{16384}\,\text{Hz} = 61.03515\,\mu s$ per cycle), so multiply by $T_{s}$ to obtain SI time. The settling components depend on [InTargetTime](InTargetTime.md).

## How it works

Each array element represents a different time:

| Index | Descriptions |
|----|----|
| 1 | Motion profile time |
| 2 | The time from the start of motion until the axis starts to settle into the target for at least InTargetTime. |
| 3 | The time from the start of motion until the axis settles into the target for at least InTargetTime. |
| 4 | The time from the end of motion profile until the axis starts to settle into the target for at least InTargetTime. |

In summary,

$$
MotionSamples\lbrack 2\rbrack = \ MotionSamples\lbrack 1\rbrack + \ MotionSamples\lbrack 4\rbrack
$$

$$
MotionSamples\lbrack 3\rbrack = \ MotionSamples\lbrack 2\rbrack + \frac{InTargetTime}{T_{s}}\ 
$$

## Examples

![image30.emf](../../../assets/image30.emf)

The plot above shows an example of MotionSamples. Since MotionSamples is in controller cycles, multiplication by sampling time (here, it is $T_{s} = 61.03515\mu s$) is needed to get the time in SI unit.

```text
MotionSamples[1]?   ; motion profile time of the last move (controller cycles)
MotionSamples[3]?   ; total time until settled for at least InTargetTime
```

## See also

- [InTargetTime](InTargetTime.md) — dwell time used in the `MotionSamples[3]` relation
- [InTargetStat](InTargetStat.md) — settling state of the axis
