---
keyword: Abort
summary: Immediately stops motion using the emergency deceleration rate (EmrgDec).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 133
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
# Abort

Immediately stops motion using the emergency deceleration rate (`EmrgDec`).

## Overview

`Abort` is a command that stops axis motion as quickly as possible, decelerating at the emergency rate [EmrgDec](../03-kinematics-configuration/EmrgDec.md) rather than the normal [Decel](../03-kinematics-configuration/Decel.md) rate used by [Stop](Stop.md). It can be issued at any time during motion and is typically used for safety or fault recovery. It is an axis-related command function.

## Examples

```text
AAbort               ; emergency-stop the axis
```

## See also

- [Stop](Stop.md) — controlled stop using the normal `Decel` rate
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency deceleration rate used by `Abort`
