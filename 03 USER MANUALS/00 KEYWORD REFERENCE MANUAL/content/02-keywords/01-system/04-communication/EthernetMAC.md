---
keyword: EthernetMAC
summary: Controller MAC address, stored as decimal octets one per array element.
availability:
  standalone:
  - v4
  - v5
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

`EthernetMAC` holds the controller's MAC address as six octets in **decimal**, one per array element. Each controller on the same network must have a unique MAC address. It is saved to flash. For example, `00-B0-D0-63-C2-26` is stored as:

| Element | Hex | Decimal |
|---------|-----|---------|
| EthernetMAC[1] | 00 | 0 |
| EthernetMAC[2] | B0 | 176 |
| EthernetMAC[3] | D0 | 208 |
| EthernetMAC[4] | 63 | 99 |
| EthernetMAC[5] | C2 | 194 |
| EthernetMAC[6] | 26 | 38 |

## Examples

```text
AEthernetMAC[3]     ; read the third octet (decimal)
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetPort](EthernetPort.md) — TCP port number
