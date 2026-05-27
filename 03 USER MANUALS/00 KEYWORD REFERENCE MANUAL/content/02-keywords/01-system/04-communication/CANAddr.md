---
keyword: CANAddr
summary: CAN base address of the controller node.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 67
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
  range: null
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANAddr

CAN base address of the controller node.

## Overview

`CANAddr` sets the CAN base address of the controller on a CAN bus. Set it to a **multiple of 16**, because each controller reserves 16 addresses for internal purposes.

DIP switches add an offset to the base address to form the *CAN initial address*; the initial address wraps around if it overflows past 2032. From the initial address:

- the controller **receives** messages at `initial address + 2·N`
- the controller **replies** at `initial address + 2·N + 1`

where N = 0, 1, 2, …. `CANAddr` is saved to flash. See the communication manual for full addressing details.

## Examples

```text
ACANAddr=64          ; set the CAN base address (a multiple of 16)
```

## See also

- [CANBaud](CANBaud.md) — CAN bus baud rate
- [CANDelay](CANDelay.md) — CAN message delay
- [ChainAddress](ChainAddress.md) — address in a daisy-chain topology
