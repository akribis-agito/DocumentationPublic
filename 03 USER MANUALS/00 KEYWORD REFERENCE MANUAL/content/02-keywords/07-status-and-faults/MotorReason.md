---
keyword: MotorReason
summary: Read-only code reporting why the axis was last disabled.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 498
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorReason

Read-only code reporting why the axis was last disabled.

## Overview

`MotorReason` records why the axis was disabled, so you can distinguish a fault-driven shutdown from a deliberate disable command. It is an axis-scoped, read-only code that is not saved to flash. It is reset to `0` (NONE) whenever the axis is enabled (`MotorOn=1`).

When `MotorReason` reports a controller fault (value `1`), read [ConFlt](ConFlt.md) for the specific fault code and the [ConFltSnapVal](ConFltSnapVal.md) snapshot for the captured system state.

## How it works

`MotorReason` holds the reason for the **last** disable. It is set at the moment the axis goes from enabled to disabled, and reset to `0` (NONE) whenever the axis is enabled (`MotorOn=1`), so while the axis is running it reads `0`.

| Value | Internal name | Description |
|---|---|---|
| 0 | `MOTOR_OFF_REASON_NONE` | **NONE** — no disable recorded, or the axis is enabled. |
| 1 | `MOTOR_OFF_REASON_FLT` | **CONFLT** — a controller fault disabled the axis. Read [ConFlt](ConFlt.md) for the specific code. |
| 2 | `MOTOR_OFF_REASON_IO` | **Digital Input** — a digital input configured to disable the axis was activated. |
| 3 | `MOTOR_OFF_REASON_UPROG` | **User Program (IDE+)** — a `MotorOn=0` command came from the user program. |
| 4 | `MOTOR_OFF_REASON_COMM` | **Communication** — a `MotorOn=0` command came over the communication channel. |

The fault reason (`1`) is set specifically when the axis transitions to disabled while a [ConFlt](ConFlt.md) is present, which distinguishes a fault-driven shutdown from a deliberate disable command (reasons `2`–`4`).

Note: the array default reported in the parameter table is `-1`, but the firmware initialises and resets the live value to `0` (NONE); in normal operation you will only see values `0`–`4`.

## Examples

```text
AMotorReason        ; 1 = controller fault, 2 = digital input, 3 = user program, 4 = communication
```

## See also

- [ConFlt](ConFlt.md) — the specific fault code when MotorReason is 1 (CONFLT)
- [ConFltSnapVal](ConFltSnapVal.md) — parameter snapshot captured at the fault
- [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) — enabling the axis resets MotorReason to 0
