---
keyword: VecDecel
summary: Vector deceleration rate (user units/s^2) ramping the resultant velocity down to rest.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 637
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecDecel

Vector deceleration rate (user units/s^2) ramping the resultant velocity down to rest.

## Overview

`VecDecel` sets the deceleration rate for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second squared. It defines how quickly the resultant (vector) velocity ramps down from [VecSpeed](VecSpeed.md) to rest at the end of a controlled stop, applying to the path as a whole. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

`VecDecel` is the controlled (normal) deceleration; [VecEmrgDec](VecEmrgDec.md) is the faster emergency rate used on a stop or fault.

## Examples

```text
VecDecel=100000     ; vector deceleration (user units/s^2, default)
VecDecel?           ; read the current value
```

## See also

- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
- [VecEmrgDec](VecEmrgDec.md) — emergency deceleration rate
