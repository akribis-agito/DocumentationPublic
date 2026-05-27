---
keyword: ProgPushArg
summary: Pushes a value onto the argument stack of a target user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 431
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPushArg

Pushes a value onto the argument stack of a target user program task.

## Overview

`ProgPushArg` is a command that pushes a value onto the argument stack of a target user program task, staging arguments before the task is invoked or resumed. The pushed values become the task's argument slots in [ProgArg](ProgArg.md) and are read inside the task through [ProgArgThis](ProgArgThis.md). It is a non-axis command and is not saved to flash.

## Examples

```text
ProgPushArg=10      ; push the value 10 as the next argument for the target task
```

## See also

- [ProgArg](ProgArg.md) — per-task argument slots
- [ProgArgThis](ProgArgThis.md) — read back the arguments inside the running task
- [ProgRun](ProgRun.md) — run a task as a thread
