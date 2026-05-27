---
keyword: ProgSingle
summary: Single-steps a user program thread (debugger step into / step over).
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgSingle` is a user-program command, normally issued by the PC Suite, that executes the next line of a thread and then halts — the basis for debugger stepping. The form `ProgSingle[thread],0` behaves like "step into", while `ProgSingle[thread],1` behaves like "step over" for internal wait loops. It is used together with breakpoints set by [ProgBreakThis](ProgBreakThis.md) and position readouts from [ProgPointer](ProgPointer.md) / [ProgLine](ProgLine.md). It is a non-axis command and is not saved to flash.

## How it works

| Second argument | Behaviour |
|----|----|
| 0 | Execute the next line and halt — debugger "step into" |
| 1 | Equivalent to debugger "step over" for internal wait loops |

## Examples

```text
AProgSingle[1],0    ; step into: execute the next line of thread 1, then halt
AProgSingle[1],1    ; step over internal wait loops in thread 1
```

## See also

- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
- [ProgLine](ProgLine.md) — current source line number
