---
keyword: ProgReset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 295
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
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
# ProgReset

**Definition:**

ProgReset is a command that resets a user program task, returning it to its initial state. It is an array parameter (indexed by task number) and is a non-axis command not saved to flash.

**See also:**

[ProgHaltThis](ProgHaltThis.md), [ProgBreakThis](ProgBreakThis.md), [ProgStatAll](ProgStatAll.md)
