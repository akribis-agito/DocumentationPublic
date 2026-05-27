---
keyword: MotorOn
summary: Enables or disables the motor, and reports the servo on/off status.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 130
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorOn

Enables or disables the motor, and reports the servo on/off status.

## Overview

`MotorOn` is used to enable/disable the motor (by writing) or report the servo status (by reading). `MotorOn = 0` disables the motor; `MotorOn = 1` enables it. When the motor is disabled, no power is applied to the motor and none of the control loops are active.

The motor can also be disabled internally by a controller fault (see [ConFlt](../../../02-keywords/07-status-and-faults/ConFlt.md) and [Controller error codes](../../../04-error-codes/controller-error-codes.md)). When the axis is enabled, `ConFlt` is cleared; if the fault state remains, the fault is retriggered and the axis is disabled again. To enable the motor with pre-checks and a reportable result, use [CanMotorOn](CanMotorOn.md) / [CanMotorOnRes](CanMotorOnRes.md).

Some keywords are only writable or callable when the axis is disabled — refer to each keyword's attribute table (`ok_motor_on`) for details.

## Examples

```text
MotorOn=1           ; enable the motor
MotorOn=0           ; disable the motor
MotorOn?            ; read servo status (0 = off, 1 = on)
```

## See also

- [CanMotorOn](CanMotorOn.md) — enable the motor with pre-checks
- [CanMotorOnRes](CanMotorOnRes.md) — result of the last enable attempt
- [ConFlt](../../../02-keywords/07-status-and-faults/ConFlt.md) — controller fault register that can disable the motor
