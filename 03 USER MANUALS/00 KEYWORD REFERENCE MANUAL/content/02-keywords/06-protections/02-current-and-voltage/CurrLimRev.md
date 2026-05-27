---
keyword: CurrLimRev
summary: Negative current-command limit (used when CurrLimMode = 3).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 394
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
  - 0
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrLimRev

Negative current-command limit (used when CurrLimMode = 3).

## Overview

`CurrLimRev` defines the **negative** current-command limit, overriding the default [PeakCL](PeakCL.md) limit. It applies only when [CurrLimMode](CurrLimMode.md) is `3`. The value should be given as a positive number (it bounds the negative side, i.e. the command is limited to −`CurrLimRev`).

## Examples

```text
ACurrLimMode=3
ACurrLimRev=40000    ; magnitude of the negative current limit (mA)
```

## See also

- [CurrLimFwd](CurrLimFwd.md) — positive current-command limit
- [CurrLimMode](CurrLimMode.md) — must be 3 for this to apply
