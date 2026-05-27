---
keyword: EncAbsWRType
summary: Selects read or write access for the next absolute encoder register transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 715
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncAbsWRType

Selects read or write access for the next absolute encoder register transaction.

## Overview

`EncAbsWRType` selects the type of register access (read or write) to perform when communicating with the absolute encoder via [EncAbsSendCmd](EncAbsSendCmd.md). Set this before issuing `EncAbsSendCmd` to define whether the transaction reads from or writes to the encoder register at [EncAbsAddr](EncAbsAddr.md). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

## Examples

```text
AEncAbsWRType=0      ; read access
AEncAbsWRType=1      ; write access
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address for the transaction
- [EncAbsWData](EncAbsWData.md) — data to write on a write transaction
- [EncAbsRData](EncAbsRData.md) — data read back on a read transaction
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
