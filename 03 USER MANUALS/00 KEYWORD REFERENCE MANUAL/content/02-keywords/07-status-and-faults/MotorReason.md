---
keyword: MotorReason
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 498
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
  - 4
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorReason

**Definition:**

MotorReason stores the reason on why the axis was disabled. MotorReason is reset to 0 upon motor on.

| Value | Description |
|---|---|
| 0 | **NONE** |
| 1 | **CONFLT** A controller fault triggered caused the axis to be disabled. Check ConFlt for more details. |
| 2 | **Digital Input** A command was sent via a digital input to disable the axis. |
| 3 | **User Program (IDE+)** A command was sent via the user program to disable the axis. |
| 4 | **Communication** A command was sent via the communication channel to disable the axis. |
