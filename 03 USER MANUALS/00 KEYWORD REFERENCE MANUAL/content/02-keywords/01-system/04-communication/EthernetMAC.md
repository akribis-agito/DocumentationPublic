---
keyword: EthernetMAC
summary: Controller MAC address, stored as decimal octets one per array element.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 602
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
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
# EthernetMAC

Controller MAC address, stored as decimal octets one per array element.

## Overview

`EthernetMAC` holds the controller's MAC address as six octets stored in **decimal**, one per array element. (The array is dimensioned so the usable indices start at `[1]`; index `[0]` is not used.) MAC addresses are normally written in hexadecimal, so each pair of hex digits must be converted to its decimal value before writing it here. Each controller on the same network must have a unique MAC address. It is saved to flash and read during start-up, so set the octets, [Save](../02-operation/Save.md), and [Reset](../02-operation/Reset.md) to apply.

For example, the placeholder address `AA:BB:CC:DD:EE:FF` is stored as:

| Element | Hex | Decimal |
|---------|-----|---------|
| EthernetMAC[1] | AA | 170 |
| EthernetMAC[2] | BB | 187 |
| EthernetMAC[3] | CC | 204 |
| EthernetMAC[4] | DD | 221 |
| EthernetMAC[5] | EE | 238 |
| EthernetMAC[6] | FF | 255 |

## How it works

The firmware reads the six decimal octets and assembles them into the hardware MAC address the network interface advertises. To convert a hex octet to decimal, multiply the first hex digit by 16 and add the second (for example `CC` = 12 × 16 + 12 = 204).

## Examples

```text
AEthernetMAC[1]=170 ; first octet (AA in hex)
AEthernetMAC[3]     ; read the third octet (decimal)
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetPort](EthernetPort.md) — TCP port number
