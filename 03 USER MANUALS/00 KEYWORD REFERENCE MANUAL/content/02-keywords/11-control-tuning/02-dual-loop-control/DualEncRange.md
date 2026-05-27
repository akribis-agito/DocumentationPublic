---
keyword: DualEncRange
availability:
  standalone: []
  central-i:
  - v5
can_code: 726
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualEncRange

Motor-feedback position range within which true dual-loop control is used.

## Overview

`DualEncRange` defines the lower and upper motor-feedback ([AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md)) bounds for range-limited dual-loop control. True dual-loop control is used while the motor feedback is inside this range; pseudo dual-loop control is used outside it. It is only used when [DualLoopOn](DualLoopOn.md) = 1, [DualEncSwapOn](DualEncSwapOn.md) = 1 and [DualEncMode](DualEncMode.md) = 1.

| Index | Description |
|---|---|
| `DualEncRange[1]` | Lower bound of the position range |
| `DualEncRange[2]` | Upper bound of the position range |

The bounds are in motor (auxiliary) encoder counts. The third array element is reserved.

## How it works

Each control cycle, with range-limited mode active, the controller tests the motor feedback against the two bounds:

$$
DualEncRange[1] \le AuxPos \le DualEncRange[2]
$$

When the condition holds, true dual-loop control is active and [DualLoopStat](DualLoopStat.md) reads `2`; when it does not hold, pseudo dual-loop control is active and [DualLoopStat](DualLoopStat.md) reads `1`. A position offset is maintained across the boundary so the switch does not produce a position step.

## Examples

```text
ADualEncRange[1]=-500000   ; lower bound (motor-encoder counts)
ADualEncRange[2]=500000    ; upper bound (motor-encoder counts)
ADualEncMode=1             ; enable range-limited dual-loop
```

## See also

- [DualEncMode](DualEncMode.md) — enables range-limited dual-loop (required = 1)
- [DualEncSwapOn](DualEncSwapOn.md) — pseudo dual-loop switch (required = 1)
- [DualLoopOn](DualLoopOn.md) — enable dual-loop control (required = 1)
- [DualLoopStat](DualLoopStat.md) — reports the structure active at the current position
- [AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md) — motor feedback compared against the range
