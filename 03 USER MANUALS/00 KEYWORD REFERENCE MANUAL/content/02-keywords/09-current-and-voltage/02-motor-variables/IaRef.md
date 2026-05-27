---
keyword: IaRef
summary: Read-only phase A current reference, in milliamperes (definition varies by motor type).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 27
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
# IaRef

Read-only phase A current reference, in milliamperes (definition varies by motor type).

## Overview

`IaRef` is the reference current of phase A, in milliamperes. Its exact derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). It is the reference counterpart of the measured phase A current [Ia](Ia.md); their difference is [IaErr](IaErr.md).

## How it works

| Motor type | Description |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | `IaRef` equals [CurrRefCtrl](CurrRefCtrl.md) after direction correction. |
| Three-phase motor (MotorType = 3 or 4) | `IaRef` equals the phase A result of the inverse Park transform of [IqRef](IqRef.md) and [IdRef](IdRef.md). It is used in abc-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | `IaRef` equals the phase A result after stepper-motor calculation and direction correction of [CurrRefCtrl](CurrRefCtrl.md). |

## Examples

```text
IaRef?              ; read phase A current reference (mA)
```

## See also

- [Ia](Ia.md) — measured phase A current
- [IaErr](IaErr.md) — phase A current error
- [IbRef](IbRef.md) — phase B current reference
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the derivation
