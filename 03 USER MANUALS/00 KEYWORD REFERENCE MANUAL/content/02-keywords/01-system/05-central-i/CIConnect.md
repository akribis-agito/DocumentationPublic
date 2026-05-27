---
keyword: CIConnect
summary: Command that initiates a Central-i link on the selected axis port.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 504
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIConnect

Command that initiates a Central-i link on the selected axis port.

## Overview

`CIConnect` initiates a Central-i link connection on the selected axis port. Run it after the port has been configured — device role ([CIDeviceType](CIDeviceType.md)) and link parameters ([CILinkConfig](CILinkConfig.md)) — and before any real-time synchronised data exchange can take place. It cannot be issued while the motor is on or in motion. After a successful connection, [CIIdentity](CIIdentity.md) is populated and [CIStatus](CIStatus.md) reflects the live link.

## Examples

```text
ACIConnect           ; bring up the Central-i link on the selected axis
```

## See also

- [CIAutoConnect](CIAutoConnect.md) — connect automatically at power-up
- [CIDisconnect](CIDisconnect.md) — tear down the link
- [CIDeviceType](CIDeviceType.md) / [CILinkConfig](CILinkConfig.md) — port configuration
- [CIStatus](CIStatus.md) — link state
