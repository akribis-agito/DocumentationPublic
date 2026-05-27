---
keyword: Ia
summary: Read-only measured phase A current, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 9
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
# Ia

Read-only measured phase A current, in milliamperes.

## Overview

`Ia` reports the measured current of phase A, in milliamperes. Phase A is defined by the connection scheme in the hardware reference guide. It is the feedback counterpart of the phase A reference [IaRef](IaRef.md); their difference is the phase A current error [IaErr](IaErr.md).

## How it works

Each control-loop sample the firmware reads the phase A current-sense ADC, converts the raw count to milliamperes with the hardware current-sensing factor, and subtracts the per-axis zero-current calibration offset measured at start-up:

$$
Ia\ \lbrack mA\rbrack\ = \ (ADC_{A}\ \times\ currentSensingFactor)\ -\ IaZeroCalibration
$$

The current-sensing factor is fixed by the current-range hardware (so a given ADC count maps to a fixed mA value). For three-phase brushless motors only two phases are measured directly and the third is derived from Kirchhoff's law as `Ic = -(Ia + Ib)`; depending on the hardware variant `Ia` or `Ib` may be the derived one. `Ia` is then used to form the dq currents [Iq](Iq.md)/[Id](Id.md) and the magnitude [MotorCurr](MotorCurr.md), and it is checked against the per-phase over-current protection [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md).

## Examples

```text
AIa                 ; read measured phase A current (mA)
```

## See also

- [IaRef](IaRef.md) — phase A current reference
- [IaErr](IaErr.md) — phase A current error (IaRef − Ia)
- [Ib](Ib.md) — measured phase B current
- [MotorCurr](MotorCurr.md) — total feedback current amplitude built from Ia/Ib/Ic
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — per-phase over-current limit checked against Ia
