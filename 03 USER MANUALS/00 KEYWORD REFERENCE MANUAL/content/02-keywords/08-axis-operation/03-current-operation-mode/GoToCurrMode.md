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

### Walk-through: switch to current mode for a force test

Apply a small commanded current to verify mechanical/coil polarity or stick a known force on the actuator. Start from position mode with the motor on, hand off to current mode using the table source, and observe the result.

```text
AOperationMode            ; expect 3 (position) — start from a safe known state
AMotorOn                  ; expect 1 (servo on)
ACurrCmdSrc=1             ; use the user-defined CurrCmdVal table
ACurrCmdVal[1]=500        ; first table entry — 500 mA (adjust to your motor and rig)
ACurrCmdHTime[1]=2000     ; hold for 2000 ms
ACurrCmdVal[2]=0          ; second entry — back to zero
ACurrCmdHTime[2]=1000     ; hold for 1000 ms
ACurrCmdHTime[3]=0        ; HTime = 0 ends the sequence
AGoToCurrMode             ; graceful switch; CurrCmdIndex resets to 1, CurrCmdCntr to 0
                          ; ... observe the response ...
AMotorCurr                ; live motor current feedback (mA)
ACurrCmdCntr              ; ramp/hold counter for the active entry
                          ; ... when done ...
AGoToPosMode              ; bumpless return to position control
```

`GoToCurrMode` is rejected from CNC (multi-axis) motion and does nothing if the axis is already in current mode. It also leaves the `CurrCmdVal` / `CurrCmdSlope` / `CurrCmdHTime` tables intact — the sequence always restarts from entry 1.

## See also

- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [CurrCmdSrc](CurrCmdSrc.md) — source of the current reference once in mode
- [Current operation mode](00-overview.md) — overview of current-mode behavior
