---
keyword: ProgHalt
summary: Halts a specified user program thread; it can later be resumed where it stopped.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 197
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
  implemented: partial
overrides: {}
---
# ProgHalt

Halts a specified user program thread; it can later be resumed where it stopped.

## Overview

`ProgHalt[Thread no.]` pauses the specified thread. Halting is not the same as resetting: the thread keeps its program pointer, call stack and numeric stack, so a later `ProgRun[thread],0` continues from the exact instruction where it stopped. To pause every active thread at once use [ProgHaltAll](ProgHaltAll.md), or [ProgHaltThis](ProgHaltThis.md) to pause the task issuing the command. `ProgHalt` is also commonly placed at the end of a non-looping program so execution does not run on into the function definitions (see [ProgFunc](ProgFunc.md)). It is a non-axis command and is not saved to flash.

## How it works

`ProgHalt` removes the thread from the scheduler's round-robin without disturbing its saved position. The thread's status, reported by [ProgStat](ProgStat.md), drops to `0` (not running) immediately. Because nothing is cleared, the difference between halting and resetting is:

| Action | Pointer and stacks | Next `ProgRun` |
|----|----|----|
| `ProgHalt[thread]` | Preserved | `ProgRun[thread],0` resumes from the stop point |
| [ProgReset](ProgReset.md)`[thread]` | Cleared (pointer back to the start of the main program) | Starts a task from its beginning |

The thread number must be within the available range (`[1]` to `[8]`, or `[12]` on a Central-i master); a higher index is rejected.

## Examples

```text
AProgHalt[1]        ; pause thread 1; AProgRun[1],0 later resumes from this point
```

## See also

- [ProgRun](ProgRun.md) — run a thread, or resume it with `ProgRun[thread],0`
- [ProgHaltAll](ProgHaltAll.md) — pause all active threads
- [ProgHaltThis](ProgHaltThis.md) — pause the task that issues the command
- [ProgReset](ProgReset.md) — reset a thread (not the same as halting)
- [ProgStat](ProgStat.md) — running status of a thread
