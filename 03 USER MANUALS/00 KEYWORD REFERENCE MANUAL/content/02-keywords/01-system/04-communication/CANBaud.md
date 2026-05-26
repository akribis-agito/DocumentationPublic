---
keyword: CANBaud
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 68
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
  - 1
  - 6
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANBaud

**Definition:**

In CAN bus communication, CANBaud defines the baud rate of the CAN bus communication. The following table shows the values of CANBaud and corresponding baud rates.

| CANBaud value | Baud rate \[kHz\] |
|---------------|-------------------|
| 1             | 31.25             |
| 2             | 62.5              |
| 3             | 125               |
| 4             | 250               |
| 5             | 500               |
| 6             | 1000              |

For more information, please refer to communication manual.
