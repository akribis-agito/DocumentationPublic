---
keyword: CIConnect
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 504
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
# CIConnect

**Definition:**

CIConnect is a command that initiates a Central-i link connection on the selected axis port. It must be executed after the port is configured (device type, link configuration) and before any real-time synchronised data exchange can take place.

**See also:**

[CIAutoConnect](CIAutoConnect.md), [CIDisconnect](CIDisconnect.md), [CIDeviceType](CIDeviceType.md), [CIStatus](CIStatus.md)
