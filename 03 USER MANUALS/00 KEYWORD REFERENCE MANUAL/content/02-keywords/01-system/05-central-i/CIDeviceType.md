---
keyword: CIDeviceType
summary: Selects the role/class of the Central-i port on an axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 503
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIDeviceType

Selects the role/class of the Central-i port on an axis.

## Overview

`CIDeviceType` selects the role of the Central-i port on its axis — for example master or slave, or a specific device class. It is axis-related and saved to flash, and it affects how the link is initialised at startup or when [CIConnect](CIConnect.md) is called. Configure it (together with [CILinkConfig](CILinkConfig.md)) before connecting.

## Examples

```text
ACIDeviceType       ; query the configured Central-i role for this axis
```

## See also

- [CIConnect](CIConnect.md) — initiate the link
- [CILinkConfig](CILinkConfig.md) — physical/protocol parameters
- [CISyncDef](CISyncDef.md) — synchronous data definition
