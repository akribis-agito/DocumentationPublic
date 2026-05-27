---
keyword: ProgResetAll
summary: Stops all running threads and resets every pointer and stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 192
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
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgResetAll

Stops all running threads and resets every pointer and stack.

## Overview

`ProgResetAll` returns the whole user program system to its initial state, resetting every thread's program pointer and clearing all call and numeric stacks. It is the global form of [ProgReset](ProgReset.md): where `ProgReset` returns a single thread to its initial state, `ProgResetAll` clears the entire program state in one command. Compare with [ProgHaltAll](ProgHaltAll.md), which only suspends threads without clearing them. It is a non-axis command and is not saved to flash.

## How it works

`ProgResetAll` only proceeds when **no thread is running**. It first checks every thread; if even one is still active the command is rejected with an error and nothing is changed. Stop all threads with [ProgHaltAll](ProgHaltAll.md) before issuing it. The command is also rejected if there is no stored program.

When it does run, it re-initializes the full program state: every thread's pointer is set back to the start of the main program, all call and numeric stacks are emptied, per-thread errors are cleared, and each thread's [ProgStat](ProgStat.md) returns to `0` (not running). This is the cleanest way to bring all threads back to a known starting point before a fresh [ProgRun](ProgRun.md).

## Examples

```text
AProgHaltAll         ; first stop every thread...
AProgResetAll        ; ...then reset all pointers and stacks
```

## See also

- [ProgReset](ProgReset.md) — reset a single thread
- [ProgHaltAll](ProgHaltAll.md) — stop all threads (required before ProgResetAll)
- [ProgStatAll](ProgStatAll.md) — combined status of all threads
