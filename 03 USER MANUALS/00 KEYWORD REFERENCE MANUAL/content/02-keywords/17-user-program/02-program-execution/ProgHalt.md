---
keyword: ProgHalt
summary: Halts a specified user program thread; it can later be resumed where it stopped.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 197
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
  implemented: partial
overrides: {}
---
# ProgHalt

Halts a specified user program thread; it can later be resumed where it stopped.

## Overview

`ProgHalt[Thread no.]` halts the specified thread number. Halting is not the same as resetting: if [ProgRun](ProgRun.md) is issued again for the same thread, execution continues from the point where it was halted. To halt every active thread at once use [ProgHaltAll](ProgHaltAll.md), or [ProgHaltThis](ProgHaltThis.md) for the running task. It is also placed at the end of a non-looping program so execution does not run on into the function definitions (see [ProgFunc](ProgFunc.md)). It is a non-axis command and is not saved to flash.

## Examples

```text
AProgHalt[1]        ; halt thread 1; ProgRun[1] later resumes from this point
```

## See also

- [ProgRun](ProgRun.md) — run/resume a thread
- [ProgHaltAll](ProgHaltAll.md) — halt all active threads
- [ProgHaltThis](ProgHaltThis.md) — halt the running task
- [ProgReset](ProgReset.md) — reset a task (not the same as halting)
