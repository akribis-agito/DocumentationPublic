---
keyword: ProgStat
summary: Reports the running status of a specified user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 259
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStat

Reports the running status of a specified user program thread.

## Overview

`ProgStat` is a read-only array parameter, indexed by thread, that reports the running status of one user program thread. It is the per-thread complement of [ProgStatAll](ProgStatAll.md) (combined status of all threads) and is used alongside [ProgError](ProgError.md) when diagnosing why a thread stopped. Index it `[1]` to `[8]` (or `[12]` on a Central-i master). It is a non-axis status variable and is not saved to flash.

## How it works

The controller maintains the status of each thread as the scheduler services it:

| Value | Meaning |
|----|----|
| -1 | No user program loaded in the controller |
| 0 | Loaded but this thread is not running (stopped, halted, reset, or stopped on error) |
| 1 | This thread is running |

Running (`1`) is not written the instant the thread is started; it is set when the scheduler next services that thread's line. Because servicing is gated by [ProgPriority](ProgPriority.md) — a higher priority value makes a thread wait more scheduler passes between lines — there can be a short delay between starting a thread and `ProgStat` reading `1`. The `0` value is written promptly on every stop path (halt, reset, breakpoint, single-step, and error-halt). Starting a thread (for example with [ProgRun](ProgRun.md)) also clears that thread's [ProgError](ProgError.md) to `0`.

When a thread stops because of a run-time error, `ProgStat` returns to `0` — there is no distinct "error" value — and the cause is left in [ProgError](ProgError.md) for that thread. To distinguish a clean stop from an error stop, read `ProgError` for the same index.

## Examples

```text
AProgStat[1]        ; 1 if thread 1 is running, 0 if stopped, -1 if no program
```

## See also

- [ProgStatAll](ProgStatAll.md) — combined status of all threads
- [ProgError](ProgError.md) — last error code per thread
- [ProgRun](ProgRun.md) — run a task as a thread
- [ProgPointer](ProgPointer.md) — current position of each thread
