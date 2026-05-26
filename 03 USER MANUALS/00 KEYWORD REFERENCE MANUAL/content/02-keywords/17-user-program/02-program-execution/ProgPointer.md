---
keyword: ProgPointer
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 279
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPointer

**Definition:**

ProgPointer is a read-only array parameter that reports the current instruction pointer (program counter) of each user program task. It is a non-axis status variable and is not saved to flash.

**See also:**

[ProgStatAll](ProgStatAll.md), [ProgLine](ProgLine.md), [ProgBreakThis](ProgBreakThis.md)
