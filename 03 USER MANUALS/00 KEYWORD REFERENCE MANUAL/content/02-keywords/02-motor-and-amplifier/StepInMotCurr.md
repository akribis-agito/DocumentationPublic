---
keyword: StepInMotCurr
summary: Stepper phase current command, in mA, applied while the motor is in motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 255
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 50
  - 64000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepInMotCurr

Stepper phase current command, in mA, applied while the motor is in motion.

## Overview

`StepInMotCurr` is the phase current command, in milliampere, applied to a stepper motor while it is **in motion** (the stepping current). It sets the torque available for moves; the companion keyword [StepInPosCurr](StepInPosCurr.md) sets the lower current held at standstill.

This keyword only applies when [MotorType](MotorType.md) is 6 (open-loop stepper) or 7 (closed-loop stepper). It is axis-scope and flash-saved, but may be changed while the motor is on and in motion. Set it within the motor's rated current to avoid overheating.

## Examples

```text
AStepInMotCurr=2000      ; 2000 mA phase current while moving
AStepInMotCurr          ; query the current value
```

## See also

- [StepInPosCurr](StepInPosCurr.md) — stepper phase current at standstill (holding current)
- [MotorType](MotorType.md) — must be 6 or 7 (stepper) for this keyword to apply
- [StepBits](StepBits.md) — steps per electrical cycle
