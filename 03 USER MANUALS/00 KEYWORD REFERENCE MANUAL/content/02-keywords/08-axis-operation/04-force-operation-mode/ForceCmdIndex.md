---
keyword: ForceCmdIndex
summary: Index of the active ForceCmdVal / ForceCmdHTime table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 573
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
# ForceCmdIndex

Index of the active ForceCmdVal / ForceCmdHTime table entry.

## Overview

`ForceCmdIndex` is the index of the [ForceCmdVal](ForceCmdVal.md) and [ForceCmdHTime](ForceCmdHTime.md) values currently in use. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2 (user-defined table).

`ForceCmdIndex` resets to 1 upon receipt of the [GoToForceMode](GoToForceMode.md) command, upon automatic condition switching, or upon a digital input switching to force operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it so the reference table starts from the desired `ForceCmdVal`/`ForceCmdHTime` pair.

> **Note:** The user can overwrite `ForceCmdIndex` at any time while in force operation mode. This causes an immediate switch of the `ForceCmdVal` in use, without resetting the [ForceCmdCntr](ForceCmdCntr.md) timer.

## Examples

```text
ForceCmdIndex?      ; read the active table entry
ForceCmdIndex=3     ; jump to the third entry
```

## See also

- [ForceCmdVal](ForceCmdVal.md) — table of force values
- [ForceCmdHTime](ForceCmdHTime.md) — holding times per entry
- [ForceCmdCntr](ForceCmdCntr.md) — timer for the active entry
