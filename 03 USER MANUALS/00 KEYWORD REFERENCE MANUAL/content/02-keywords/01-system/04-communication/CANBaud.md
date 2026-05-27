---
keyword: CANBaud
summary: CAN bus baud rate, selected from a fixed table.
availability:
  standalone:
  - v4
  - v5
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

`CANBaud` selects the CAN bus baud rate from the table below. The default, `6`, corresponds to 1 Mbit/s. It is saved to flash; all nodes on a bus must use the same baud rate.

| CANBaud | Baud rate [kbit/s] |
|---------|--------------------|
| 1 | 31.25 |
| 2 | 62.5 |
| 3 | 125 |
| 4 | 250 |
| 5 | 500 |
| 6 | 1000 |

See the communication manual for more information.

## Examples

```text
ACANBaud=6           ; 1 Mbit/s
```

## See also

- [CANAddr](CANAddr.md) — CAN base address
- [CANDelay](CANDelay.md) — CAN message delay
