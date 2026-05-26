---
keyword: ProgHaltThis
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 258
attributes:
  access: ro
  scope: non-axis
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
# ProgHaltThis

**Definition:**

ProgHaltThis is a command that halts the currently executing user program task. It is a non-axis command and is not saved to flash.

**See also:**

[ProgBreakThis](ProgBreakThis.md), [ProgReset](ProgReset.md), [ProgStatAll](ProgStatAll.md)
