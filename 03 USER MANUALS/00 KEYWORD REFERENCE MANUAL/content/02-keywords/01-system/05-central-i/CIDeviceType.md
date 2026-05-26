---
keyword: CIDeviceType
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

CIDeviceType is an axis-related parameter that selects the role of the Central-i port on that axis — for example, master or slave, or a specific device class. The value is saved to flash and affects how the link is initialised at startup or when [CIConnect](CIConnect.md) is called.

**See also:**

[CIConnect](CIConnect.md), [CILinkConfig](CILinkConfig.md), [CISyncDef](CISyncDef.md)
