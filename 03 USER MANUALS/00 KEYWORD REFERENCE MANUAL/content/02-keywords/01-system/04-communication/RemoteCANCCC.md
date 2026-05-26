---
keyword: RemoteCANCCC
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 441
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
  - -2147483648
  - 2147483647
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANCCC

**Definition:**

RemoteCANCCC holds the CAN Command Code (CCC) — the parameter identifier — that will be written to the remote controller when [RemoteCANSend](RemoteCANSend.md) is executed. Together with [RemoteCANAdd](RemoteCANAdd.md) and [RemoteCANVal](RemoteCANVal.md) it defines the complete remote write transaction.

**See also:**

[RemoteCANAdd](RemoteCANAdd.md), [RemoteCANVal](RemoteCANVal.md), [RemoteCANSend](RemoteCANSend.md)
