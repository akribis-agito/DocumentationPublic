---
keyword: ProgBreakThis
summary: Sets a breakpoint on the currently executing user program task.
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

Sets a breakpoint on the currently executing user program task.

## Overview

`ProgBreakThis` is a command that sets a breakpoint on the currently executing user program task, suspending its execution at the next program instruction. Unlike [ProgHaltThis](ProgHaltThis.md), which stops the task, it is intended for debugging so execution can be inspected and resumed. Use [ProgPointer](ProgPointer.md) to see where each task is suspended. It is a non-axis command and is not saved to flash.

## Examples

```text
AProgBreakThis       ; break the currently executing task at the next instruction
```

## See also

- [ProgHaltThis](ProgHaltThis.md) — halt the running task
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
