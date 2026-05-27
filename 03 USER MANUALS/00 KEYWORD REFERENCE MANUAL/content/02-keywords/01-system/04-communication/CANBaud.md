---
keyword: CANBaud
summary: CAN bus baud rate, selected from a fixed table.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 68
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
  - 1
  - 6
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANBaud

CAN bus baud rate, selected from a fixed table.

## Overview

`CANBaud` selects the CAN bus baud rate from a fixed table of six entries. The value is an index, not the rate itself. The default, `6`, corresponds to 1 Mbit/s. It is saved to flash and applied during start-up, so change it, [Save](../02-operation/Save.md), and [Reset](../02-operation/Reset.md) for it to take effect. **All nodes on a bus must use the same baud rate.**

| CANBaud | Baud rate [kbit/s] |
|---------|--------------------|
| 1 | 31.25 |
| 2 | 62.5 |
| 3 | 125 |
| 4 | 250 |
| 5 | 500 |
| 6 | 1000 |

## How it works

At start-up the firmware reads `CANBaud` and programs the CAN controller's bit-timing registers with the corresponding pre-computed configuration for that rate. If the stored value is outside the table, the firmware falls back to 1 Mbit/s (index 6). The rate that was actually applied is reported back through the identification data, so a host can confirm the link speed in use.

See the communication manual for more information.

## Examples

```text
ACANBaud=6           ; 1 Mbit/s (default), then Save and Reset
ACANBaud=4           ; 250 kbit/s
```

## See also

- [CANAddr](CANAddr.md) — CAN base address
- [CANDelay](CANDelay.md) — minimum spacing between CAN reply messages
- [RSBaud](RSBaud.md) — serial-port baud rate
