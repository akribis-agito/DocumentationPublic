---
keyword: Id
summary: Read-only direct-axis feedback current after Park transform (three-phase only), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 11
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
overrides: {}
---
# Id

Read-only direct-axis feedback current after Park transform (three-phase only), in milliamperes.

## Overview

`Id` is the feedback current in the direct (d) axis after the Park transform, in milliamperes. It is only applicable for three-phase motors ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4); otherwise `Id` is 0. It is the direct-axis counterpart of [Iq](Iq.md) and is regulated against its reference [IdRef](IdRef.md) in dq0-domain current control, producing the error [IdErr](IdErr.md).

## Examples

```text
Id?                 ; read direct-axis feedback current (mA)
```

## See also

- [IdRef](IdRef.md) — direct-axis current reference
- [IdErr](IdErr.md) — direct-axis current error
- [Iq](Iq.md) — quadrature-axis feedback current
