---
keyword: ProgStatAll
summary: Returns a combined status word for all user program tasks.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 298
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStatAll

Returns a combined status word for all user program tasks.

## Overview

`ProgStatAll` is a read-only parameter that returns a single value summarizing the execution state of all user program threads. It is the aggregate counterpart of [ProgStat](ProgStat.md), which reports one thread, and is useful for a quick health check of the whole program without reading each thread. It is a non-axis status variable and is not saved to flash.

## How it works

The controller recomputes this summary about once a second by scanning every thread. An error on any thread takes priority over any thread running, so the worst condition across all threads is the one reported:

| Value | Meaning |
|----|----|
| -1 | No user program loaded in the controller |
| 0 | Program loaded but no thread is running |
| 1 | At least one thread is running (and none has an error) |
| 2 | At least one thread has stopped on an error |

The summary is built by starting at `-1` (no program), promoting to `0` once a program is present, setting `1` if any thread's [ProgStat](ProgStat.md) is running, and setting `2` as soon as any thread is found with a non-zero [ProgError](ProgError.md). The error condition is detected from `ProgError`, not from any "error" value of `ProgStat` (which has none), so error (`2`) outranks running (`1`) regardless of the order in which threads are scanned.

A consequence worth noting: a thread that stopped on an error reads [ProgStat](ProgStat.md) `= 0` (its `ProgStat` was set to "not running" when it halted), yet `ProgStatAll` still reads `2` because the non-zero [ProgError](ProgError.md) is what raises the summary. When `ProgStatAll` reads `2`, read `ProgError` per thread to find which thread failed and why. Because it is updated on a one-second cycle, very short-lived run states may not always be visible here; for an immediate per-thread reading use [ProgStat](ProgStat.md).

## Examples

```text
AProgStatAll        ; -1 no program, 0 idle, 1 a thread running, 2 a thread errored
```

## See also

- [ProgStat](ProgStat.md) — running status of one thread
- [ProgError](ProgError.md) — last error code per thread
- [ProgPointer](ProgPointer.md) — current position of each thread
- [ProgReset](ProgReset.md) — reset a thread to its initial state
