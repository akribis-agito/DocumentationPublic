---
keyword: IdErr
summary: Read-only direct-axis current error (IdRef − Id), three-phase only, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 22
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# IdErr

Read-only direct-axis current error (IdRef − Id), three-phase only, in milliamperes.

## Overview

`IdErr` is the calculated current error in the direct (d) axis, in milliamperes — the difference between the reference [IdRef](IdRef.md) and the feedback [Id](Id.md). It is only applicable for three-phase motors ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4); otherwise `IdErr` is 0. It is used in three-phase dq0-domain current control.

## How it works

$$
IdErr\ \lbrack mA\rbrack\  = \ IdRef\ \lbrack mA\rbrack\  - \ Id\ \lbrack mA\rbrack
$$

## Examples

```text
AIdErr              ; read direct-axis current error (mA)
```

## See also

- [IdRef](IdRef.md) — direct-axis current reference
- [Id](Id.md) — direct-axis feedback current
- [IqErr](IqErr.md) — quadrature-axis current error
