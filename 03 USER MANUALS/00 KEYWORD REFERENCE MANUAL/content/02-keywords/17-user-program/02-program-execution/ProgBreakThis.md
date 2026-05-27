---
keyword: ProgBreakThis
summary: Sets a breakpoint on the currently executing user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgBreakThis` is a command issued from inside a running user program that suspends the calling thread at the current point in its execution. It is the self-targeting counterpart of [ProgBreaks](ProgBreaks.md): instead of pre-loading a program location to stop at, the program asks to stop *here* when this line runs. It is intended for debugging, so the thread can be inspected and later resumed rather than reset. It is a non-axis command and is not saved to flash.

## How it works

When a running program executes `ProgBreakThis`, the controller marks the calling thread as not needing to execute further instructions and updates its program status to "not running" (unless that thread has no program loaded). Execution stops at this location with the thread's state intact; use [ProgPointer](ProgPointer.md) to see where it is suspended, [ProgCallStack](ProgCallStack.md) to inspect the call frames, and the program snapshot ([ProgSnapVal](ProgSnapVal.md)) for captured state. Resume the thread with [ProgRun](ProgRun.md) or step it with [ProgSingle](ProgSingle.md).

`ProgBreakThis` must be issued from within a user program (it acts on "this" thread). The difference from [ProgHaltThis](ProgHaltThis.md) is intent: both stop the thread where it is, but `ProgBreakThis` is the debugging break used together with the breakpoint and single-step tools.

## Examples

```text
AProgBreakThis       ; break the currently executing task at the next instruction
```

## See also

- [ProgHaltThis](ProgHaltThis.md) — halt the running task
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
