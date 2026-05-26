---
keyword: CIIdentity
summary: Per-axis array of identifying information returned by the connected Central-i device.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 509
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 24
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
overrides:
  standalone.v4:
    array_size: 23
  central-i.v4:
    array_size: 23
---
# CIIdentity

Per-axis array of identifying information returned by the connected Central-i device.

## Overview

`CIIdentity` is a read-only, axis-related array containing identifying information reported by the connected Central-i device — such as device class, version, and serial number. It is populated automatically after a successful [CIConnect](CIConnect.md); before connection its contents are not meaningful.

## Examples

```text
CIIdentity[1]?      ; read the first identity word of the connected device
```

## See also

- [CIConnect](CIConnect.md) — populates this array on connect
- [CIStatus](CIStatus.md) — live link state
- [CIDeviceType](CIDeviceType.md) — locally configured port role
