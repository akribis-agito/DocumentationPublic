---
summary: Label keyword marking the start of a callable user program task.
---
# ProgTask

Label keyword marking the start of a callable user program task.

## Overview

`ProgTask` is used as a label in user programs, marking the entry point of a task. A task is started by [ProgRun](ProgRun.md) using `AProgRun[thread], task no.`, which runs the code after the matching `AProgTask[task no.]` label under the assigned thread number until a [ProgHalt](ProgHalt.md) is reached. Tasks differ from functions ([ProgFunc](ProgFunc.md)) in that they are launched as threads rather than called and returned from.

## How it works

`ProgTask[]` is a label marking a program location, not an executed command — it records where a task begins so that [ProgRun](ProgRun.md) can launch it by index. The distinction between a task and a function is how it is entered:

- A **task** ([ProgTask](ProgTask.md)) is *launched as a thread* by [ProgRun](ProgRun.md). It then runs concurrently with other threads, each thread getting a share of execution time governed by [ProgPriority](ProgPriority.md). A task is the unit of independent, parallel execution.
- A **function** ([ProgFunc](ProgFunc.md)) is *called and returned from* within a single thread via [ProgFuncCall](ProgFuncCall.md) / [Return](Return.md), using that thread's call stack.

Task and thread numbers are independent: the task number selects which `ProgTask[]` label to run, and the thread number is the slot it runs in. The same task may be run in different threads, and the special task number `-1` runs the main program (the code at the start of the file); see [ProgRun](ProgRun.md). A task ends at [ProgHalt](ProgHalt.md); without it, execution simply continues into the following lines of the file.

> **Note:** If `ProgHalt` is not used, execution continues linearly into the next line in the file.

## Examples

```text
AProgTask[5]        ; label: start of task 5
; the body of task 5
AProgHalt[3]        ; stop when run as thread 3

AProgRun[3],5       ; elsewhere: run task 5 as thread 3
```

## See also

- [ProgRun](ProgRun.md) — run a task as a thread
- [ProgPriority](ProgPriority.md) — scheduling share of a running thread
- [ProgHalt](ProgHalt.md) — halt a thread (end of a non-looping task)
- [ProgFunc](ProgFunc.md) — label for a callable function
