---
keyword: JerkMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 722
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# JerkMode

**Condition:**

JerkMode is only used when MotionMode = 1 or 2 (point-to-point motion).

**Definition:**

JerkMode is used to define point-to-point motion profiler’s order, as shown below.

| JerkMode | Motion profiler’s order | Related keywords |
|----|----|----|
| 0 | 2 (Infinite jerk) | Speed, Accel, Decel, Jerk |
| 1 | 3 (Infinite snap) | Speed, Accel, Decel, Jerk, JerkInAcc, JerkInDec |
