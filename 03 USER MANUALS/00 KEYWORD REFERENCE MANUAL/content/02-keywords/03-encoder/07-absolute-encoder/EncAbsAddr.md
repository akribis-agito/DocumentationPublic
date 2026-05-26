---
keyword: EncAbsAddr
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

**Definition:**

EncAbsAddr specifies the register address within the absolute encoder to be accessed by the next EncAbsSendCmd transaction. The address is used in combination with EncAbsWRType to target the correct encoder register for a read or write operation. It is an axis-related parameter, not saved to flash, and cannot be changed while the motor is on or in motion.

**See also:**

[EncAbsWRType](EncAbsWRType.md), [EncAbsWData](EncAbsWData.md), [EncAbsRData](EncAbsRData.md), [EncAbsSendCmd](EncAbsSendCmd.md)
