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

`CurrRefMaster` is the index of the master axis (0-based) used in slave-drive mode: the slave axis copies its current reference (`CurrRef`) from the `CurrRef` of the master axis. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 3, which exists only in the central-i v5 firmware.

## How it works

Each control cycle, while in current mode with `CurrCmdSrc` = 3, the firmware sets this axis' `CurrRef` directly equal to `CurrRef[CurrRefMaster]` — i.e. it tracks the master axis' current reference sample-for-sample. The master index is a plain 0-based axis number:

| Value | Axis |
|-------|------|
| 0     | A    |
| 1     | B    |
| …     | …    |

The duration of slave-drive operation is governed by [CurrCmdHTime](CurrCmdHTime.md)`[1]` exactly as for the analog source: if `CurrCmdHTime[1]` is negative the slave follows the master indefinitely; if it is 0 or positive the axis returns to position mode when [CurrCmdCntr](CurrCmdCntr.md) exceeds it. No ramp ([CurrCmdSlope](CurrCmdSlope.md)) or table stepping applies in this source.

> **Note:** `CurrRefMaster` cannot be changed while the motor is on or in motion. Configure it before enabling slave-drive operation.

## Examples

```text
ACurrCmdSrc=3        ; follow a master axis (slave drive)
ACurrRefMaster=0     ; copy current reference from axis A
```

## See also

- [CurrCmdSrc](CurrCmdSrc.md) — selects master-axis current command (value 3)
- [CurrCmdHTime](CurrCmdHTime.md) — `[1]` sets how long the slave follows the master
- [Current operation mode](00-overview.md) — overview of current-mode keywords
