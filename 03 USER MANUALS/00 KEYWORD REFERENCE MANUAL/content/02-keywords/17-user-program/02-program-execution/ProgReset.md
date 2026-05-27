---
keyword: ProgReset
summary: Resets a user program task to its initial state.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Resets a user program task to its initial state.

## Overview

`ProgReset` is a command, indexed by task number, that resets a user program task to its initial state. Unlike [ProgHalt](ProgHalt.md), which merely suspends a thread so it can resume, resetting clears its progress so a subsequent [ProgRun](ProgRun.md) starts from the beginning. To reset every thread and clear all pointers and stacks at once, use [ProgResetAll](ProgResetAll.md). It is a non-axis command and is not saved to flash.

## Examples

```text
AProgReset[1]       ; reset task 1 to its initial state
```

## See also

- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgHaltThis](ProgHaltThis.md) — halt the running task
- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
