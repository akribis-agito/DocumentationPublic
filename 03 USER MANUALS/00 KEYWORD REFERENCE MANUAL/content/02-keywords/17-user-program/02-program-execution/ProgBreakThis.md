---
keyword: ProgBreakThis
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 429
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
# ProgBreakThis

**Definition:**

ProgBreakThis is a command that sets a breakpoint on the currently executing user program task, suspending its execution at the next program instruction. It is a non-axis command and is not saved to flash.

**See also:**

[ProgHaltThis](ProgHaltThis.md), [ProgReset](ProgReset.md), [ProgPointer](ProgPointer.md)
