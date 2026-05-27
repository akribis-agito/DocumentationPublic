---
keyword: CurrCmdSrc
summary: Selects the source of the current reference in current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 330
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdSrc

Selects the source of the current reference in current mode.

## Overview

Under current operation mode, `CurrCmdSrc` sets the source of the current command (`CurrRef`). It is read by the mode-switching logic to decide how the current reference is generated and when the axis exits current mode (see [Current operation mode](00-overview.md)).

## How it works

| Value | Source |
|----|----|
| 0 | Analog current command input (defined by [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)) |
| 1 or 2 | User-defined values ([CurrCmdVal](CurrCmdVal.md)), each with specific timing ([CurrCmdHTime](CurrCmdHTime.md)) |
| 3 | Master axis current command (axis defined by [CurrRefMaster](CurrRefMaster.md)) |

## Examples

```text
CurrCmdSrc=1        ; use the user-defined CurrCmdVal table
CurrCmdSrc=3        ; follow a master axis (slave drive)
```

## See also

- [CurrCmdVal](CurrCmdVal.md) — user-defined current values (sources 1/2)
- [CurrRefMaster](CurrRefMaster.md) — master axis index (source 3)
- [Current operation mode](00-overview.md) — overall mode behavior
