---
keyword: ProgPointer
summary: Reports the current instruction pointer of each user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 279
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
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPointer

Reports the current instruction pointer of each user program task.

## Overview

`ProgPointer` is a read-only array parameter, indexed by task, that reports the current instruction pointer (program counter) of each user program task. A value of `-1` indicates no active position. It is the low-level counterpart of [ProgLine](ProgLine.md), which maps the same position back to a source line number, and is used during debugging together with [ProgBreakThis](ProgBreakThis.md) and [ProgStatAll](ProgStatAll.md). It is a non-axis status variable and is not saved to flash.

## Examples

```text
ProgPointer[1]?     ; instruction pointer of task 1 (-1 = no active position)
```

## See also

- [ProgLine](ProgLine.md) — current source line number
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
