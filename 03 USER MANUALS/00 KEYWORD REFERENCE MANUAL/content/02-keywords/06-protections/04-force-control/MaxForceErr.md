---
keyword: MaxForceErr
summary: Maximum allowable force error in closed-loop force control; exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 585
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
  - 327680
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErr

Maximum allowable force error in closed-loop force control; exceeding it faults.

## Overview

`MaxForceErr` is the maximum allowable force error in **closed-loop** force-control mode. If the difference between the commanded and measured force exceeds this threshold, the controller raises a fault. It is axis-related, saved to flash, and may be changed at any time including during motion. For the open-loop equivalent, see [MaxForceErrOL](MaxForceErrOL.md).

## Examples

```text
AMaxForceErr=2000    ; max closed-loop force error before fault
```

## See also

- [MaxForceErrOL](MaxForceErrOL.md) — open-loop force-error limit
