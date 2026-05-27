---
keyword: PolePrs
summary: Number of motor magnet pole pairs, interpreted according to the motor type, for correct feedback and commutation.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 54
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
  - 50
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
---
# PolePrs

Number of motor magnet pole pairs, interpreted according to the motor type, for correct feedback and commutation.

## Overview

`PolePrs` defines the number of magnet pole pairs (one pole pair = one north plus one south pole). Its exact meaning depends on the configured [MotorType](MotorType.md). Setting the correct value is essential for feedback and commutation to work normally and to prevent possible damage.

This keyword only applies when [MotorType](MotorType.md) is 3 (linear DC brushless), 4 (rotary DC brushless), or 7 (closed-loop stepper). For linear brushless motors (type 3) the controller automatically forces `PolePrs = 1`. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion. Changing `PolePrs` on a brushless motor re-arms commutation (the [StatReg](../07-status-and-faults/StatReg.md) commutation bit is cleared until the axis re-phases).

## How it works

For brushless motors, `PolePrs` together with [EncRes](../03-encoder/01-general-settings/EncRes.md) defines the **electrical cycle** used for commutation. The controller pre-computes the counts per electrical cycle as

$$Counts\ per\ electrical\ cycle = \frac{EncRes}{PolePrs}$$

and converts a feedback position into an electrical angle by multiplying its position-within-cycle by $2\pi / (EncRes/PolePrs)$. That angle drives the inverse-Park transformation that produces the three phase voltages. A wrong `PolePrs` therefore mis-scales the electrical angle, so commutation fails and the motor can run away — set it correctly before enabling.

For closed-loop steppers, `PolePrs` (electrical cycles per revolution) and [StepBits](StepBits.md) define the *steps-per-count* factor used to convert the velocity reference into stepping increments: $StepsPerCount = PolePrs \cdot 2^{StepBits} / EncRes$.

`PolePrs` is interpreted differently per motor type:

`PolePrs` is interpreted differently per motor type:

| MotorType               | PolePrs descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 (Linear DC brushless) | PolePrs is the number of pole pairs per magnetic period. In short, user must always set PolePrs = 1 for linear brushless motor.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 4 (Rotary DC brushless) | PolePrs is the number of pole pairs per mechanical revolution of rotary motor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 7 (Stepper closed loop) | PolePrs is the number of electrical cycles (1 electrical cycle = 1 set of full-step excitation sequence) per mechanical revolution of 2-phase stepper motor. In 1 electrical cycle, there are total of 4 full steps. Normally, stepper motor manufacturers specify the resolution in terms of physical angle per one full step. This means in 1 revolution, the number of electrical cycles is $$PolePrs = \ \ \frac{360\lbrack physical\ deg\rbrack}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$ |

## Examples

```text
APolePrs=1           ; linear DC brushless motor (must be 1)
APolePrs=4           ; rotary brushless: 4 pole pairs per revolution
APolePrs            ; query the configured pole-pair count
```

## See also

- [MotorType](MotorType.md) — determines how PolePrs is interpreted
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — encoder resolution, used with PolePrs to form the electrical cycle
- [StepBits](StepBits.md) — steps per electrical cycle for stepper motors
- [StatReg](../07-status-and-faults/StatReg.md) — commutation status bit (cleared when PolePrs changes on a brushless motor)
