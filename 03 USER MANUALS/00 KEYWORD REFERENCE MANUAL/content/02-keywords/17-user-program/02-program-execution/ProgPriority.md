---
keyword: ProgPriority
summary: Sets the scheduling priority (service interval) of a user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Sets the scheduling priority (service interval) of a user program thread.

## Overview

`ProgPriority` sets the scheduling priority of a user program thread. It is an array parameter indexed by thread number, with a valid range of `1`–`10` and a default of `1`, and it controls how often the interpreter executes that thread relative to the others started with [ProgRun](ProgRun.md). It is a non-axis parameter and is saved to flash.

## How it works

The interpreter runs threads cooperatively, one line at a time. On each scheduling pass it advances round-robin to the next active thread and executes a single program line for it before moving on, so by default all running threads make progress at an equal rate.

`ProgPriority` changes that rate by acting as an *interval*: each thread carries a counter that increments every time the scheduler reaches it, and a line is executed only when the counter reaches the thread's `ProgPriority` value, after which the counter resets. The effect is:

- `ProgPriority[t] = 1` (the default) — the thread runs a line on every pass: full speed, highest effective priority.
- Higher values run the thread *less* often — at `2` it runs every second time it is reached, at `10` every tenth time.

In other words, a **lower** number gives a thread a **larger** share of execution time. Use it to bias time toward a time-critical thread (leave it at `1`) while throttling background threads (set them higher). The value is per thread, so it applies to whichever task is currently running as that thread number (see [ProgRun](ProgRun.md)).

## Examples

```text
AProgPriority[1]=1   ; thread 1 at full rate (default, highest effective priority)
AProgPriority[2]=5   ; thread 2 runs one line every 5th scheduling pass
```

## See also

- [ProgRun](ProgRun.md) — run a task as a thread
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
