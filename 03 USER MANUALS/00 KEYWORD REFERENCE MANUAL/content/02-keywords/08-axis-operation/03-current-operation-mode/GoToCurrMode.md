---
keyword: GoToCurrMode
summary: Command to gracefully enter current operation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 335
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GoToCurrMode

Command to gracefully enter current operation mode.

## Overview

`GoToCurrMode` instructs the controller to enter current operation mode in a graceful manner. The preparation includes halting motion, clearing counters (such as [CurrCmdCntr](CurrCmdCntr.md) and [CurrCmdIndex](CurrCmdIndex.md)), and variable initialisation. For other ways to enter current mode, see [OperationMode](../01-general-keywords/OperationMode.md).

## Examples

```text
AGoToCurrMode        ; gracefully switch to current operation mode
```

## See also

- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [CurrCmdSrc](CurrCmdSrc.md) — source of the current reference once in mode
- [Current operation mode](00-overview.md) — overview of current-mode behavior
