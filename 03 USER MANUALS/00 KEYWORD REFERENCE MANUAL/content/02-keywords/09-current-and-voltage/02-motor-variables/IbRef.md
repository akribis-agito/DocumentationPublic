---
keyword: IbRef
summary: Read-only phase B current reference, in milliamperes (definition varies by motor type).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 28
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
# IbRef

Read-only phase B current reference, in milliamperes (definition varies by motor type).

## Overview

`IbRef` is the reference current of phase B, in milliamperes. Its exact derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). It is the reference counterpart of the measured phase B current [Ib](Ib.md); their difference is [IbErr](IbErr.md).

## How it works

| Motor type | Description |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | `IbRef` equals 0. |
| Three-phase motor (MotorType = 3 or 4) | `IbRef` equals the phase B result of the inverse Park transform of [IqRef](IqRef.md) and [IdRef](IdRef.md). It is used in abc-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | `IbRef` equals the phase B result after stepper-motor calculation and direction correction of [CurrRefCtrl](CurrRefCtrl.md). |

## Examples

```text
AIbRef              ; read phase B current reference (mA)
```

## See also

- [Ib](Ib.md) — measured phase B current
- [IbErr](IbErr.md) — phase B current error
- [IaRef](IaRef.md) — phase A current reference
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the derivation
