---
keyword: ProgPriority
summary: Sets the scheduling priority of a user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 296
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPriority

Sets the scheduling priority of a user program task.

## Overview

`ProgPriority` sets the scheduling priority of a user program task. It is an array parameter indexed by task number, with a valid range of `1`–`10`, and it influences how the interpreter shares execution time among concurrent tasks started with [ProgRun](ProgRun.md). It is a non-axis parameter and is saved to flash.

## Examples

```text
AProgPriority[1]=5   ; set task 1 to priority 5 (range 1-10)
```

## See also

- [ProgRun](ProgRun.md) — run a task as a thread
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
