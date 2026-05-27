---
keyword: StepBits
summary: Sets the number of steps per electrical cycle for a stepper motor, controlling full-, half-, or micro-stepping.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 256
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
  - 2
  - 16
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepBits

Sets the number of steps per electrical cycle for a stepper motor, controlling full-, half-, or micro-stepping.

## Overview

`StepBits` defines the number of steps per electrical cycle for a stepper motor, which sets how finely each full-step excitation sequence is subdivided. Higher values give finer microstepping and smoother motion at the cost of less torque per step.

This keyword only applies when [MotorType](MotorType.md) is 6 (open-loop stepper) or 7 (closed-loop stepper). It feeds into the resolution and counts-per-revolution formulas described under [MotorType](MotorType.md), and works alongside [PolePrs](PolePrs.md) for closed-loop steppers. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

## How it works

The number of steps per electrical cycle is

$$
Steps\ per\ electrical\ cycle = 2^{StepBits}\ \lbrack step\ count\rbrack
$$

`StepBits = 2` and `StepBits = 3` correspond to full-stepping (4 steps per electrical cycle) and half-stepping (8 steps per electrical cycle) respectively. Microstepping is achieved by increasing `StepBits` above 2 (up to the maximum of 16).

## Examples

```text
AStepBits=2          ; full-stepping (4 steps per electrical cycle)
AStepBits=3          ; half-stepping (8 steps per electrical cycle)
AStepBits=8          ; microstepping (256 steps per electrical cycle)
AStepBits           ; query the current setting
```

## See also

- [MotorType](MotorType.md) — must be 6 or 7 (stepper) for this keyword to apply
- [PolePrs](PolePrs.md) — electrical cycles per revolution for closed-loop steppers
- [StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md) — stepper phase currents in motion / at standstill
