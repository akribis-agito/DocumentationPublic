---
keyword: ProgHaltAll
summary: Halts all currently active user program threads.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 278
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
# ProgHaltAll

Halts all currently active user program threads.

## Overview

`ProgHaltAll` pauses every user program thread in one command. As with [ProgHalt](ProgHalt.md), halting is not the same as resetting: each thread keeps its program pointer and stacks and can be resumed with `ProgRun[thread],0`. To stop all threads **and** clear their pointers and stacks, use [ProgResetAll](ProgResetAll.md) instead. It is a non-axis command and is not saved to flash.

## How it works

`ProgHaltAll` removes all threads from the scheduler at once by clearing every thread's "execute" flag, then sets each thread's [ProgStat](ProgStat.md) to `0` (not running). No pointers or stacks are touched, so the program state is frozen exactly where each thread stopped and can be continued individually with `ProgRun[thread],0`. The command requires a stored program; with no program loaded it is rejected.

## Examples

```text
AProgHaltAll         ; halt every active user program thread
```

## See also

- [ProgHalt](ProgHalt.md) — pause a single thread
- [ProgHaltThis](ProgHaltThis.md) — pause the task that issues the command
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgStatAll](ProgStatAll.md) — combined status of all threads
