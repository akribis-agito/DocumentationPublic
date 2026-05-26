---
keyword: EncAbsRData
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

**Definition:**

EncAbsRData contains the data returned from an absolute encoder register read transaction triggered by EncAbsSendCmd. After a successful read, the value from the encoder register addressed by EncAbsAddr is available here. It is a read-only, axis-related parameter that is not saved to flash.

**See also:**

[EncAbsAddr](EncAbsAddr.md), [EncAbsWRType](EncAbsWRType.md), [EncAbsWData](EncAbsWData.md), [EncAbsSendCmd](EncAbsSendCmd.md)
