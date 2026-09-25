---
keyword: EncAbsAddr
summary: Register address within the absolute encoder to be accessed by the next transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 716
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
overrides:
  central-i.v5:
    can_code: 899
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# EncAbsAddr

Register address within the absolute encoder to be accessed by the next transaction.

## Overview

`EncAbsAddr` specifies the memory address inside the absolute encoder to be accessed by the next [EncAbsSendCmd](EncAbsSendCmd.md) transaction. It is used together with [EncAbsWRType](EncAbsWRType.md) (read or write) to target the correct encoder register. The valid range is 0 to 255 (8-bit). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion. Available on v4 (standalone and central-i) and v5 (central-i); the CAN code differs between the two (see [Changes between versions](#changes-between-versions)).

## How it works

When [EncAbsSendCmd](EncAbsSendCmd.md) runs, it writes `EncAbsAddr` to the encoder-interface memory-address register before issuing the read or write command. The address therefore selects which encoder register the subsequent transaction targets; it has no effect on its own. Set it together with [EncAbsWRType](EncAbsWRType.md) — and, for a write, [EncAbsWData](EncAbsWData.md) — then issue `EncAbsSendCmd`.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| CAN code | 716 | 899 |

The value range, default and motor-on / in-motion restrictions are the same in both versions. **v5 is central-i only.** The transaction that uses this value runs only on a standalone controller: on a central-i master, v5 refuses [EncAbsSendCmd](EncAbsSendCmd.md) and on v4 the transaction does not reach the encoder.

## Examples

```text
AEncAbsAddr=16       ; target register address 16
AEncAbsAddr          ; query the configured address
```

## See also

- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write to the addressed register
- [EncAbsRData](EncAbsRData.md) — data read back from the addressed register
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; this interface applies to the serial absolute encoder
