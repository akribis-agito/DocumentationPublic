---
keyword: StepInPosCurr
summary: Stepper phase current command, in mA, held while the motor is at standstill.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 254
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
  - 0
  - 32000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepInPosCurr

Stepper phase current command, in mA, held while the motor is at standstill.

## Overview

`StepInPosCurr` is the phase current command, in milliampere, applied to a stepper motor while it is **at standstill** (the holding current). It is typically set lower than the in-motion current to reduce heating and power consumption while still holding position. The companion keyword [StepInMotCurr](StepInMotCurr.md) sets the higher current used during motion.

This keyword only applies when [MotorType](MotorType.md) is 6 (open-loop stepper) or 7 (closed-loop stepper). It is axis-scope and flash-saved, but may be changed while the motor is on and in motion. A value of 0 applies no holding current.

## Examples

```text
AStepInPosCurr=500       ; 500 mA holding current at standstill
AStepInPosCurr=0         ; no holding current
AStepInPosCurr          ; query the current value
```

## See also

- [StepInMotCurr](StepInMotCurr.md) — stepper phase current while in motion (stepping current)
- [MotorType](MotorType.md) — must be 6 or 7 (stepper) for this keyword to apply
- [StepBits](StepBits.md) — steps per electrical cycle
