---
keyword: StopVec
summary: Command that stops coordinated vector motion, decelerating all member axes with VecEmrgDec.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 645
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopVec

Command that stops coordinated vector motion, decelerating all member axes with VecEmrgDec.

## Overview

`StopVec` is a command that stops coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). All participating axes (selected by [VecMemberAxes](VecMemberAxes.md)) decelerate together using the emergency deceleration rate [VecEmrgDec](VecEmrgDec.md) and come to rest, keeping the vector path coordinated as it stops. It is an axis-related command function that can be issued at any time, including during motion. For a continuous arc (see [VecNumCircles](VecNumCircles.md) = 0), `StopVec` is the means of ending the motion.

## Examples

```text
StopVec=0           ; stop the active vector motion
```

## See also

- [VecEmrgDec](VecEmrgDec.md) — deceleration rate used to stop
- [VecMotionStat](VecMotionStat.md) — reports the resulting motion state
- [VecPause](VecPause.md) — temporarily pause (vs. stop) vector motion
