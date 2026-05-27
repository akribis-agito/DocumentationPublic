---
keyword: GoToPosMode
summary: Command to gracefully enter position operation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 336
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
# GoToPosMode

Command to gracefully enter position operation mode.

## Overview

`GoToPosMode` instructs the controller to enter position operation mode in a graceful manner. The position value (`Pos`) at the time the command is received is recorded in [ModeSwitchPos](ModeSwitchPos.md).

Through the [BeginOnToPos](BeginOnToPos.md) flag, the user may choose to immediately start a point-to-point motion to a target position (set by [RetractTarget](RetractTarget.md) or [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)) at a defined speed ([RetractSpeed](RetractSpeed.md)) upon receipt of the command. For other ways to enter position mode, see [OperationMode](../01-general-keywords/OperationMode.md).

> **Note:** `GoToPosMode` cannot be used while the axis is in velocity operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2).

## Examples

```text
AGoToPosMode         ; gracefully switch to position operation mode
AModeSwitchPos      ; read the recorded entry/exit positions
```

## See also

- [BeginOnToPos](BeginOnToPos.md) — optionally run a move on entry
- [ModeSwitchPos](ModeSwitchPos.md) — positions recorded at mode transitions
- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
