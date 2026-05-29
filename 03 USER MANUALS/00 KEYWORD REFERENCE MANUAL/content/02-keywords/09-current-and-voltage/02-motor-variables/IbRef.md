---
keyword: IbRef
summary: Read-only phase B current reference, in milliamperes (definition varies by motor type).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
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
| Three-phase brushless motor (MotorType = 3, 4) | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta - 120^\circ)$, where $\theta$ is the commutation angle — the phase B result of the inverse transform of $\text{IqRef} = \text{CurrRef}_{dir}$ and [IdRef](IdRef.md) (= 0). Active when current control runs in the abc domain ([ControlMode](ControlMode.md) bit 1 set). |
| Two-phase stepper motor (MotorType = 6, 7) | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \cos(\theta_{step})$, where $\theta_{step}$ is the stepper electrical angle. The two stepper phases are driven in quadrature (sin/cos). |

`IbRef` is bounded to ±64000 mA. Its difference from the measured [Ib](Ib.md) gives [IbErr](IbErr.md), the input to the phase B current loop.

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
