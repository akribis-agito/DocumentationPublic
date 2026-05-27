---
keyword: CanMotorOn
summary: Command that attempts to enable the motor after running pre-checks.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 129
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
# CanMotorOn

Command that attempts to enable the motor after running pre-checks.

## Overview

`CanMotorOn` is a command function that attempts to enable the motor on the axis. It performs the necessary pre-checks and, if all conditions are met, transitions the axis to the motor-on state. It is an axis-related command and can be issued at any time.

Unlike writing directly to [MotorOn](MotorOn.md), this command reports why an enable attempt was rejected: the result of the last attempt can be read from [CanMotorOnRes](CanMotorOnRes.md).

## Examples

```text
ACanMotorOn          ; attempt to enable the motor
ACanMotorOnRes      ; read the result of the attempt
```

## See also

- [CanMotorOnRes](CanMotorOnRes.md) — result code of the last enable attempt
- [MotorOn](MotorOn.md) — enable/disable state of the motor
