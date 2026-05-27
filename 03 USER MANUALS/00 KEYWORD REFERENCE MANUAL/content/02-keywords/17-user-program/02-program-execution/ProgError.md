---
keyword: ProgError
summary: Reports the last interpreter error code for each user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 199
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgError

Reports the last interpreter error code for each user program thread.

## Overview

`ProgError` is a read-only array parameter, indexed by thread, that reports the error code raised the last time a user program thread stopped on an error. A value of `0` indicates no error. It is used together with [ProgStat](ProgStat.md) and [ProgStatAll](ProgStatAll.md) when diagnosing a thread that has stopped unexpectedly. Index it `[1]` to `[8]` (or `[12]` on a Central-i master). It is a non-axis status variable and is not saved to flash.

## How it works

When an instruction in a thread fails — for example a stack overflow or underflow, a call to a task or function that does not exist, or any other run-time fault — the controller:

1. Stores the error code in `ProgError` for that thread.
2. Halts that thread and sets its [ProgStat](ProgStat.md) to `0` (not running), leaving its [ProgPointer](ProgPointer.md) on the failing instruction so it can be examined or re-executed.
3. Adds the error to the controller error log, tagged as coming from the user program thread, so it also appears in [ErrLog](../../07-status-and-faults/ErrLog.md). In `ErrLog` a user-program error is tagged with source `16 + n` (for example `17` for thread 1).

`ProgError` holds the value until the thread is run again — starting or stepping a thread with [ProgRun](ProgRun.md) or [ProgSingle](ProgSingle.md), or resetting it with [ProgReset](ProgReset.md), clears its error back to `0`. The error stays latched for inactive threads, so it can be read after the fact. Because an error on any thread also drives [ProgStatAll](ProgStatAll.md) to `2`, that aggregate value is a quick way to detect that some thread needs `ProgError` inspected.

> **Note:** The individual error code numbers are defined in the User Program Language Manual and are not reproduced in this reference.

## Examples

```text
AProgError[1]       ; error code for thread 1 (0 = no error)
```

## See also

- [ProgStat](ProgStat.md) — running status of a thread
- [ProgStatAll](ProgStatAll.md) — combined status of all threads (2 = a thread errored)
- [ProgPointer](ProgPointer.md) — position left on the failing instruction
- [ProgReset](ProgReset.md) — reset a thread (clears its error)
- [ErrLog](../../07-status-and-faults/ErrLog.md) — controller error log; user-program errors appear tagged by thread
