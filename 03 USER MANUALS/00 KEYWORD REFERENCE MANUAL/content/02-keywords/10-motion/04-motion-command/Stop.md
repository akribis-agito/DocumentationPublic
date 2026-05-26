---
keyword: Stop
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 132
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
# Stop

**Definition:**

Stop is a command that decelerates the axis to rest using the normal Decel rate and then halts motion. Unlike Abort, Stop performs a controlled deceleration. It is an axis-related command function that can be issued at any time, including during motion.

**See also:**

[Abort](Abort.md), [Decel](../03-kinematics-configuration/Decel.md), [EmrgDec](../03-kinematics-configuration/EmrgDec.md)
