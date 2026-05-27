---
keyword: MaxForceErrOL
summary: Maximum allowable force error in open-loop force control; exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 591
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
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErrOL

Maximum allowable force error in open-loop force control; exceeding it faults.

## Overview

`MaxForceErrOL` is the maximum allowable force error in **open-loop** force-control mode (OL = open loop). If the force error exceeds this limit in open-loop operation, the controller raises a fault. It is axis-related, saved to flash, and may be changed at any time including during motion. It is the open-loop counterpart of [MaxForceErr](MaxForceErr.md) (its default is larger, as open-loop error is naturally greater).

## Examples

```text
AMaxForceErrOL=50000 ; max open-loop force error before fault
```

## See also

- [MaxForceErr](MaxForceErr.md) — closed-loop force-error limit
