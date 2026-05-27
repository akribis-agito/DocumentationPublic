---
keyword: DualLoopStat
availability:
  standalone: []
  central-i:
  - v5
can_code: 727
attributes:
  access: ro
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualLoopStat

**Definition:**

DualLoopStat denotes the status of dual-loop control.

| DualLoopOn | Descriptions                       |
|------------|------------------------------------|
| 0          | Default control is active          |
| 1          | Pseudo dual-loop control is active |
| 2          | Dual-loop control is active        |
