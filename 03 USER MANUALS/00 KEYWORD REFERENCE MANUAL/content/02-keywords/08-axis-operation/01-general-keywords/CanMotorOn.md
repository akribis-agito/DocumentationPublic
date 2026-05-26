---
keyword: CanMotorOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 129
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CanMotorOn

**Definition:**

CanMotorOn is a command function that attempts to enable the motor on the axis. It performs the necessary pre-checks and, if all conditions are met, transitions the axis to the motor-on state. The result of the enable attempt can be read from CanMotorOnRes. It is an axis-related command and can be issued at any time.

**See also:**

[CanMotorOnRes](CanMotorOnRes.md), [MotorOn](MotorOn.md)
