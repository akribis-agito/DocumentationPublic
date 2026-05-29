---
keyword: EthernetPort
summary: TCP port for Ethernet communication.
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

TCP port for Ethernet communication.

## Overview

`EthernetPort` defines the TCP port number on which the controller accepts Ethernet connections. The field accepts any value in the full TCP port range (0–65535), and the default is **50000**. It is saved to flash and read during start-up, so changes require [Save](../02-operation/Save.md) and [Reset](../02-operation/Reset.md).

How the value is used depends on the platform:

- **Standalone controllers** listen on the configured port for the main connection (the "all-to-default" recovery DIP setting forces port 50000 regardless of the stored value).
- **Central-i controllers** accept the main connection on a fixed port (50000) and report the configured `EthernetPort` value in the identity information rather than using it as the listening port.

In normal use this keyword is left at its default of 50000.

## Examples

```text
AEthernetPort       ; read the configured port
AEthernetPort=50000 ; set the TCP port (default), then Save and Reset
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetMAC](EthernetMAC.md) — MAC address
