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

`EncAbsAddr` specifies the register address within the absolute encoder to be accessed by the next [EncAbsSendCmd](EncAbsSendCmd.md) transaction. It is used together with [EncAbsWRType](EncAbsWRType.md) (read or write) to target the correct encoder register. It is an axis-scope parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

## Examples

```text
EncAbsAddr=16       ; target register address 16
```

## See also

- [EncAbsWRType](EncAbsWRType.md) — selects read or write access
- [EncAbsWData](EncAbsWData.md) — data to write to the addressed register
- [EncAbsRData](EncAbsRData.md) — data read back from the addressed register
- [EncAbsSendCmd](EncAbsSendCmd.md) — issues the transaction
