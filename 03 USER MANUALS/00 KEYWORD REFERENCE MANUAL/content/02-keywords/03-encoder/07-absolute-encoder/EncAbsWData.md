---
keyword: EncAbsWData
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

**Definition:**

EncAbsWData holds the data value to be written to the absolute encoder register when a write transaction is issued via EncAbsSendCmd. Load this parameter with the desired value before calling EncAbsSendCmd with EncAbsWRType set to write. It is an axis-related parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

**See also:**

[EncAbsAddr](EncAbsAddr.md), [EncAbsWRType](EncAbsWRType.md), [EncAbsRData](EncAbsRData.md), [EncAbsSendCmd](EncAbsSendCmd.md)
