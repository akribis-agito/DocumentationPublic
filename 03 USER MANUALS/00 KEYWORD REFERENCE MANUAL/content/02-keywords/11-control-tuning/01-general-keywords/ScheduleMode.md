---
keyword: ScheduleMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 260
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 11
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleMode

**Definition:**

ScheduleMode defines the gain scheduling algorithm to be used. The table below shows the available scheduling options.

**Note:**

1. Digital input (lower 16 bits of DInMode[x] = 14; upper 16 bits of DInMode[x] has the corresponding axis’ bit set; x is digital input number).
2. Manual assignment through communication
3. When the digital input is low, control set 1 is used.
4. When the digital input is high, control set 2 is used.
5. with axis previously not in active CNC motion, or
6. for at least ScheduleTime after axis was previously in other/non-linear CNC motion segment.
7. with axis previously not in active CNC motion, or
8. for at least ScheduleTime after axis was previously in other/non-linear CNC motion segment.
