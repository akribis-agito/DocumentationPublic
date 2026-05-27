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

`EthernetPort` defines the TCP port number on which the controller accepts Ethernet connections. Although the field accepts any value in the full TCP port range (0–65535), the controller communicates **only on port 50000**, which is also the default. It is saved to flash and read during start-up, so changes require [Save](../02-operation/Save.md) and [Reset](../02-operation/Reset.md). In normal use this keyword is left at its default; it exists mainly so the value can be inspected and stored alongside the rest of the network configuration.

## Examples

```text
AEthernetPort       ; read the configured port (50000)
AEthernetPort=50000 ; set the TCP port (default), then Save and Reset
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetMAC](EthernetMAC.md) — MAC address
