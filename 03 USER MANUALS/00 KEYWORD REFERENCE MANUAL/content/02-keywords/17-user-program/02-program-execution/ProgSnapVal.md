---
keyword: ProgSnapVal
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 538
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgSnapVal

**Definition:**

ProgSnapVal is a read-only array parameter that holds the values captured by the program snapshot mechanism. Each element contains the last recorded value for the corresponding source defined in ProgSnapSrc. It is a non-axis status variable and is not saved to flash.

**See also:**

[ProgSnapSrc](ProgSnapSrc.md), [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md)
