---
keyword: MotorReason
summary: Read-only code reporting why the axis was last disabled.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

| Value | Description |
|---|---|
| 0 | **NONE** |
| 1 | **CONFLT** A controller fault triggered caused the axis to be disabled. Check ConFlt for more details. |
| 2 | **Digital Input** A command was sent via a digital input to disable the axis. |
| 3 | **User Program (IDE+)** A command was sent via the user program to disable the axis. |
| 4 | **Communication** A command was sent via the communication channel to disable the axis. |

## Examples

```text
AMotorReason        ; 1 = controller fault, 2 = digital input, 3 = user program, 4 = communication
```

## See also

- [ConFlt](ConFlt.md) — the specific fault code when MotorReason is 1 (CONFLT)
- [ConFltSnapVal](ConFltSnapVal.md) — parameter snapshot captured at the fault
- [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) — enabling the axis resets MotorReason to 0
