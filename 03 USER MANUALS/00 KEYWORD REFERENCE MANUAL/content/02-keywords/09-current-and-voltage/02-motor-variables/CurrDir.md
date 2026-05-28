---
keyword: CurrDir
summary: Flips the direction of motor excitation (0 = normal, 1 = flipped).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 76
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrDir

Flips the direction of motor excitation (0 = normal, 1 = flipped).

## Overview

`CurrDir` configures the direction of motor excitation. It is normally used together with the encoder direction setting [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) to flip the axis into the desired physical direction. Because it changes how current is applied to the motor, it cannot be changed while the axis is in motion or the motor is on.

## How it works

`CurrDir` acts as a sign on the current path between the velocity/current loop and the commutation. After the current reference has been limited, the controller forms the direction-corrected reference used by the current loop:

$$
CurrRef_{dir}\ = \begin{cases} +CurrRef & CurrDir = 0 \\ -CurrRef & CurrDir = 1 \end{cases}
$$

This direction-corrected reference is the value the commutation then resolves into the phase references [IaRef](IaRef.md)/[IbRef](IbRef.md) (and [IqRef](IqRef.md) for brushless motors), so flipping `CurrDir` reverses the direction in which the commanded current drives the motor. The reported total current [MotorCurr](MotorCurr.md) is negated by the same flag, so it stays consistent with the commanded direction. The measured per-phase currents [Ia](Ia.md)/[Ib](Ib.md) and the dq currents [Iq](Iq.md)/[Id](Id.md) themselves are **not** negated by `CurrDir`; with `CurrDir` = 1 they appear with inverted sign relative to their references.

| CurrDir | Effect |
|---------|--------|
| 0 | Motor direction is not flipped; the direction-corrected reference equals `+CurrRef`. |
| 1 | Motor direction is flipped; the direction-corrected reference equals `−CurrRef`. |

## Examples

```text
ACurrDir=0           ; normal excitation direction
ACurrDir=1           ; flipped excitation direction
ACurrDir              ; read the current excitation-direction setting
```

## See also

- [EncDir / AuxEncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) — encoder direction, normally set together with CurrDir
- [MotorCurr](MotorCurr.md) — total current, negated by the same CurrDir flag
- [IaRef](IaRef.md), [IbRef](IbRef.md) — phase references derived from the direction-corrected current reference
- [ControlMode](ControlMode.md) — current/voltage control options
