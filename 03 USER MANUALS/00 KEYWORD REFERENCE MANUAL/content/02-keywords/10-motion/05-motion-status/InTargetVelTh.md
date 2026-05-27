---
keyword: InTargetVelTh
summary: Velocity settling window (Vel[1]) used to declare target reached in current/force control.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 292
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetVelTh

Velocity settling window (Vel[1]) used to declare target reached in current/force control.

## Overview

In current or force control operation mode (`OperationMode = 1` or `4`), `InTargetVelTh` is the velocity settling window that the absolute feedback velocity [Vel](../01-kinematics-status/Vel.md) `[1]` must stay within for [InTargetTime](InTargetTime.md) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`). For position/velocity control the position-based window [InTargetTol](InTargetTol.md) is used instead.

## Examples

```text
InTargetVelTh=1000  ; velocity window in user units/s (default)
InTargetVelTh?      ; read current value
```

## See also

- [InTargetStat](InTargetStat.md) — settling state gated by this window
- [InTargetTime](InTargetTime.md) — minimum dwell time inside the window
- [InTargetTol](InTargetTol.md) — position settling window (position/velocity control)
