---
keyword: CIGlobalStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 510
attributes:
  access: ro
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIGlobalStat

**Definition:**

CIGlobalStat is a read-only non-axis register that encodes the connection state of all Central-i ports. Each port uses two bits: the low bit is set when the port is connected, and the high bit indicates the port is operating in simulation (offline) mode. Reading this single value gives a system-wide overview without querying each axis individually.

**See also:**

[CIStatus](CIStatus.md), [CIConnect](CIConnect.md), [CIDisconnect](CIDisconnect.md)
