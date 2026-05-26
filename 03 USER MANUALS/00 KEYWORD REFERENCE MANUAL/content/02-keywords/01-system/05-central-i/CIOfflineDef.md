---
keyword: CIOfflineDef
summary: Per-axis array defining which parameters are included in the Central-i offline dataset.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 507
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CIOfflineDef

Per-axis array defining which parameters are included in the Central-i offline dataset.

## Overview

`CIOfflineDef` is an axis-related array that defines which parameters make up the Central-i offline dataset — i.e. which values are sent when [CIOfflineSend](CIOfflineSend.md) is executed. The values themselves are held in [CIOfflineData](CIOfflineData.md). The definition is saved to flash. It is the offline counterpart of [CISyncDef](CISyncDef.md), which defines the live synchronous data map.

## Examples

```text
CIOfflineDef[1]?    ; read the first offline-dataset definition element
```

## See also

- [CIOfflineData](CIOfflineData.md) — offline payload values
- [CIOfflineSend](CIOfflineSend.md) — transmit the offline package
- [CISyncDef](CISyncDef.md) — synchronous (live-link) data definition
