---
keyword: RevPLim
summary: Reverse software travel limit; reference position is capped here.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 82
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
  default: -2000000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RevPLim

Reverse software travel limit; reference position is capped here.

## Overview

`RevPLim` is the reverse (negative) software travel limit, in counts. The reference position is capped at `RevPLim`: motion stops there if the reference would go lower, and any reverse motion whose final target is below `RevPLim` is rejected. It cannot be changed while the axis is in motion.

## Examples

```text
RevPLim=-1000000    ; reverse soft limit (counts)
```

## See also

- [FwdPLim](FwdPLim.md) — forward software travel limit
- [LimitsStat](LimitsStat.md) — hardware limit-switch status
