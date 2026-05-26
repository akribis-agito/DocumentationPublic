---
keyword: EthernetIP
summary: Controller IP address, stored one octet per array element.
availability:
  standalone:
  - v4
  - v5
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

`EthernetIP` holds the controller's IP address as four octets, one per array element (each 0–255). It is saved to flash. For example, the address `172.1.1.50` is stored as:

| Element | Value |
|---------|-------|
| EthernetIP[1] | 172 |
| EthernetIP[2] | 1 |
| EthernetIP[3] | 1 |
| EthernetIP[4] | 50 |

## Examples

```text
EthernetIP[1]=172
EthernetIP[2]=1
EthernetIP[3]=1
EthernetIP[4]=50    ; sets 172.1.1.50 (Save + Reset to apply)
```

## See also

- [EthernetPort](EthernetPort.md) — TCP port number
- [EthernetMAC](EthernetMAC.md) — MAC address
