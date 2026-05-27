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

`EncAbsRData` contains the byte returned from an absolute encoder register read transaction triggered by [EncAbsSendCmd](EncAbsSendCmd.md). After a successful read, the value from the encoder register addressed by [EncAbsAddr](EncAbsAddr.md) is available here. The value is 8-bit (0 to 255). It is a read-only, axis-scope parameter that is not saved to flash. Available on v4 firmware only.

## How it works

On a read transaction `EncAbsSendCmd` waits for the encoder to respond, reads the returned byte from the encoder-interface read-data register, bit-reverses it (the encoder transmits LSB-first), and stores the result in `EncAbsRData` (`AG300_CTL01Funcs.c:20051`–`20052`). It is only updated by a read ([EncAbsWRType](EncAbsWRType.md) = 0); a write transaction leaves it unchanged. Read it after `EncAbsSendCmd` reports completion.

## Examples

```text
AEncAbsRData        ; read the result of the last register read
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address that was read
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write to the addressed register
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; this interface applies to the serial absolute encoder
