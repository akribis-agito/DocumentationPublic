---
keyword: CIAutoConnect
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 500
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIAutoConnect

**Definition:**

CIAutoConnect is an axis-related parameter that, when enabled, causes the controller to automatically attempt to establish a Central-i connection on power-up or reset, without requiring an explicit [CIConnect](CIConnect.md) command from the host. The setting is saved to flash.

**See also:**

[CIConnect](CIConnect.md), [CIDisconnect](CIDisconnect.md), [CIStatus](CIStatus.md)
