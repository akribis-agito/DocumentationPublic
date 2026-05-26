---
keyword: CurrLimFwd
summary: Positive current-command limit (used when CurrLimMode = 3).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 393
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
overrides: {}
---
# CurrLimFwd

Positive current-command limit (used when CurrLimMode = 3).

## Overview

`CurrLimFwd` defines the **positive** current-command limit, overriding the default [PeakCL](PeakCL.md) limit. It applies only when [CurrLimMode](CurrLimMode.md) is `3`. The value should be positive.

## Examples

```text
CurrLimMode=3
CurrLimFwd=40000    ; positive current limit (mA)
```

## See also

- [CurrLimRev](CurrLimRev.md) — negative current-command limit
- [CurrLimMode](CurrLimMode.md) — must be 3 for this to apply
