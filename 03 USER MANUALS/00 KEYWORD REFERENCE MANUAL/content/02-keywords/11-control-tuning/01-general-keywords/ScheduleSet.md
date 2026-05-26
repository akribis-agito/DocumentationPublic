---
keyword: ScheduleSet
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 261
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
  - 1
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleSet

**Definition:**

ScheduleSet represents the tuning gains set number that is currently in use. The value is reset to 1 upon power cycle or when gain scheduling is disabled (ScheduleMode = 0).

ScheduleSet will vary depending on the gain scheduling algorithm, defined by ScheduleMode (and relevant scheduling keywords). ScheduleSet can be also set manually by the user, by entering manual gain scheduling mode (ScheduleMode = 1).
