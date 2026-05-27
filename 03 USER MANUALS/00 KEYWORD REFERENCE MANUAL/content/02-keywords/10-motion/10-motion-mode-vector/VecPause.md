---
keyword: VecPause
summary: Pauses (1) or resumes (0) vector motion by ramping the resultant speed to/from zero.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 640
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecPause

Pauses (1) or resumes (0) vector motion by ramping the resultant speed to/from zero.

## Overview

`VecPause` temporarily holds vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) without ending the move. A value of `1` pauses the vector motion by setting the speed to 0, decelerating until stopping. A value of `0` continues the motion normally; if previously paused, it accelerates back up to [VecSpeed](VecSpeed.md). Unlike [StopVec](StopVec.md), which terminates the move, `VecPause` lets the same move resume from where it left off.

It is not saved to flash and takes its default value `0` at power-up.

## Examples

```text
AVecPause=1          ; pause vector motion (decelerate to a stop)
AVecPause=0          ; resume vector motion (accelerate back to VecSpeed)
```

## See also

- [StopVec](StopVec.md) — terminate (rather than pause) vector motion
- [VecSpeed](VecSpeed.md) — speed resumed to after a pause
- [VecMotionStat](VecMotionStat.md) — vector motion status
