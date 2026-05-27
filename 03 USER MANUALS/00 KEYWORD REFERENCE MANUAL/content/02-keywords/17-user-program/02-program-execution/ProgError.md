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

`ProgError` is a read-only array parameter, indexed by thread, that reports the interpreter error code raised by a user program thread. A value of `0` indicates no error. It is used together with [ProgStat](ProgStat.md) and [ProgStatAll](ProgStatAll.md) when diagnosing a thread that has stopped unexpectedly. It is a non-axis status variable and is not saved to flash.

> **Documentation pending:** The individual error codes are listed in the interpreter-errors table of the User Program Language Manual, which is not reproduced here.

## Examples

```text
AProgError[1]       ; interpreter error code for thread 1 (0 = no error)
```

## See also

- [ProgStat](ProgStat.md) — running status of a thread
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
- [ProgReset](ProgReset.md) — reset a task to its initial state
