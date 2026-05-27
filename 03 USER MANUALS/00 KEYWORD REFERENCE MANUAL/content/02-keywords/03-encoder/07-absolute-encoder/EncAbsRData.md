---
keyword: EncAbsRData
summary: Data returned from an absolute encoder register read transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 718
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncAbsRData

Data returned from an absolute encoder register read transaction.

## Overview

`EncAbsRData` contains the data returned from an absolute encoder register read transaction triggered by [EncAbsSendCmd](EncAbsSendCmd.md). After a successful read, the value from the encoder register addressed by [EncAbsAddr](EncAbsAddr.md) is available here. It is a read-only, axis-scope parameter that is not saved to flash.

## Examples

```text
AEncAbsRData        ; read the result of the last register read
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address that was read
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write to the addressed register
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
