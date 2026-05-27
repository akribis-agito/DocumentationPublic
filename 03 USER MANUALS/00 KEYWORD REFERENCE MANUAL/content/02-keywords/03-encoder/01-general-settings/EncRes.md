---
keyword: EncRes
summary: Encoder resolution; counts per magnetic pitch (linear) or per revolution (rotary).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 56
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncRes

Encoder resolution; counts per magnetic pitch (linear) or per revolution (rotary).

## Overview

`EncRes` defines the encoder resolution, interpreted according to the motor type ([MotorType](../../02-motor-and-amplifier/MotorType.md)):

- For linear motors, `EncRes` is the number of encoder counts per magnetic pitch (North-North).
- For rotary motors, `EncRes` is the number of encoder counts per revolution.
- For voice coils, `EncRes` has no effect and can be set to any value.

Together with the pole pairs ([PolePrs](../../02-motor-and-amplifier/PolePrs.md)), `EncRes` is used to calculate encoder counts per pole pair for commutation. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

> [!warning]
> `PolePrs` and `EncRes` are used to calculate encoder counts per pole pair for commutation. Incorrect values will cause the commutation process to fail or pass incorrectly, which may result in unexpected behaviour such as high motor current or a runaway condition. This can cause severe damage to the controller, motor, or any other system parts connected to the motor.

## How it works

`EncRes` is a scaling constant used by several internal calculations rather than a quantity that is read back:

- **Commutation electrical cycle.** The firmware computes the counts per electrical cycle as $EncRes / PolePrs$ (`SpecialFuncs.c:3860`). This defines how the measured position maps onto the electrical angle for sinusoidal commutation, so an incorrect `EncRes` mis-aligns the commutation angle (see the warning above). For a stepper, the steps-per-count factor is derived as $PolePrs \times electricalCycle / EncRes$ (`SpecialFuncs.c:3926`).
- **Speed-unit conversion (BEMF feed-forward and reporting).** `EncRes` converts internal counts/s into engineering speed (`SpecialFuncs.c:6169` onward):
  - Linear motor: $magneticPitch[\text{m}] / EncRes$ — counts/s to m/s (here `EncRes` is counts per magnetic pitch).
  - Rotary motor / DC brush: $60 / EncRes$ — counts/s to rpm (here `EncRes` is counts per revolution).
  - Voice coil: $1 / EncRes$; `EncRes` has no physical commutation role and may be left at any value.

`EncRes` is the *raw* encoder resolution; per-axis unit display scaling for [Pos](../../10-motion/01-kinematics-status/Pos.md) and its derivatives is handled separately by [UsrUnits](UsrUnits-AuxUsrUnits.md).

## Examples

```text
AEncRes=10000        ; 10000 counts per revolution (rotary) or per pitch (linear)
AEncRes             ; query the configured encoder resolution
```

## See also

- [MotorType](../../02-motor-and-amplifier/MotorType.md) — determines how `EncRes` is interpreted
- [PolePrs](../../02-motor-and-amplifier/PolePrs.md) — pole pairs, combined with `EncRes` for commutation
- [EncType](EncType-AuxEncType.md) — encoder feedback type
- [UsrUnits](UsrUnits-AuxUsrUnits.md) — user-unit display scaling applied on top of the raw counts
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position measured in encoder counts
