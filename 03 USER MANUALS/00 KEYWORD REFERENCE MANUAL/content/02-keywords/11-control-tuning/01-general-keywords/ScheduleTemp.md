---
keyword: ScheduleTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 273
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20
  - 120
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleTemp

**Definition:**

ScheduleTemp is an array of temperature range for temperature-based gain scheduling (ScheduleMode = 8). ScheduleTemp must be monotonically increases along increasing array element.
