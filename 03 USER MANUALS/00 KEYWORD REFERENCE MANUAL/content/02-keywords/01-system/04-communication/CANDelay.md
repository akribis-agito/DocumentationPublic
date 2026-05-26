---
keyword: CANDelay
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 222
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANDelay

**Definition:**

In CAN bus communication, CANDelay sets the number of samples to delay the messages by. This delay does not affect the baud rate.

For more information, please refer to communication manual.
