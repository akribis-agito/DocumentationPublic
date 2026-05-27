---
keyword: ProgSnapSrc
summary: Selects which parameters the program snapshot mechanism captures.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 537
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgSnapSrc

Selects which parameters the program snapshot mechanism captures.

## Overview

`ProgSnapSrc` is an array parameter that configures which controller parameters are captured by the program snapshot mechanism. Each element specifies a source parameter to record when a snapshot is triggered; the captured values are read back from [ProgSnapVal](ProgSnapVal.md). It mirrors the fault-snapshot mechanism configured by [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md). It is a non-axis parameter and is saved to flash.

## Examples

```text
AProgSnapSrc[1]=<CAN code of parameter to capture>   ; first snapshot source
```

## See also

- [ProgSnapVal](ProgSnapVal.md) — values captured by the snapshot mechanism
- [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md) — fault-snapshot source selection
