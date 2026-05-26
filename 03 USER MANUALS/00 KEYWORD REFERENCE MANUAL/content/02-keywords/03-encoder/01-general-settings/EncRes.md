---
keyword: EncRes
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 56
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncRes

**Definition:**

For linear motors, EncRes represents the number of encoder counts per magnetic pitch (North-North).

For rotary motors, EncRes represents the number of encoder counts per revolution.

For voice coils, EncRes has no effect and can be set to any value.

**Warning:**

PolePrs and EncRes are used to calculate encoder counts per pole pair for commutation. Incorrect values will result in the commutation process failing or passing incorrectly. As a result, user might experience unexpected behaviour such as high motor current or runaway condition. This can result in severe damage to the controller, motor or any other system parts connected to the motor.
