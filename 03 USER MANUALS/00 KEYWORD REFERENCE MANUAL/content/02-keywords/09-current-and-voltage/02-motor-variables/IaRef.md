---
keyword: IaRef
summary: Read-only phase A current reference, in milliamperes (definition varies by motor type).
availability:
- controller
- ci-master
can_code: 27
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -16000
  - 16000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000
    - 64000
  agc300-et:
    range:
    - -4000
    - 4000
  agc301-et:
    range:
    - -4000
    - 4000
  agc301-et-bioxtreme:
    range:
    - -4000
    - 4000
  agd200-et-2d01:
    range:
    - -4000
    - 4000
  agd200-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d01:
    range:
    - -4000
    - 4000
  agd301-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d09:
    range:
    - -25500
    - 25500
  agd155-af-2a06:
    range:
    - -25500
    - 25500
  agd155-af-2a10:
    range:
    - -28500
    - 28500
  agd155-ec:
    range:
    - -25500
    - 25500
  agd155-ec-var34:
    range:
    - -28500
    - 28500
  agd155-ec-var34-3:
    range:
    - -42500
    - 42500
  agd156-ec:
    range:
    - -12726
    - 12726
  agd101-ec-34a:
    range:
    - -28280
    - 28280
  agd101-ec-17a:
    range:
    - -14140
    - 14140
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# IaRef

Read-only phase A current reference, in milliamperes (definition varies by motor type).

## Overview

`IaRef` is the reference current of phase A, in milliamperes. Its exact derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). It is the reference counterpart of the measured phase A current [Ia](Ia.md); their difference is [IaErr](IaErr.md).

## How it works

All three derivations start from the direction-corrected scalar current reference $\text{CurrRef}_{dir}$, which is the limited current reference after the [CurrDir](CurrDir.md) sign is applied. The commutation then projects it onto phase A:

| Motor group (MotorType) | Phase A reference |
|----|----|
| Single-phase / brush motor (MotorType = 1, 2) | $\text{IaRef}\ = \ \text{CurrRef}_{dir}$ (the whole current reference goes to phase A). |
| Three-phase brushless motor (MotorType = 3, 4) | $\text{IaRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta)$, where $\theta$ is the commutation angle. This is the inverse transform of the dq reference with $\text{IqRef} = \text{CurrRef}_{dir}$ and [IdRef](IdRef.md) = 0. It is the active reference when current control runs in the abc domain ([ControlMode](ControlMode.md) bit 1 set). |
| Two-phase stepper motor (MotorType = 6, 7) | $\text{IaRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta_{step})$, where $\theta_{step}$ is the stepper electrical angle (from the position reference in open loop, or from the integrated velocity reference in closed loop). |

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
