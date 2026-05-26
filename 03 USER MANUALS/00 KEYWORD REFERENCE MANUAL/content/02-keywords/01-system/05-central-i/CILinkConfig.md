---
keyword: CILinkConfig
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 539
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CILinkConfig

**Definition:**

CILinkConfig is an axis-related array that configures the physical and protocol parameters of a Central-i port, such as baud rate, timing, and framing options. The settings are saved to flash and applied when [CIConnect](CIConnect.md) initialises the link.

**See also:**

[CIDeviceType](CIDeviceType.md), [CIConnect](CIConnect.md), [CISyncDef](CISyncDef.md)
