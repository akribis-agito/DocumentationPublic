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

When `ProgStatAll` reads `2`, read [ProgStat](ProgStat.md) and [ProgError](ProgError.md) per thread to find which thread failed and why. Because it is updated on a one-second cycle, very short-lived run states may not always be visible here; for an immediate per-thread reading use [ProgStat](ProgStat.md).

## Examples

```text
AProgStatAll        ; -1 no program, 0 idle, 1 a thread running, 2 a thread errored
```

## See also

- [ProgStat](ProgStat.md) — running status of one thread
- [ProgError](ProgError.md) — last error code per thread
- [ProgPointer](ProgPointer.md) — current position of each thread
- [ProgReset](ProgReset.md) — reset a thread to its initial state
