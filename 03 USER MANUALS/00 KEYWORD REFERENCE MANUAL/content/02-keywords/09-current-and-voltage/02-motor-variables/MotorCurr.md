---
keyword: MotorCurr
summary: Read-only total feedback current vector amplitude of the motor, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 8
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
# MotorCurr

Read-only total feedback current vector amplitude of the motor, in milliamperes.

## Overview

`MotorCurr` is the total feedback current vector amplitude of the motor, in milliamperes. It combines the measured phase currents into a single magnitude whose formula depends on the motor group selected by [MotorType](../../02-motor-and-amplifier/MotorType.md), then takes the sign convention described below. It provides a single value for monitoring the overall current the motor is drawing.

The value is computed each control-loop sample from the measured phase currents [Ia](Ia.md), [Ib](Ib.md) (and the derived phase C current `Ic = -(Ia + Ib)` for three-phase motors). The reported value is taken after the [CurrDir](CurrDir.md) inversion.

## How it works

The amplitude is built from the measured phase currents according to the motor group, and a sign is then attached:

| Motor group (MotorType) | Magnitude formula | Sign |
|----|----|----|
| Single-phase / brush motor (MotorType = 1 brush, 2 voice coil) | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \left\| \text{Ia} \right\|\ \lbrack mA\rbrack$ | Sign of [Ia](Ia.md) (value is `Ia` directly). |
| Three-phase brushless motor (MotorType = 3 linear, 4 rotary) | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \sqrt{\frac{2}{3}\left(\text{Ia}^{2} + \text{Ib}^{2} + \text{Ic}^{2}\right)}\ \lbrack mA\rbrack$ | Sign of [Iq](Iq.md): positive when $\text{Iq} \geq 0$, otherwise negative. |
| Two-phase stepper motor (MotorType = 6 open loop, 7 closed loop) | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \sqrt{\text{Ia}^{2} + \text{Ib}^{2}}\ \lbrack mA\rbrack$ | Always positive (a stepper has no current sign; direction is carried by the commutation angle). |

The three-phase magnitude $\sqrt{\frac{2}{3}(\text{Ia}^{2}+\text{Ib}^{2}+\text{Ic}^{2})}$ assumes sinusoidal commutation; for a balanced three-phase set it equals the dq-frame magnitude $\sqrt{\text{Iq}^{2}+\text{Id}^{2}}$ formed from [Iq](Iq.md)/[Id](Id.md).

**CurrDir inversion.** After the magnitude and sign are formed, the reported value is negated when [CurrDir](CurrDir.md) = 1 (flipped excitation direction) and passed through unchanged when CurrDir = 0.

The unsigned magnitude and its square are reused internally for the motor I²T power protection and for the stuck-motor and dynamic-braking logic; `MotorCurr` exposes the signed result.

## Examples

```text
AMotorCurr          ; read total feedback current amplitude (mA)
```

## See also

- [Ia](Ia.md), [Ib](Ib.md) — measured phase currents used to build the magnitude
- [Iq](Iq.md), [Id](Id.md) — measured dq-axis currents; Iq supplies the sign for three-phase motors
- [CurrDir](CurrDir.md) — excitation-direction flag that negates the reported value
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the formula
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — per-phase over-current protection on the same measured currents
