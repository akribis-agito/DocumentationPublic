---
keyword: IbRef
summary: Read-only phase B current reference, in milliamperes (definition varies by motor type).
availability:
- controller
- ci-master
can_code: 28
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# IbRef

Read-only phase B current reference, in milliamperes (definition varies by motor type).

## Overview

`IbRef` is the reference current of phase B, in milliamperes. Its exact derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). It is the reference counterpart of the measured phase B current [Ib](Ib.md); their difference is [IbErr](IbErr.md).

## How it works

Like [IaRef](IaRef.md), the phase B reference is the commutation projection of the direction-corrected scalar current reference $\text{CurrRef}_{dir}$, which is the limited current reference after the [CurrDir](CurrDir.md) sign is applied:

| Motor group (MotorType) | Phase B reference |
|----|----|
| Single-phase / brush motor (MotorType = 1, 2) | $\text{IbRef}\ = \ 0$ (only phase A is driven). |
| Three-phase brushless motor (MotorType = 3, 4) | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta - 120^\circ)$, where $\theta$ is the commutation angle — the phase B result of the inverse transform of $\text{IqRef} = \text{CurrRef}_{dir}$ and [IdRef](IdRef.md) (= 0). This commutation reference is computed every sample regardless of [ControlMode](ControlMode.md); the phase B error [IbErr](IbErr.md) it produces is only used as a control-loop input when current control runs in the abc domain ([ControlMode](ControlMode.md) bit 1 set). When current control is bypassed it is also applied directly as the phase B voltage command. |
| Two-phase stepper motor (MotorType = 6, 7) | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \cos(\theta_{step})$, where $\theta_{step}$ is the stepper electrical angle. The two stepper phases are driven in quadrature (sin/cos). |

`IbRef` is bounded by the controller's peak current rating, which is product-dependent (up to ±64000 mA on the highest-rated hardware). Its difference from the measured [Ib](Ib.md) gives [IbErr](IbErr.md), the input to the phase B current loop.

## Examples

```text
AIbRef              ; read phase B current reference (mA)
```

## See also

- [Ib](Ib.md) — measured phase B current
- [IbErr](IbErr.md) — phase B current error
- [IaRef](IaRef.md) — phase A current reference
- [IqRef](IqRef.md), [IdRef](IdRef.md) — dq references that this phase reference is the inverse transform of (brushless)
- [CurrDir](CurrDir.md) — direction correction applied before projection onto the phase
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the derivation
