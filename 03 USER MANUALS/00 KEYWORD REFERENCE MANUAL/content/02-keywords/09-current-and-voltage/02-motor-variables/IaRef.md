---
keyword: IaRef
summary: Read-only phase A current reference, in milliamperes (definition varies by motor type).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# IaRef

Read-only phase A current reference, in milliamperes (definition varies by motor type).

## Overview

`IaRef` is the reference current of phase A, in milliamperes. Its exact derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). It is the reference counterpart of the measured phase A current [Ia](Ia.md); their difference is [IaErr](IaErr.md).

## How it works

All three derivations start from the direction-corrected scalar current reference `CurrRefFinal`, which is the limited current reference after the [CurrDir](CurrDir.md) sign is applied. The commutation then projects it onto phase A:

| Motor group (MotorType) | Phase A reference |
|----|----|
| Single-phase / brush motor (MotorType = 1, 2) | $IaRef\ = \ CurrRefFinal$ (the whole current reference goes to phase A). |
| Three-phase brushless motor (MotorType = 3, 4) | $IaRef\ = \ CurrRefFinal \cdot \sin(\theta)$, where $\theta$ is the commutation angle. This is the inverse transform of the dq reference with [IqRef](IqRef.md) = `CurrRefFinal` and [IdRef](IdRef.md) = 0. It is the active reference when current control runs in the abc domain ([ControlMode](ControlMode.md) bit 1 set). |
| Two-phase stepper motor (MotorType = 6, 7) | $IaRef\ = \ CurrRefFinal \cdot \sin(\theta_{step})$, where $\theta_{step}$ is the stepper electrical angle (from `PosRef` in open loop, or from the integrated velocity reference in closed loop). |

`IaRef` is bounded to ±64000 mA. Its difference from the measured [Ia](Ia.md) gives [IaErr](IaErr.md), the input to the phase A current loop.

## Examples

```text
AIaRef              ; read phase A current reference (mA)
```

## See also

- [Ia](Ia.md) — measured phase A current
- [IaErr](IaErr.md) — phase A current error
- [IbRef](IbRef.md) — phase B current reference
- [IqRef](IqRef.md), [IdRef](IdRef.md) — dq references that this phase reference is the inverse transform of (brushless)
- [CurrDir](CurrDir.md) — direction correction applied before projection onto the phase
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the derivation
