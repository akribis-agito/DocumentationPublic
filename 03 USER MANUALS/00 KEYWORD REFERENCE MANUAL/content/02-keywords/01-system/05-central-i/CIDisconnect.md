---
keyword: CIDisconnect
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 505
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIDisconnect

**Definition:**

CIDisconnect is a command that terminates the active Central-i link on the selected axis port. After this command the port stops real-time data exchange until a subsequent [CIConnect](CIConnect.md) is issued.

**See also:**

[CIConnect](CIConnect.md), [CIAutoConnect](CIAutoConnect.md), [CIStatus](CIStatus.md)
