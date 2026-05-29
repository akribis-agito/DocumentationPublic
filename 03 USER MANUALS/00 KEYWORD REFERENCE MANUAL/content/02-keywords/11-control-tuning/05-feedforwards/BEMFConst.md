---
keyword: BEMFConst
summary: Motor back-EMF constant used to compute the speed-proportional voltage feedforward.
availability:
  standalone: []
  central-i:
  - v5
can_code: 847
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 10000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BEMFConst

Motor back-EMF constant used to compute the speed-proportional voltage feedforward.

> Available from central-i v5.

## Overview

`BEMFConst` is the motor's back-EMF (electromotive force) constant. A moving motor generates a voltage proportional to its speed; `BEMFConst` is the proportionality between that generated voltage and speed, taken from the motor data sheet. The controller uses it to compute the back-EMF term of the voltage feedforward — the speed-proportional voltage that must be supplied so the current loop does not have to overcome the back-EMF on its own. The back-EMF term appears on the quadrature axis and is part of [VqFFW](VqFFW.md).

`BEMFConst` only contributes when voltage feedforward is enabled by [VoltageFFWOn](VoltageFFWOn.md) and its level [BEMFFFWLevel](BEMFFFWLevel.md) is non-zero. With the default value 0 there is no back-EMF feedforward.

## How it works

Each control cycle the back-EMF feedforward voltage is `BEMFConst`, scaled by [BEMFFFWLevel](BEMFFFWLevel.md) (a percentage), multiplied by the actual motor speed ([Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md)). The controller converts the speed from internal counts-per-second into the units in which the constant is specified and converts the result into the internal voltage (PWM) units of the current loop, so the value you enter is the physical motor constant in its data-sheet units.

The expected units of `BEMFConst` depend on the motor type ([MotorType](../../../02-keywords/02-motor-and-amplifier/MotorType.md)):

| Motor type | Units of BEMFConst |
|------------|--------------------|
| Rotary brushless and DC brush | Volt per RPM |
| Linear brushless | Volt per (m/s) |
| Voice coil | Volt per (m/s) |

For three-phase (rotary and linear brushless) motors the data-sheet back-EMF constant is usually given as a line-to-line value; the controller divides it internally by √3 to obtain the per-phase value, so enter the line-to-line constant as published.

The valid range is 0 to 10000 (in the units above) and the default is 0. `BEMFConst` is a flash-backed parameter and may be set with the motor on or in motion.

## Examples

```text
ABEMFConst=0.05      ; set back-EMF constant (e.g. V/RPM for a rotary motor)
ABEMFConst           ; read back the configured constant
```

## See also

- [BEMFFFWLevel](BEMFFFWLevel.md) — percentage level applied to the back-EMF feedforward term
- [VqFFW](VqFFW.md) — q-axis feedforward output that carries the back-EMF term
- [VoltageFFWOn](VoltageFFWOn.md) — master enable for voltage feedforward
- [MotorType](../../../02-keywords/02-motor-and-amplifier/MotorType.md) — selects the motor type that determines the units of BEMFConst
- [Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md) — actual motor speed the back-EMF term is proportional to
