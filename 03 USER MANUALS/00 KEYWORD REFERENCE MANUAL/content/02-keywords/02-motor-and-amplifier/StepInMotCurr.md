---
keyword: StepInMotCurr
summary: Stepper phase current command, in mA, applied while the motor is in motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# StepInMotCurr

Stepper phase current command, in mA, applied while the motor is in motion.

## Overview

`StepInMotCurr` is the phase current command, in milliampere, applied to a stepper motor while it is **in motion** (the stepping current). It sets the torque available for moves; the companion keyword [StepInPosCurr](StepInPosCurr.md) sets the lower current held at standstill.

This keyword only applies when [MotorType](MotorType.md) is 6 (open-loop stepper) or 7 (closed-loop stepper). It is axis-scope and flash-saved, but may be changed while the motor is on and in motion. Set it within the motor's rated current to avoid overheating. Its maximum is the product's maximum current command; [StepInPosCurr](StepInPosCurr.md) is capped at half that.

## How it works

Each control cycle the firmware picks the stepper current from the motion status: if the axis is moving — [MotionStat](../10-motion/05-motion-status/MotionStat.md) is non-zero and **not** merely waiting for an input to start — it uses `StepInMotCurr`; otherwise it uses [StepInPosCurr](StepInPosCurr.md). The selected value becomes the current reference magnitude that scales the phase-current sine/cosine vectors:

$$IaRef = StepInMotCurr \cdot \sin\theta \qquad IbRef = StepInMotCurr \cdot \cos\theta$$

where the electrical angle θ comes from the commanded position (see [StepBits](StepBits.md)). A 2-phase current loop then drives Ia/Ib to these references. So `StepInMotCurr` directly sets the torque-producing current envelope during moves.

## Examples

```text
AStepInMotCurr=2000      ; 2000 mA phase current while moving
AStepInMotCurr          ; query the current value
```

## Changes between versions

In **v5 (central-i)** this parameter is a 32-bit floating-point value (`float32`) instead of the v4 integer; it is still expressed in mA. v5 is central-i only.

## See also

- [StepInPosCurr](StepInPosCurr.md) — stepper phase current at standstill (holding current)
- [MotorType](MotorType.md) — must be 6 or 7 (stepper) for this keyword to apply
- [StepBits](StepBits.md) — steps per electrical cycle
- [MotionStat](../10-motion/05-motion-status/MotionStat.md) — motion status that selects this current vs the standstill current
