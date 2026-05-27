---
keyword: ProgHaltThis
summary: Halts the currently executing user program task.
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

Halts the currently executing user program task.

## Overview

`ProgHaltThis` is a command that halts the currently executing user program task — the "self-halt" form of [ProgHalt](ProgHalt.md), which targets a thread by index. As with halting in general, the task can be resumed with [ProgRun](ProgRun.md) rather than restarted, in contrast to [ProgReset](ProgReset.md). It is a non-axis command and is not saved to flash.

## Examples

```text
ProgHaltThis        ; halt the task that issues this command
```

## See also

- [ProgHalt](ProgHalt.md) — halt a thread by index
- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
