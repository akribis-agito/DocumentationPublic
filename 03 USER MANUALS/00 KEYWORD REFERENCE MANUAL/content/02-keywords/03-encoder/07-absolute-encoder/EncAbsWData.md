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

`EncAbsWData` holds the byte to be written to the absolute encoder register on a write transaction issued via [EncAbsSendCmd](EncAbsSendCmd.md). Load it before calling `EncAbsSendCmd` with [EncAbsWRType](EncAbsWRType.md) set to 1 (write). The valid range is 0 to 255 (8-bit). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion. Available on v4 firmware only.

## How it works

On a write transaction `EncAbsSendCmd` writes `EncAbsWData` to the encoder-interface write-data register after setting [EncAbsAddr](EncAbsAddr.md), then issues the encoder "write to memory" command (`AG300_CTL01Funcs.c:20057`). It is ignored on a read transaction ([EncAbsWRType](EncAbsWRType.md) = 0). The value is the data byte sent to the addressed encoder register.

## Examples

```text
AEncAbsWData=200     ; value to write to the addressed register
AEncAbsWData         ; query the staged write value
```

## See also

- [EncAbsAddr](EncAbsAddr.md) — register address for the write
- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsRData](EncAbsRData.md) — data read back on a read transaction
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; this interface applies to the serial absolute encoder
