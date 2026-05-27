---
keyword: ForceCmdCntr
summary: Time elapsed in force mode or in the active ForceCmdVal entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 574
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
# ForceCmdCntr

Time elapsed in force mode or in the active ForceCmdVal entry.

## Overview

`ForceCmdCntr` is the time elapsed, in milliseconds, that drives the timing-table logic of force operation mode. Its meaning depends on [ForceCmdSrc](ForceCmdSrc.md):

1. If `ForceCmdSrc` = 0 (analog input): time elapsed under force operation mode.
2. If `ForceCmdSrc` = 1 or 2 (user-defined table): time elapsed under the existing [ForceCmdVal](ForceCmdVal.md) array entry. This resets to 0 when switching to the next `ForceCmdVal` entry.

`ForceCmdCntr` resets to 0 upon receipt of the [GoToForceMode](GoToForceMode.md) command, upon automatic condition switching, or upon a digital input switching to force operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it to any initial value and start the timer from there.

> **Note:** The user can overwrite `ForceCmdCntr` at any time while in force operation mode.

## Examples

```text
ForceCmdCntr?       ; read elapsed time (ms)
ForceCmdCntr=0      ; restart the timer
```

## See also

- [ForceCmdHTime](ForceCmdHTime.md) — holding time compared against this counter
- [ForceCmdIndex](ForceCmdIndex.md) — active table entry
- [GoToForceMode](GoToForceMode.md) — resets this counter on entry
