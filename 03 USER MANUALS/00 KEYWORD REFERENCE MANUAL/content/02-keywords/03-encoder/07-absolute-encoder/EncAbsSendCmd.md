---
keyword: EncAbsSendCmd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 719
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EncAbsSendCmd

**Definition:**

EncAbsSendCmd is a command that initiates a register read or write transaction to the absolute encoder using the address, data, and type set in EncAbsAddr, EncAbsWData, and EncAbsWRType. After the transaction completes, EncAbsRData holds the result of a read operation. It is an axis-related command function.

**See also:**

[EncAbsAddr](EncAbsAddr.md), [EncAbsWRType](EncAbsWRType.md), [EncAbsWData](EncAbsWData.md), [EncAbsRData](EncAbsRData.md)
