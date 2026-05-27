---
keyword: EthernetPort
summary: TCP port for Ethernet communication (Agito controllers support port 50000).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 601
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
  - 65535
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
---
# EthernetPort

TCP port for Ethernet communication (Agito controllers support port 50000).

## Overview

`EthernetPort` defines the TCP port number used for Ethernet communication. Agito controllers support **only port 50000**, which is also the default. It is saved to flash.

## Examples

```text
AEthernetPort       ; query the configured port (50000)
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetMAC](EthernetMAC.md) — MAC address
