---
keyword: PeakCL
summary: Peak current limit, used for both current-command saturation and I²t protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 52
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 20
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PeakCL

Peak current limit, used for both current-command saturation and I²t protection.

## Overview

`PeakCL` is the peak current limit. It serves two roles: it is the upper bound used by the I²t scheme (with [ContCL](ContCL.md) and [PeakTime](PeakTime.md)), and — when the current-limit mode [CurrLimMode](CurrLimMode.md) is `0` — it caps the current command, so the absolute value of the command never exceeds `PeakCL`.

## Examples

```text
APeakCL=64000        ; peak current limit (mA)
```

## See also

- [ContCL](ContCL.md) — continuous current limit
- [PeakTime](PeakTime.md) — time allowed at peak current
- [CurrLimMode](CurrLimMode.md) — selects how the current command is limited
