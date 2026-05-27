---
keyword: GoToForceMode
summary: Command to gracefully enter force operation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 575
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
# GoToForceMode

Command to gracefully enter force operation mode.

## Overview

`GoToForceMode` instructs the controller to enter force operation mode in a graceful manner. The preparation includes halting motion, clearing counters (such as [ForceCmdCntr](ForceCmdCntr.md) and [ForceCmdIndex](ForceCmdIndex.md)), and variable initialisation. For other ways to enter force mode, see [OperationMode](../01-general-keywords/OperationMode.md).

> **Note:** `GoToForceMode` cannot be used while the axis is in current operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1).

## Examples

```text
AGoToForceMode       ; gracefully switch to force operation mode
```

## See also

- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [ForceCmdSrc](ForceCmdSrc.md) — source of the force reference once in mode
- [Force operation mode](00-overview.md) — overview of force-mode behavior
