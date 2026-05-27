---
keyword: ProgRun
summary: Runs (or resumes) a task as a given thread number.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 198
attributes:
  access: rw
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
  - 254
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgRun

Runs (or resumes) a task as a given thread number.

## Overview

`ProgRun[Thread no.], Task no.` runs the requested task as the given thread number. To run the "main" program — the code that starts at the beginning of the file — use `-1` as the task number. If the thread was previously stopped with [ProgHalt](ProgHalt.md), `ProgRun` resumes it from where it was halted rather than restarting it; use [ProgReset](ProgReset.md) first to start from the beginning. Tasks are defined by [ProgTask](ProgTask.md) labels, and their priority is set by [ProgPriority](ProgPriority.md). It is a non-axis command and is not saved to flash.

## Examples

```text
AProgRun[3],5       ; run task 5 as thread 3
AProgRun[1],-1      ; run the main program as thread 1
```

## See also

- [ProgTask](ProgTask.md) — label marking the start of a task
- [ProgHalt](ProgHalt.md) — halt a thread (resumable by ProgRun)
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgPriority](ProgPriority.md) — task scheduling priority
