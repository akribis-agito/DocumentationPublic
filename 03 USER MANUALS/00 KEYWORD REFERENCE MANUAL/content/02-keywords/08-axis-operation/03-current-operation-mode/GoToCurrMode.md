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

`GoToCurrMode` instructs the controller to enter current operation mode in a graceful manner. For other ways to enter current mode, see [OperationMode](../01-general-keywords/OperationMode.md).

## How it works

When the command is received the firmware performs the following, all with interrupts disabled so the transition is atomic:

1. **Already in current mode** — does nothing and replies OK.
2. **Member of a CNC (multi-axis) motion** — refuses the command and returns an error; you cannot enter current mode from a coordinated motion.
3. **Otherwise:**
   - If the axis is in motion, motion is ended immediately with the reason code "end / go-to-current" and the profiler sample time is stored.
   - [CurrCmdIndex](CurrCmdIndex.md) is reset to 1 (first table entry) and [CurrCmdCntr](CurrCmdCntr.md) is reset to 0.
   - [OperationMode](../01-general-keywords/OperationMode.md) is set to current control (value 1), the current position is recorded as the mode-switch position, and the in-target counter is cleared.

`GoToCurrMode` does **not** clear the [CurrCmdVal](CurrCmdVal.md), [CurrCmdSlope](CurrCmdSlope.md) or [CurrCmdHTime](CurrCmdHTime.md) tables — those keep their configured values so the sequence runs from entry 1 on each entry into the mode. This is the same preparation the firmware performs when current mode is entered automatically by a threshold condition.

## Examples

```text
AGoToCurrMode        ; gracefully switch to current operation mode
```

## See also

- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [CurrCmdSrc](CurrCmdSrc.md) — source of the current reference once in mode
- [Current operation mode](00-overview.md) — overview of current-mode behavior
