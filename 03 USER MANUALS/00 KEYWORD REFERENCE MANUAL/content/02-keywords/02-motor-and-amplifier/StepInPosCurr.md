---
keyword: StepInPosCurr
summary: Stepper phase current command, in mA, held while the motor is at standstill.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# StepInPosCurr

Stepper phase current command, in mA, held while the motor is at standstill.

## Overview

`StepInPosCurr` is the phase current command, in milliampere, applied to a stepper motor while it is **at standstill** (the holding current). It is typically set lower than the in-motion current to reduce heating and power consumption while still holding position. The companion keyword [StepInMotCurr](StepInMotCurr.md) sets the higher current used during motion.

This keyword only applies when [MotorType](MotorType.md) is 6 (open-loop stepper) or 7 (closed-loop stepper). It is axis-scope and flash-saved, but may be changed while the motor is on and in motion. A value of 0 applies no holding current. Its maximum is half the product's maximum current command (the in-motion current [StepInMotCurr](StepInMotCurr.md) can use the full maximum).

## How it works

Each control cycle the firmware selects the stepper current from the motion status: when the axis is **not** moving ([MotionStat](../10-motion/05-motion-status/MotionStat.md) is zero, or it is only waiting for an input to start) it uses `StepInPosCurr`; while moving it uses [StepInMotCurr](StepInMotCurr.md). The selected value scales the phase-current vectors held against the present electrical angle θ:

$$IaRef = StepInPosCurr \cdot \sin\theta \qquad IbRef = StepInPosCurr \cdot \cos\theta$$

so the motor holds its position with reduced heating. A 2-phase current loop drives Ia/Ib to these references; with `StepInPosCurr = 0` no holding current flows and the motor can be back-driven.

## Examples

```text
AStepInPosCurr=500       ; 500 mA holding current at standstill
AStepInPosCurr=0         ; no holding current
AStepInPosCurr          ; query the current value
```

## Changes between versions

In **v5 (central-i)** this parameter is a 32-bit floating-point value (`float32`) instead of the v4 integer; it is still expressed in mA. v5 is central-i only.

## See also

- [StepInMotCurr](StepInMotCurr.md) — stepper phase current while in motion (stepping current)
- [MotorType](MotorType.md) — must be 6 or 7 (stepper) for this keyword to apply
- [StepBits](StepBits.md) — steps per electrical cycle
- [MotionStat](../10-motion/05-motion-status/MotionStat.md) — motion status that selects this current vs the in-motion current
