---
keyword: ScheduleTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 262
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleTime

**Definition:**

ScheduleTime defines the timing of gain scheduling, in milliseconds, for time-based scheduling (ScheduleMode = 2, 6, 7, 11 or 12).
