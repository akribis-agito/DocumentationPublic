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
  range:
  - 1
  - 2032
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANAddr

CAN base address of the controller node.

## Overview

`CANAddr` sets the CAN base address of the controller on a CAN bus. Set it to a **multiple of 16**, because each controller reserves a block of 16 consecutive CAN identifiers for its own use. It is saved to flash and applied during start-up, so change it, [Save](../02-operation/Save.md), and [Reset](../02-operation/Reset.md) to take effect. The allowed range runs up to the 11-bit CAN identifier limit, leaving room for the per-controller block of 16.

## How it works

At start-up the firmware combines the stored base address with the controller's hardware address DIP switches to form the **CAN initial address**:

$$
\text{initial address} = \text{CANAddr} + 16 \cdot (\text{DIP address})
$$

From that initial address the controller assigns its CAN mailboxes:

| Offset from initial address | Purpose |
|---|---|
| +0 | Receive (host → controller commands) |
| +1 | Reply (controller → host responses) |
| +15 | Push-status messages |

This is why the base must be a multiple of 16 and why each node occupies a 16-identifier block: the DIP switches step the block in units of 16 so several identical controllers can share one bus without overlapping. A dedicated "all-to-default" DIP setting overrides the stored value and forces the well-known default base of 64, which is useful for recovering a controller whose stored address is unknown.

The CAN identifier is 11 bits wide, so addresses must stay within that range; the configurable maximum reserves the top block of 16. See the communication manual for the complete addressing scheme.

## Examples

```text
ACANAddr=64          ; set the CAN base address (a multiple of 16), then Save and Reset
```

## See also

- [CANBaud](CANBaud.md) — CAN bus baud rate
- [CANDelay](CANDelay.md) — minimum spacing between CAN reply messages
- [ChainAddress](ChainAddress.md) — address in a serial daisy-chain topology
- [RemoteCANSend](RemoteCANSend.md) — send a CAN write/read to another node
