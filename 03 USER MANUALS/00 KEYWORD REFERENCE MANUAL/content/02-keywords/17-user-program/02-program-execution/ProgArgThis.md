---
keyword: ProgArgThis
summary: Reads back the argument values received by the currently executing task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 433
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 21
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
overrides:
  central-i.v5:
    array_size: 27
---
# ProgArgThis

Reads back the argument values received by the currently executing task.

## Overview

`ProgArgThis` is an array parameter that reads back the argument values received by the currently executing user program task, giving the task access to its own argument list. It is the in-task view of the arguments staged with [ProgPushArg](ProgPushArg.md) and stored per task in [ProgArg](ProgArg.md). `ProgArgThis` is a non-axis parameter and is not saved to flash.

## Examples

```text
AProgArgThis[1]     ; read the first argument received by the running task
```

## See also

- [ProgArg](ProgArg.md) — per-task argument slots
- [ProgPushArg](ProgPushArg.md) — push an argument value onto a task's argument stack
