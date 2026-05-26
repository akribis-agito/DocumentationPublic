---
keyword: StopVec
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

**Definition:**

StopVec is a command that stops coordinated vector motion. All participating axes decelerate together using VecEmrgDec and come to rest. It is an axis-related command function that can be issued at any time, including during motion.

**See also:**

[VecEmrgDec](VecEmrgDec.md), [VecMotionStat](VecMotionStat.md)
