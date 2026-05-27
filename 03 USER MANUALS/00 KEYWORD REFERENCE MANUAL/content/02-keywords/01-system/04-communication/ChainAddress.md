---
keyword: ChainAddress
summary: CAN address used when the controller runs in a daisy-chain topology.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 159
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
  - -1
  - 8
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ChainAddress

CAN address used when the controller runs in a daisy-chain topology.

## Overview

`ChainAddress` assigns this controller an address on a daisy-chained serial bus, so several controllers can share one multi-drop serial line (the RJ45 serial port) and each respond only to commands aimed at it. This is the controller's "extended protocol" / multi-drop addressing mode. The default of `-1` disables the feature — the controller is not part of a chain and responds to every command on its port. It is saved to flash and is latched once at start-up, so changes take effect only after [Save](../02-operation/Save.md) and [Reset](../02-operation/Reset.md).

## How it works

When `ChainAddress` is not `-1`, each command on the serial bus must begin with a single address digit. The controller compares that leading digit against its own `ChainAddress`:

| Leading address | Behaviour |
|---|---|
| Equal to this controller's `ChainAddress` (0–7) | The command is for this unit: the address digit is stripped and the rest of the command is executed normally, with a reply sent. |
| 8 (quiet broadcast) | Every unit on the chain executes the command, but **none** replies (avoids reply collisions on the shared bus). |
| Any other valid address (0–7) | The command is for a different unit and is ignored by this one. |

A bare carriage return after the address (no command) is treated as a do-nothing keep-alive. The valid range is therefore `-1` (disabled) and `0`–`8`, where `8` is reserved as the quiet broadcast address. The address actually in use is reported through the identification data.

Because the address is read only at start-up, you cannot move a controller to a new chain position on the fly — you must Save and Reset.

## Examples

```text
AChainAddress=1      ; this unit answers to address "1"; Save and Reset to apply
AChainAddress=-1     ; disable chain addressing (respond to all commands)
```

## See also

- [CANAddr](CANAddr.md) — CAN base address (CAN-bus addressing, separate from the serial chain)
- [RSBaud](RSBaud.md) — serial-port baud rate used by the chain
- [CANBaud](CANBaud.md) — CAN bus baud rate
