---
keyword: InTargetTime
summary: Minimum dwell time inside the settling window before target-reached is signalled.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 266
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
  - 163840
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetTime

Minimum dwell time inside the settling window before target-reached is signalled.

## Overview

`InTargetTime` is the minimum time that the absolute value of the monitored signal — [PosErr](../01-kinematics-status/PosErr.md) or [Vel](../01-kinematics-status/Vel.md) `[1]` — must remain within the settling window ([InTargetTol](InTargetTol.md) or [InTargetVelTh](InTargetVelTh.md)) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`).

## Examples

```text
AInTargetTime=100    ; require the window to be held for the configured duration
AInTargetTime       ; read current value
```

## See also

- [InTargetStat](InTargetStat.md) — settling state this time gates the transition to "reached"
- [InTargetTol](InTargetTol.md) — position settling window
- [InTargetVelTh](InTargetVelTh.md) — velocity settling window
