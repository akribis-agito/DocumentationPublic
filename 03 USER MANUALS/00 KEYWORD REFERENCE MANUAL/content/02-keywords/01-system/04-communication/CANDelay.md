---
keyword: CANDelay
summary: Delay, in samples, applied to CAN messages.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 222
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
  - 0
  - 1000
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANDelay

Delay, in samples, applied to CAN messages.

## Overview

`CANDelay` sets the number of samples by which CAN messages are delayed. This affects only message timing — it does **not** change the baud rate ([CANBaud](CANBaud.md)). It is saved to flash. See the communication manual for guidance on when a delay is needed.

## Examples

```text
CANDelay=6          ; delay CAN messages by 6 samples
```

## See also

- [CANAddr](CANAddr.md) — CAN base address
- [CANBaud](CANBaud.md) — CAN bus baud rate
