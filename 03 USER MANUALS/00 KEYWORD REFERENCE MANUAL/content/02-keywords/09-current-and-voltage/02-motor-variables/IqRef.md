---
keyword: IqRef
summary: Read-only quadrature-axis current reference (definition varies by motor type), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 30
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IqRef

Read-only quadrature-axis current reference (definition varies by motor type), in milliamperes.

## Overview

`IqRef` is the reference current of the quadrature (q) axis, in milliamperes. Its derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). For three-phase motors it is the torque-producing reference, derived from [CurrRefCtrl](CurrRefCtrl.md) after direction correction and regulated against the feedback [Iq](Iq.md).

## How it works

| Motor type | Description |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | `IqRef` equals [IaRef](IaRef.md). |
| Three-phase motor (MotorType = 3 or 4) | `IqRef` equals [CurrRefCtrl](CurrRefCtrl.md) after direction correction. It is used in dq0-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | `IqRef` equals 0. |

## Examples

```text
AIqRef              ; read quadrature-axis current reference (mA)
```

## See also

- [Iq](Iq.md) — quadrature-axis feedback current
- [IqErr](IqErr.md) — quadrature-axis current error
- [IdRef](IdRef.md) — direct-axis current reference
- [CurrRefCtrl](CurrRefCtrl.md) — loop-side current reference
