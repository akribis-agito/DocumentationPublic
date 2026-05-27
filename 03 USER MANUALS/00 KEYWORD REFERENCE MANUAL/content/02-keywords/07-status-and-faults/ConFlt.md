---
keyword: ConFlt
summary: Holds the controller error code that disabled the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 31
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ConFlt

Holds the controller error code that disabled the axis.

## Overview

`ConFlt` stores the error code that caused the axis to be disabled. A value of `0` means no fault is present; any positive value is a controller fault code (codes `1001` and above) — see [Controller error codes](../../04-error-codes/controller-error-codes.md) for the full list and their meanings.

`ConFlt` is an axis-scoped register that is not saved to flash, so it always reflects the live fault state of that axis. It works together with the diagnostic snapshot pair [ConFltSnapSrc](ConFltSnapSrc.md) / [ConFltSnapVal](ConFltSnapVal.md), which freeze selected parameter values at the moment a fault occurs, and with [MotorReason](MotorReason.md), which reports the broader category of why the axis was disabled.

## How it works

- Each time `ConFlt` takes a new positive value, that value is also appended to the controller [ErrLog](ErrLog.md).
- `ConFlt` is automatically cleared to `0` when the axis is re-enabled (`MotorOn=1`).
- You may write `0` to `ConFlt` to clear the fault status manually.
- You cannot write a positive value to simulate a fault. Negative values are writable but are reserved for internal use.

## Examples

```text
AConFlt             ; read the current fault code (0 = no fault)
AConFlt=0            ; clear the fault status
```

## See also

- [Controller error codes](../../04-error-codes/controller-error-codes.md) — meaning of each fault code
- [MotorReason](MotorReason.md) — why the axis was disabled (fault vs. command)
- [ConFltSnapSrc](ConFltSnapSrc.md) / [ConFltSnapVal](ConFltSnapVal.md) — parameter snapshot captured at fault
- [ErrLog](ErrLog.md) — log that positive ConFlt values are appended to
- [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) — re-enabling the axis clears ConFlt
