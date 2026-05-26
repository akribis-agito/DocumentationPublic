---
keyword: CIGlobalStat
summary: Read-only register encoding the connection state of all Central-i ports.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
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

Read-only register encoding the connection state of all Central-i ports.

## Overview

`CIGlobalStat` is a read-only, non-axis register that summarises the connection state of every Central-i port in one value. Each port occupies two bits:

- the **low** bit is set when the port is connected;
- the **high** bit indicates the port is operating in simulation (offline) mode.

Reading this single value gives a system-wide overview without querying each axis with [CIStatus](CIStatus.md).

## Examples

```text
CIGlobalStat?       ; system-wide Central-i connection state
```

## See also

- [CIStatus](CIStatus.md) — detailed per-axis link state
- [CIConnect](CIConnect.md) / [CIDisconnect](CIDisconnect.md) — change the connection
