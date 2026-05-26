---
keyword: SchedulePos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 264
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
  - -2147483648
  - 2147483647
  default: 2147483647
  scaling: 1.0
  implemented: final
overrides: {}
---
# SchedulePos

**Definition:**

SchedulePos is an array of position range for position-based gain scheduling (ScheduleMode = 5 or 10). SchedulePos must be monotonically increases along increasing array element.
