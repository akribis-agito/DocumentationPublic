---
keyword: ProgSingle
summary: Single-steps a user program thread (debugger step into / step over).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 191
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
  - 1
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgSingle

Single-steps a user program thread (debugger step into / step over).

## Overview

`ProgSingle[Thread no.], Step type` advances a thread by a single step and then pauses it — the basis for debugger stepping, normally issued by the Agito PCSuite. The step type selects "step into" or "step over". It is used together with breakpoints set by [ProgBreakThis](ProgBreakThis.md) and the position readouts [ProgPointer](ProgPointer.md) and [ProgLine](ProgLine.md). It is a non-axis command and is not saved to flash.

## How it works

`ProgSingle` re-enables the chosen thread for just one step, then the scheduler halts it again and sets its [ProgStat](ProgStat.md) back to `0` (not running). Like a resume, it does not disturb the thread's pointer or stacks, so stepping picks up exactly where the thread last stopped. The thread's [ProgError](ProgError.md) is cleared at the start of each step.

| Step type | Behaviour |
|----|----|
| 0 | **Step into** — execute the next single low-level instruction, then halt |
| 1 | **Step over** — keep executing until the program pointer advances, then halt; this steps over internal wait loops (such as a wait condition that re-executes the same line) instead of stopping inside them |

When `ProgSingle` is issued from a communication terminal it temporarily ignores any breakpoint that sits on the very next instruction, so stepping is not blocked by a breakpoint at the current position. The command is rejected if there is no stored program, if the stored program fails its checksum, if the thread is already running, or if the thread pointer is already past the end of the program.

## Examples

```text
AProgSingle[1],0    ; step into: execute the next line of thread 1, then halt
AProgSingle[1],1    ; step over internal wait loops in thread 1
```

## See also

- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
- [ProgLine](ProgLine.md) — current source line number
