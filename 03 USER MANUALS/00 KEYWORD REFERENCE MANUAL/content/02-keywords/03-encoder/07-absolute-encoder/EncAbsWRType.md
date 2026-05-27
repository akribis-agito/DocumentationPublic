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

`EncAbsWRType` selects the direction of the next absolute-encoder register transaction (read or write) performed by [EncAbsSendCmd](EncAbsSendCmd.md). Set it before issuing `EncAbsSendCmd` to define whether the transaction reads from or writes to the encoder memory at [EncAbsAddr](EncAbsAddr.md). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion. Available on v4 firmware only.

## How it works

`EncAbsSendCmd` branches on this value (`AG300_CTL01Funcs.c:20043`):

| Value | Access | Effect |
|---|---|---|
| 0 | Read | Sends the encoder "read from memory" command; the returned byte appears in [EncAbsRData](EncAbsRData.md). |
| 1 | Write | Sends the encoder "write to memory" command, writing [EncAbsWData](EncAbsWData.md) to the addressed register. |

The value is a direction selector only; it does not itself trigger the transaction. See [EncAbsSendCmd](EncAbsSendCmd.md) for the full sequence.

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
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; this interface applies to the serial absolute encoder
