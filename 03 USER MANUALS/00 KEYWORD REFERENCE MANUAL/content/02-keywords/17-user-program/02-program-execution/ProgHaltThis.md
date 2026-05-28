---
keyword: ProgHaltThis
summary: Halts the currently executing user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgHaltThis` pauses the thread that is executing it — the "self-halt" form of [ProgHalt](ProgHalt.md), which instead targets a thread by index. A thread uses it to suspend its own execution, for example at the end of a one-shot routine. As with halting in general, the thread keeps its position and stacks and can be resumed with `ProgRun[thread],0` rather than restarted, in contrast to [ProgReset](ProgReset.md). It is a non-axis command and is not saved to flash.

## How it works

`ProgHaltThis` is only valid when issued **from within a running user program** — sending it from a communication terminal is rejected. When executed, it clears the current thread's "execute" flag so the scheduler stops servicing it, and sets that thread's [ProgStat](ProgStat.md) to `0` (not running). The thread's program pointer is held on the `ProgHaltThis` line itself (it is not advanced past it), so the thread does not run on into whatever follows. Because the pointer stays on the halt line, resuming the thread with `ProgRun[thread],0` re-executes the `ProgHaltThis` and halts again; to continue past it, move the pointer first (for example reset the thread with [ProgReset](ProgReset.md) and run the desired task, or run a different task).

## Examples

```text
AProgHaltThis        ; halt the task that issues this command
```

## See also

- [ProgHalt](ProgHalt.md) — halt a thread by index
- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
