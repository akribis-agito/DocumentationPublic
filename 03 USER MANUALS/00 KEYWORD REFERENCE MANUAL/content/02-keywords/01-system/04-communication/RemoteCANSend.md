---
keyword: RemoteCANSend
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 443
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANSend

**Definition:**

RemoteCANSend is a command that transmits a CAN write message to the remote node specified by [RemoteCANAdd](RemoteCANAdd.md), setting the parameter identified by [RemoteCANCCC](RemoteCANCCC.md) to the value in [RemoteCANVal](RemoteCANVal.md). It can be executed during motion.

**See also:**

[RemoteCANAdd](RemoteCANAdd.md), [RemoteCANCCC](RemoteCANCCC.md), [RemoteCANVal](RemoteCANVal.md)
