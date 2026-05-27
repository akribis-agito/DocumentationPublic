---
keyword: StuckTime
summary: Duration the stuck condition must persist before the axis is flagged stuck.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 88
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
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckTime

Duration the stuck condition must persist before the axis is flagged stuck.

## Overview

`StuckTime` is the duration used for motor-stuck detection: the high-current / low-velocity condition (current above [StuckCurr](StuckCurr.md) while velocity stays below [StuckVel](StuckVel.md)) must persist for `StuckTime` before the axis is declared stuck.

## Examples

```text
AStuckTime=4096      ; how long the stuck condition must hold
```

## See also

- [StuckCurr](StuckCurr.md) — current threshold
- [StuckVel](StuckVel.md) — velocity threshold
