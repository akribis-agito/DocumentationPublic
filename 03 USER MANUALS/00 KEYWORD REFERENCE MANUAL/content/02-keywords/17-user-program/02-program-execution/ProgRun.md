---
keyword: ProgRun
summary: Runs (or resumes) a task as a given thread number.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgRun[Thread no.], Task no.` starts (or resumes) a user program task on the given thread. The controller can run several user program threads at once, each with its own program pointer, call stack and numeric stack, so independent tasks can run side by side. `ProgRun` selects which thread to drive (the array index) and which task that thread should execute (the value). It is a non-axis command and is not saved to flash.

## How it works

The controller runs user program threads under a built-in round-robin scheduler. There are up to **8 threads** on a standalone controller and up to **12** on a Central-i master; index them `[1]` through `[8]` (or `[12]`). On each scheduler pass the controller advances every active thread by **one low-level instruction**, so the threads share the processor cooperatively. How often each thread is serviced relative to the others is governed by [ProgPriority](ProgPriority.md).

The **value** passed to `ProgRun` chooses the task:

| Task value | Effect |
|----|----|
| 0 | **Resume** the thread from where it currently sits — used to continue a thread that was paused with [ProgHalt](ProgHalt.md). The pointer and stacks are left untouched. |
| 1 | Run the **main program** (task 1) — the code that starts at the beginning of the program file. |
| 2 to 30 (standalone) or 2 to 254 (Central-i master) | Run that numbered task. Tasks are marked by [ProgTask](ProgTask.md) labels. |

When a task value of 1–30 (standalone) or 1–254 (Central-i master) is given, the thread is first re-initialized (pointer set to the start of that task, call and numeric stacks cleared, error cleared) and then started — a clean run from the task entry point. A task value of 0 instead leaves all thread state in place and simply re-enables execution, which is what makes a halted thread continue from the exact instruction where it stopped. To force a paused thread to start over from the beginning instead of resuming, use [ProgReset](ProgReset.md) first.

`ProgRun` is rejected with an error if there is no stored program, if the stored program fails its checksum, if the requested task does not exist, or if the requested thread is already running. While a thread runs, [ProgStat](ProgStat.md) reports `1` for that thread and [ProgPointer](ProgPointer.md) tracks its position.

## Examples

```text
AProgRun[1],1       ; run the main program (task 1) as thread 1
AProgRun[3],5       ; run task 5 as thread 3
AProgRun[1],0       ; resume thread 1 from where ProgHalt stopped it
```

## See also

- [ProgTask](ProgTask.md) — label marking the start of a task
- [ProgHalt](ProgHalt.md) — pause a thread (resumable with `ProgRun[thread],0`)
- [ProgReset](ProgReset.md) — reset a thread so the next run starts from the beginning
- [ProgPriority](ProgPriority.md) — how often each thread is serviced by the scheduler
- [ProgStat](ProgStat.md) — running status of a thread
- [AutoExec](../../01-system/02-operation/AutoExec.md) — run the main program automatically at start-up
