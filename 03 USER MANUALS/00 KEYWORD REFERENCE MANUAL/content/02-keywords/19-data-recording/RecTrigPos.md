---
keyword: RecTrigPos
summary: Percentage of RecLength captured before the trigger (pre-trigger data).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 247
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigPos

Percentage of RecLength captured before the trigger (pre-trigger data).

## Overview

`RecTrigPos` defines the percentage of data points, out of [RecLength](RecLength.md), to capture before the trigger condition(s) activate. It is normally used during debugging to allow monitoring of the data leading up to the trigger event. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## Examples

```text
RecTrigPos[1]=10    ; reserve 10% of RecLength for pre-trigger data
RecTrigPos[1]?      ; query the first scope pre-trigger percentage
```

If `RecLength[1] = 16384` and `RecTrigPos[1] = 10`, the first scope will have 1638 pre-trigger data points and 14746 post-trigger data points.

## See also

- [RecLength](RecLength.md) — total data points per parameter
- [RecStat](RecStat.md) — reports when pre-trigger data is filled
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
