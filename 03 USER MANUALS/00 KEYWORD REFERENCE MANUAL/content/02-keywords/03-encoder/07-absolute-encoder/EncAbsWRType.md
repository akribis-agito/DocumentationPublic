---
keyword: EncAbsWRType
summary: Selects read or write access for the next absolute encoder register transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    can_code: 898
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# EncAbsWRType

Selects read or write access for the next absolute encoder register transaction.

## Overview

`EncAbsWRType` selects the direction of the next absolute-encoder register transaction (read or write) performed by [EncAbsSendCmd](EncAbsSendCmd.md). Set it before issuing `EncAbsSendCmd` to define whether the transaction reads from or writes to the encoder memory at [EncAbsAddr](EncAbsAddr.md). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion. Available on v4 (standalone and central-i) and v5 (central-i); the CAN code differs between the two (see [Changes between versions](#changes-between-versions)).

## How it works

`EncAbsSendCmd` branches on this value:

| Value | Access | Effect |
|---|---|---|
| 0 | Read | Sends the encoder "read from memory" command; the returned byte appears in [EncAbsRData](EncAbsRData.md). |
| 1 | Write | Sends the encoder "write to memory" command, writing [EncAbsWData](EncAbsWData.md) to the addressed register. |

The value is a direction selector only; it does not itself trigger the transaction. See [EncAbsSendCmd](EncAbsSendCmd.md) for the full sequence.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| CAN code | 715 | 898 |

The value range, default and motor-on / in-motion restrictions are the same in both versions. **v5 is central-i only.** The transaction that uses this value runs only on a standalone controller: on a central-i master, v5 refuses [EncAbsSendCmd](EncAbsSendCmd.md), and on v4 the transaction does not reach the encoder and changes unrelated settings in the remote drive (see [EncAbsSendCmd](EncAbsSendCmd.md)).

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
