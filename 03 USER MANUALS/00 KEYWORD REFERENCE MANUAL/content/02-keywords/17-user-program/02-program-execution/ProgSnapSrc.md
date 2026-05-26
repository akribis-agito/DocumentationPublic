---
keyword: ProgSnapSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 537
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgSnapSrc

**Definition:**

ProgSnapSrc is an array parameter that configures which controller parameters are captured by the program snapshot mechanism. Each element specifies a source parameter to be recorded when a snapshot is triggered. It is a non-axis parameter saved to flash.

**See also:**

[ProgSnapVal](ProgSnapVal.md), [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md)
