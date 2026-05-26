---
keyword: RemoteCANVal
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 442
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANVal

**Definition:**

RemoteCANVal holds the value that will be written to the remote controller's parameter (identified by [RemoteCANCCC](RemoteCANCCC.md)) when [RemoteCANSend](RemoteCANSend.md) is executed. It is a transient register (not saved to flash).

**See also:**

[RemoteCANAdd](RemoteCANAdd.md), [RemoteCANCCC](RemoteCANCCC.md), [RemoteCANSend](RemoteCANSend.md)
