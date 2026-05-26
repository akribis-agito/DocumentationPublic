---
keyword: ScheduleVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 263
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 1300000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleVel

**Definition:**

ScheduleVel is an array of velocity range for velocity-based gain scheduling (ScheduleMode = 4 or 9). ScheduleVel must be monotonically increases along increasing array element.
