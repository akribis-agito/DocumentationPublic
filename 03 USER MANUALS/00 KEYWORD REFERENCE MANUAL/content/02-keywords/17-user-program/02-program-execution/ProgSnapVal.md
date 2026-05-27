---
keyword: ProgSnapVal
summary: Holds the values captured by the program snapshot mechanism.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 538
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ProgSnapVal

Holds the values captured by the program snapshot mechanism.

## Overview

`ProgSnapVal` is a read-only array parameter that holds the values captured by the program snapshot mechanism. Each element contains the last recorded value for the corresponding source defined in [ProgSnapSrc](ProgSnapSrc.md). It is the snapshot counterpart of the fault-snapshot values in [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md). It is a non-axis status variable and is not saved to flash.

## Examples

```text
AProgSnapVal[1]     ; read the value captured for the first snapshot source
```

## See also

- [ProgSnapSrc](ProgSnapSrc.md) — snapshot source selection
- [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md) — fault-snapshot captured values
