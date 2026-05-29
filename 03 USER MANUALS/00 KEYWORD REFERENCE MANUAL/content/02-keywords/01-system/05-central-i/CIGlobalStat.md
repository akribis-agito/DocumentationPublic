---
keyword: CIGlobalStat
summary: Read-only register encoding the connection state of all Central-i ports.
availability:
  standalone:
  - v4
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

`CIGlobalStat` is a read-only, non-axis register that summarises the connection state of every Central-i port in one value, so the host can poll system-wide status without reading [CIStatus](CIStatus.md) on each axis. Each port occupies **two bits**, packed by port number:

- the **low** (even) bit of the pair is set when the port is connected;
- the **high** (odd) bit of the pair is set when that axis is in *simulation* mode ([MotorType](../../02-motor-and-amplifier/MotorType.md) set to simulation, value 5).

## How it works

For port `n` (counting from 0), the connected bit is bit `2n` and the simulation bit is bit `2n+1`:

| Port | Connected bit | Simulation bit | Connected mask |
|------|---------------|----------------|----------------|
| 0 | 0 | 1 | 0x00000001 |
| 1 | 2 | 3 | 0x00000004 |
| 2 | 4 | 5 | 0x00000010 |
| 3 | 6 | 7 | 0x00000040 |
| n | 2n | 2n+1 | `1 << (2n)` |

The firmware sets the connected bit when a port reaches the synchronised state (via [CIConnect](CIConnect.md) or [CIAutoConnect](CIAutoConnect.md)) and clears it on reset/[CIDisconnect](CIDisconnect.md). The simulation bit is governed independently: it is set when that axis's [MotorType](../../02-motor-and-amplifier/MotorType.md) is set to simulation (value 5) and cleared otherwise; it is updated when `MotorType` is written and does not depend on [CIConnect](CIConnect.md)/[CIDisconnect](CIDisconnect.md). A port whose pair reads `01` (binary) is a live link; `11` is a connected simulation axis; `00` is disconnected.

To test one port, mask with its connected bit — for example port 1 is connected when `(CIGlobalStat & 0x4)` is non-zero.

## Examples

```text
ACIGlobalStat       ; system-wide Central-i connection state
```

In a user program, check whether port 0 is connected by masking with `0x1`, and whether it is a simulation by masking with `0x2`.

## See also

- [CIStatus](CIStatus.md) — detailed per-axis link state and error codes
- [CIConnect](CIConnect.md) / [CIDisconnect](CIDisconnect.md) — set/clear the connected bit
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — value 5 (simulation) drives the per-port simulation bit
