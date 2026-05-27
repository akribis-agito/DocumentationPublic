---
summary: Label keyword marking the start of a callable user program task.
---
# ProgTask

Label keyword marking the start of a callable user program task.

## Overview

`ProgTask` is used as a label in user programs, marking the entry point of a task. A task is started by [ProgRun](ProgRun.md) using `AProgRun[thread], task no.`, which runs the code after the matching `AProgTask[task no.]` label under the assigned thread number until a [ProgHalt](ProgHalt.md) is reached. Tasks differ from functions ([ProgFunc](ProgFunc.md)) in that they are launched as threads rather than called and returned from.

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
- [ProgHalt](ProgHalt.md) — halt a thread (end of a non-looping task)
- [ProgFunc](ProgFunc.md) — label for a callable function
