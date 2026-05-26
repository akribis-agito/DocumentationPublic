---
keyword: RSBaud
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 79
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 5
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
---
# RSBaud

**Definition:**

In RS232/USB communication, RSBaud defines the baud rate as listed below.

| RSBaud value | Baud rate \[bit/s\] |
|--------------|---------------------|
| 1            | 9600                |
| 2            | 19200               |
| 3            | 38400               |
| 4            | 115200              |

RSBaud\[1\] defines the baud rate of micro-USB port. RSBaud\[2\] defines the baud rate of RJ45 port.

For more information, please refer to communication manual.
