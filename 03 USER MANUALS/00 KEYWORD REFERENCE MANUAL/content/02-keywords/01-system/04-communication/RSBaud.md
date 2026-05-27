---
keyword: RSBaud
summary: Serial (RS232/USB) baud rate per port, selected from a fixed table.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    range:
    - 1
    - 4
---
# RSBaud

Serial (RS232/USB) baud rate per port, selected from a fixed table.

## Overview

`RSBaud` selects the baud rate for the controller's serial ports, one array element per port. (The array is dimensioned so the usable indices start at `[1]`; index `[0]` is not used.)

- `RSBaud[1]` — micro-USB port
- `RSBaud[2]` — RJ45 port

The value is an index into the table below, not the rate itself. The default, `4`, is 115200 bit/s. It is saved to flash and applied during start-up, so change it, [Save](../02-operation/Save.md), and [Reset](../02-operation/Reset.md) for it to take effect.

| RSBaud | Baud rate [bit/s] |
|--------|-------------------|
| 1 | 9600 |
| 2 | 19200 |
| 3 | 38400 |
| 4 | 115200 |
| 5 | 57600 |

Note that index `5` (57600 bit/s) is out of numeric order — it was appended after the original four rates.

## How it works

Each port is configured independently at start-up from its `RSBaud` element. The firmware looks up the index in the table above and programs the serial peripheral's baud-rate divisor accordingly. If the stored value is outside the table, the firmware falls back to 115200 bit/s. The two endpoints of a serial link must use the same baud rate.

See the communication manual for more information.

## Changes between versions

On central-i (v5) the `57600` entry (index `5`) is **not available** — the valid range is `1`–`4` only. On standalone/v4 the full range `1`–`5` (including `5` = 57600) is supported.

## Examples

```text
ARSBaud[1]=4         ; set the micro-USB port to 115200 bit/s
ARSBaud[2]=1         ; set the RJ45 port to 9600 bit/s
```

## See also

- [CANBaud](CANBaud.md) — CAN bus baud rate
- [ChainAddress](ChainAddress.md) — multi-drop serial addressing that runs over this port
- [EthernetPort](EthernetPort.md) — Ethernet TCP port
