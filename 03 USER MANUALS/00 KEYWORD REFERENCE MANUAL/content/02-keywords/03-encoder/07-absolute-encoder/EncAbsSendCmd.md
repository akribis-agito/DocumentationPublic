---
keyword: EncAbsSendCmd
summary: Command that initiates a register read/write transaction to the absolute encoder.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 719
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncAbsSendCmd

Command that initiates a register read/write transaction to the absolute encoder.

## Overview

`EncAbsSendCmd` is a command function that initiates a register read or write transaction to the absolute encoder using the address, data, and type set in [EncAbsAddr](EncAbsAddr.md), [EncAbsWData](EncAbsWData.md), and [EncAbsWRType](EncAbsWRType.md). After the transaction completes, [EncAbsRData](EncAbsRData.md) holds the result of a read operation. It is an axis-scope command function.

## Examples

```text
AEncAbsWRType=0      ; configure for a read
AEncAbsAddr=16       ; target register 16
AEncAbsSendCmd       ; execute the transaction; result in EncAbsRData
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address for the transaction
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write on a write transaction
- [EncAbsRData](EncAbsRData.md) — data read back on a read transaction
