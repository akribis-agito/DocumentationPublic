---
keyword: Ib
summary: Read-only measured phase B current, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 10
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
# Ib

Read-only measured phase B current, in milliamperes.

## Overview

`Ib` reports the measured current of phase B, in milliamperes. Phase B is defined by the connection scheme in the hardware reference guide. It is the feedback counterpart of the phase B reference [IbRef](IbRef.md); their difference is the phase B current error [IbErr](IbErr.md).

## How it works

Each control-loop sample the firmware reads the phase B current-sense ADC, converts the raw count to milliamperes with the hardware current-sensing factor, and subtracts the per-axis zero-current calibration offset measured at start-up:

$$
Ib\ \lbrack mA\rbrack\ = \ (ADC_{B}\ \times\ k_{sense})\ -\ I_{0,B}
$$

where $k_{sense}$ is the hardware current-sensing factor and $I_{0,B}$ is the per-axis zero-current offset. For three-phase brushless motors only two of the three phases are sampled directly; the remaining phase is derived from $Ia + Ib + Ic = 0$ (for example $Ic = -(Ia + Ib)$), so on some hardware variants `Ib` is the derived phase rather than a measured one. For single-phase (brush / voice-coil) motors only phase A carries current and `Ib` is held at 0. `Ib` is then used to form the dq currents [Iq](Iq.md)/[Id](Id.md) and the magnitude [MotorCurr](MotorCurr.md), and it is checked against the per-phase over-current protection [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md).

## Examples

```text
AIb                 ; read measured phase B current (mA)
```

## See also

- [IbRef](IbRef.md) — phase B current reference
- [IbErr](IbErr.md) — phase B current error (IbRef − Ib)
- [Ia](Ia.md) — measured phase A current
- [MotorCurr](MotorCurr.md) — total feedback current amplitude built from Ia/Ib/Ic
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — per-phase over-current limit checked against Ib
