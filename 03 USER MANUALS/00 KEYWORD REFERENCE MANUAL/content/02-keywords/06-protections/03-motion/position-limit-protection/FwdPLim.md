---
keyword: FwdPLim
summary: Forward software travel limit; reference position is capped here.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 83
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2000000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# FwdPLim

Forward software travel limit; reference position is capped here.

## Overview

`FwdPLim` is the forward (positive) software travel limit, in counts. The reference position is capped at `FwdPLim`: motion stops there if the reference would go higher, and any forward motion whose final target is above `FwdPLim` is rejected. It cannot be changed while the axis is in motion.

## Examples

```text
FwdPLim=1000000     ; forward soft limit (counts)
```

## See also

- [RevPLim](RevPLim.md) — reverse software travel limit
- [LimitsStat](LimitsStat.md) — hardware limit-switch status
