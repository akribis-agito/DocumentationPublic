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

The controller maintains the status of each thread as the scheduler services it, and also updates it the moment a thread is started, paused, reset or stops on an error, so the value is current even for inactive threads:

| Value | Meaning |
|----|----|
| -1 | No user program loaded in the controller |
| 0 | Loaded but this thread is not running (stopped, halted, reset, or stopped on error) |
| 1 | This thread is running |

When a thread stops because of a run-time error, `ProgStat` returns to `0` and the cause is left in [ProgError](ProgError.md) for that thread. To distinguish a clean stop from an error stop, read `ProgError` for the same index.

## Examples

```text
AProgStat[1]        ; 1 if thread 1 is running, 0 if stopped, -1 if no program
```

## See also

- [ProgStatAll](ProgStatAll.md) — combined status of all threads
- [ProgError](ProgError.md) — last error code per thread
- [ProgRun](ProgRun.md) — run a task as a thread
- [ProgPointer](ProgPointer.md) — current position of each thread
