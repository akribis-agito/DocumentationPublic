---
keyword: CurrCmdIndex
summary: Index of the active CurrCmdVal / CurrCmdHTime table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 333
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 20
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdIndex

Index of the active CurrCmdVal / CurrCmdHTime table entry.

## Overview

`CurrCmdIndex` is the index of the [CurrCmdVal](CurrCmdVal.md) and [CurrCmdHTime](CurrCmdHTime.md) values currently in use. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 1 or 2 (user-defined table).

`CurrCmdIndex` resets to 1 upon receipt of the [GoToCurrMode](GoToCurrMode.md) command, upon automatic condition switching, or upon a digital input switching to current operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it so the reference table starts from the desired `CurrCmdVal`/`CurrCmdHTime` pair.

> **Note:** The user can overwrite `CurrCmdIndex` at any time while in current operation mode. This causes an immediate switch of the `CurrCmdVal` in use, without resetting the [CurrCmdCntr](CurrCmdCntr.md) timer.

## Examples

```text
ACurrCmdIndex       ; read the active table entry
ACurrCmdIndex=3      ; jump to the third entry
```

## See also

- [CurrCmdVal](CurrCmdVal.md) — table of current values
- [CurrCmdHTime](CurrCmdHTime.md) — holding times per entry
- [CurrCmdCntr](CurrCmdCntr.md) — timer for the active entry
