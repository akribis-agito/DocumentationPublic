---
keyword: EncAbsWData
summary: Data value to be written to the absolute encoder register on a write transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 717
attributes:
  access: rw
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
# EncAbsWData

Data value to be written to the absolute encoder register on a write transaction.

## Overview

`EncAbsWData` holds the data value to be written to the absolute encoder register when a write transaction is issued via [EncAbsSendCmd](EncAbsSendCmd.md). Load this parameter with the desired value before calling `EncAbsSendCmd` with [EncAbsWRType](EncAbsWRType.md) set to write. It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

## Examples

```text
AEncAbsWData=200     ; value to write to the addressed register
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address for the write
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsRData](EncAbsRData.md) — data read back on a read transaction
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
