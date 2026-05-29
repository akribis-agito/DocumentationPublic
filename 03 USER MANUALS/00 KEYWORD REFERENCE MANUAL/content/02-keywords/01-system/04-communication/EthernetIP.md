---
keyword: EthernetIP
summary: Controller IP address, stored one octet per array element.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 600
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EthernetIP

Controller IP address, stored one octet per array element.

## Overview

`EthernetIP` holds the controller's IPv4 address as four octets, one per array element, each in the range 0–255. (The array is dimensioned so the usable indices start at `[1]`; index `[0]` is not used.) Element `[1]` is the most significant octet and `[4]` the least significant. It is saved to flash and read during start-up, so set the octets, [Save](../02-operation/Save.md), and [Reset](../02-operation/Reset.md) for the new address to take effect.

For example, the address `192.168.0.10` is stored as:

| Element | Value |
|---------|-------|
| EthernetIP[1] | 192 |
| EthernetIP[2] | 168 |
| EthernetIP[3] | 0 |
| EthernetIP[4] | 10 |

## How it works

The firmware reassembles the four octets into the dotted-quad address used by the network stack when Ethernet starts up. Set all four elements to define a valid address before saving; a partially-written address (some octets left at their previous values) will produce an unintended address.

If all four octets are left at 0 (the never-configured state), the controller falls back to a built-in default address of `172.1.1.101`, so an out-of-the-box controller is still reachable on the network.

The controller's hardware-address DIP setting is added to the last octet when forming the address. On standalone controllers this offset is applied to the active address (`EthernetIP[4]` + DIP address), so several identical units on one subnet get distinct addresses. On Central-i the controller answers on the stored octets as written; the DIP offset is reflected only in the reported (identity) address.

## Examples

```text
AEthernetIP[1]=192
AEthernetIP[2]=168
AEthernetIP[3]=0
AEthernetIP[4]=10    ; sets 192.168.0.10 (Save + Reset to apply)
AEthernetIP[1]       ; read the most significant octet
```

## See also

- [EthernetPort](EthernetPort.md) — TCP port number
- [EthernetMAC](EthernetMAC.md) — MAC address
