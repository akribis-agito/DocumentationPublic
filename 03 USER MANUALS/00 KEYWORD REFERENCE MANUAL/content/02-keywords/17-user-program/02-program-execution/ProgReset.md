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

`ProgReset[Thread no.]` returns a single user program thread to its initial state. Unlike [ProgHalt](ProgHalt.md), which merely suspends a thread so it can resume from the same spot, resetting clears the thread's progress so a subsequent [ProgRun](ProgRun.md) starts a task from its beginning. To reset every thread and clear all pointers and stacks at once, use [ProgResetAll](ProgResetAll.md). It is a non-axis command and is not saved to flash.

## How it works

`ProgReset` is indexed by **thread number** (`[1]` to `[8]`, or `[12]` on a Central-i master). Resetting a thread:

- Sets its program pointer back to the start of the main program (task 1).
- Clears its call stack and numeric stack.
- Clears any wait state and pending single-step flags.
- Clears the thread's [ProgError](ProgError.md) value.

The command is rejected if there is no stored program, if the thread index is out of range, or if the thread is currently running — stop it with [ProgHalt](ProgHalt.md) first. After a reset the thread is left stopped; the next [ProgRun](ProgRun.md) chooses which task it executes.

## Examples

```text
AProgReset[1]       ; reset thread 1 to its initial state (must not be running)
```

## See also

- [ProgRun](ProgRun.md) — run a thread after resetting it
- [ProgHalt](ProgHalt.md) — pause a thread (preserves its position, unlike reset)
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgStat](ProgStat.md) — running status of a thread
- [ProgStatAll](ProgStatAll.md) — combined status of all threads
