---
keyword: CurrCmdCntr
summary: Time elapsed in current mode or in the active CurrCmdVal entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 334
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdCntr

Time elapsed in current mode or in the active CurrCmdVal entry.

## Overview

`CurrCmdCntr` is the time elapsed, in milliseconds, that drives the timing-table logic of current operation mode. Its meaning depends on [CurrCmdSrc](CurrCmdSrc.md):

1. If `CurrCmdSrc` = 0 or 3 (analog input or slave drive): time elapsed under current operation mode.
2. If `CurrCmdSrc` = 1 or 2 (user-defined table): time elapsed under the existing [CurrCmdVal](CurrCmdVal.md) array entry. This resets to 0 when switching to the next `CurrCmdVal` entry.

`CurrCmdCntr` resets to 0 upon receipt of the [GoToCurrMode](GoToCurrMode.md) command, upon automatic condition switching, or upon a digital input switching to current operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it to any initial value and start the timer from there.

> **Note:** The user can overwrite `CurrCmdCntr` at any time while in current operation mode.

## Examples

```text
ACurrCmdCntr        ; read elapsed time (ms)
ACurrCmdCntr=0       ; restart the timer
```

## See also

- [CurrCmdHTime](CurrCmdHTime.md) — holding time compared against this counter
- [CurrCmdIndex](CurrCmdIndex.md) — active table entry
- [GoToCurrMode](GoToCurrMode.md) — resets this counter on entry
