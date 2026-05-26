---
keyword: CIIdentity
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 509
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 23
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIIdentity

**Definition:**

CIIdentity is a read-only axis-related array that contains identifying information returned by the connected Central-i device, such as device class, version, and serial number. It is populated automatically after a successful [CIConnect](CIConnect.md).

**See also:**

[CIConnect](CIConnect.md), [CIStatus](CIStatus.md), [CIDeviceType](CIDeviceType.md)
