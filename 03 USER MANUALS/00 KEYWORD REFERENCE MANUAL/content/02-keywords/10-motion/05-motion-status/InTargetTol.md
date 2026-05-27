---
keyword: InTargetTol
summary: Position settling window (PosErr) used to declare target reached.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 265
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
  - 2147483647
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetTol

Position settling window (PosErr) used to declare target reached.

## Overview

In position or velocity control operation mode (`OperationMode = 2` or `3`), `InTargetTol` is the settling window that the absolute position error [PosErr](../01-kinematics-status/PosErr.md) must stay within for [InTargetTime](InTargetTime.md) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`). For current/force control the velocity-based window [InTargetVelTh](InTargetVelTh.md) is used instead.

## Examples

```text
InTargetTol=10      ; settling window in user units (default)
InTargetTol?        ; read current value
```

## See also

- [InTargetStat](InTargetStat.md) — settling state gated by this window
- [InTargetTime](InTargetTime.md) — minimum dwell time inside the window
- [InTargetVelTh](InTargetVelTh.md) — velocity settling window (current/force control)
