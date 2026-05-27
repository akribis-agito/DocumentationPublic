---
summary: Index of the master axis whose current reference a slave drive copies.
keyword: CurrRefMaster
availability:
  standalone: []
  central-i:
  - v5
can_code: 553
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrRefMaster

Index of the master axis whose current reference a slave drive copies.

## Overview

`CurrRefMaster` is the index of the master axis (0-based) used in slave-drive mode: the slave axis copies its current reference (`CurrRef`) from the `CurrRef` of the master axis. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 3.

## How it works

| Value | Axis |
|-------|------|
| 0     | A    |
| 1     | B    |
| …     | …    |

## Examples

```text
ACurrCmdSrc=3        ; follow a master axis (slave drive)
ACurrRefMaster=0     ; copy current reference from axis A
```

## See also

- [CurrCmdSrc](CurrCmdSrc.md) — selects master-axis current command (value 3)
- [Current operation mode](00-overview.md) — overview of current-mode keywords
