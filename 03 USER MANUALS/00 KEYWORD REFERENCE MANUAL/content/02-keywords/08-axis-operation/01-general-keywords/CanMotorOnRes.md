---
keyword: CanMotorOnRes
summary: Result code from the last CanMotorOn enable attempt.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 413
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CanMotorOnRes

Result code from the last CanMotorOn enable attempt.

## Overview

`CanMotorOnRes` is a read-only status variable that holds the result code from the last [CanMotorOn](CanMotorOn.md) command. A zero value indicates the motor was enabled successfully; a non-zero value indicates the reason the enable attempt was rejected. It is axis-related and is not saved to flash.

## Examples

```text
ACanMotorOnRes      ; 0 = enabled successfully, non-zero = rejected
```

## See also

- [CanMotorOn](CanMotorOn.md) — command that produces this result
- [MotorOn](MotorOn.md) — enable/disable state of the motor
