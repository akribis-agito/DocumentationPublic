---
keyword: SendToCntrlr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 484
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# SendToCntrlr

**Definition:**

SendToCntrlr is a partially-implemented function that routes a parameter write to another controller over the communication bus. It accepts an array of values that encode the target controller address, parameter code, and data payload. Because it is flagged PARTIAL, full functionality may depend on the specific firmware build.

**See also:**

[RemoteCANSend](RemoteCANSend.md), [CANAddr](CANAddr.md)
