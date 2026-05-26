---
keyword: RemoteCANAdd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 440
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
  - 2047
  default: 128
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANAdd

**Definition:**

RemoteCANAdd specifies the CAN node address of a remote controller to which a CAN message will be sent when [RemoteCANSend](RemoteCANSend.md) is executed. It is saved to flash and works together with [RemoteCANCCC](RemoteCANCCC.md) and [RemoteCANVal](RemoteCANVal.md) to form the outgoing message.

**See also:**

[RemoteCANCCC](RemoteCANCCC.md), [RemoteCANVal](RemoteCANVal.md), [RemoteCANSend](RemoteCANSend.md)
