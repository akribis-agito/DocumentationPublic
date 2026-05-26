---
keyword: RSBaud
summary: Serial (RS232/USB) baud rate per port, selected from a fixed table.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 79
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 5
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
---
# RSBaud

Serial (RS232/USB) baud rate per port, selected from a fixed table.

## Overview

`RSBaud` selects the baud rate for the controller's serial ports. Each array element configures one port:

- `RSBaud[1]` — micro-USB port
- `RSBaud[2]` — RJ45 port

The value maps to a baud rate as follows (default `4` = 115200 bit/s). It is saved to flash.

| RSBaud | Baud rate [bit/s] |
|--------|-------------------|
| 1 | 9600 |
| 2 | 19200 |
| 3 | 38400 |
| 4 | 115200 |

See the communication manual for more information.

## Examples

```text
RSBaud[1]=4         ; set the micro-USB port to 115200 bit/s
```

## See also

- [CANBaud](CANBaud.md) — CAN bus baud rate
- [EthernetPort](EthernetPort.md) — Ethernet port
