---
keyword: CIOfflineData
summary: Per-axis array holding the payload sent during a Central-i offline (simulation) transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 501
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
# CIOfflineData

Per-axis array holding the payload sent during a Central-i offline (simulation) transaction.

## Overview

`CIOfflineData` is an axis-related array holding the data payload transmitted during a Central-i offline (simulation) transaction. Load the values before calling [CIOfflineSend](CIOfflineSend.md); they are saved to flash so the same offline dataset can be replayed after reset. The *shape* of the dataset — which parameters it contains — is set by [CIOfflineDef](CIOfflineDef.md).

## Examples

```text
ACIOfflineData[1]=0  ; set the first element of the offline payload
```

## See also

- [CIOfflineDef](CIOfflineDef.md) — defines the offline dataset contents
- [CIOfflineSend](CIOfflineSend.md) — transmit the offline package
