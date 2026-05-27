---
keyword: PStatPort
summary: Selects the communication port used for parameter-statistics streaming.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 481
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
  - 3
  default: 1
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatPort

Selects the communication port used for parameter-statistics streaming.

## Overview

`PStatPort` selects the communication port over which program-status data is transmitted while streaming is enabled by [PStatOn](PStatOn.md). It works with [PStatParams](PStatParams.md) (what is sent) and [PStatInterval](PStatInterval.md) (how often). It is a non-axis parameter and is saved to flash (default `1`).

## How it works

The value selects which physical link the background streamer uses:

| Value | Port |
|---|---|
| 1 | Serial port (mini connector) |
| 2 | Serial port (RJ45 connector) |
| 3 | CAN |

On a serial port, status streaming yields to outgoing command replies so it does not interfere with normal request/response traffic; on CAN, the batch is sent as status messages. Pick a port whose available bandwidth suits your chosen [PStatInterval](PStatInterval.md) and number of [PStatParams](PStatParams.md) entries.

## Examples

```text
APStatPort=1         ; stream over the serial port (mini connector)
APStatPort=3         ; stream over CAN
```

## See also

- [PStatOn](PStatOn.md) — enable/disable periodic statistics streaming
- [PStatParams](PStatParams.md) — parameters included in each transmission
- [PStatInterval](PStatInterval.md) — interval between transmissions
