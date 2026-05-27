---
keyword: ScheduleGains
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 274
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 7
    data_type: float32
    range: null
---
# ScheduleGains

**Definition:**

ScheduleGains displays the active gains in use by the controller.

Each ScheduleGains array element corresponds to a type of gain, as shown.

| Index | Description                     |
|-------|---------------------------------|
| 1     | Position loop proportional gain |
| 2     | Acceleration feedforward gain   |
| 3     | Velocity loop proportional gain |
| 4     | Velocity loop integral gain     |
| 5     | Velocity feedforward gain       |
| 6     | Position loop integral gain     |

In case of no gain scheduling (ScheduleMode = 0), ScheduleGains values equal to first array elements of respective schedulable gain keywords. For example, ScheduleGains\[2\] = AccFFW\[1\].
