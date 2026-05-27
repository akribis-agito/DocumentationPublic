---
keyword: EncAbsAddr
summary: Register address within the absolute encoder to be accessed by the next transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# EncAbsAddr

Register address within the absolute encoder to be accessed by the next transaction.

## Overview

`EncAbsAddr` specifies the memory address inside the absolute encoder to be accessed by the next [EncAbsSendCmd](EncAbsSendCmd.md) transaction. It is used together with [EncAbsWRType](EncAbsWRType.md) (read or write) to target the correct encoder register. The valid range is 0 to 255 (8-bit). It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion. Available on v4 firmware only.

## How it works

When [EncAbsSendCmd](EncAbsSendCmd.md) runs, it writes `EncAbsAddr` to the encoder-interface memory-address register before issuing the read or write command (`AG300_CTL01Funcs.c:20045`/`20056`). The address therefore selects which encoder register the subsequent transaction targets; it has no effect on its own. Set it together with [EncAbsWRType](EncAbsWRType.md) — and, for a write, [EncAbsWData](EncAbsWData.md) — then issue `EncAbsSendCmd`.

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
