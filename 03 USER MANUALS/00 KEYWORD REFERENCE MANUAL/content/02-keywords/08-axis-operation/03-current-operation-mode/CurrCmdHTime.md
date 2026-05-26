---
keyword: CurrCmdHTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 332
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2000000000
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdHTime

**Definition:**

If CurrCmdSrc is 0 or 3 (analog input or as slave drive), only CurrCmdHTime\[1\] is used to define the time to stay within current operation mode.

If CurrCmdSrc is 1 or 2, each CurrCmdHTime array element defines the holding time for the corresponding CurrCmdVal pair.

CurrCmdHTime value is defined as shown.

| Value | Descriptions |
|---|---|
| < 0 | Source value is held indefinitely. |
| 0 | Axis exits current operation mode and enters position operation mode. |
| > 0 | Source value is held for CurrCmdHTime, before exiting current operation mode (CurrCmdSrc = 0 or 3) or proceeding to the next pair (CurrCmdSrc = 1 or 2). For CurrCmdSrc is 1 or 2, if CurrCmdIndex reaches last index value and last CurrCmdHTime entry is more than 0, axis will hold onto the last CurrCmdVal value indefinitely. |
