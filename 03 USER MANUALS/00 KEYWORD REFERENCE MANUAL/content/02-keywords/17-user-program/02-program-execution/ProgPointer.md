---
keyword: ProgPointer
summary: Reports the current instruction pointer of each user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgPointer` is a read-only array parameter, indexed by thread, that reports the current instruction pointer (program counter) of each user program thread. A value of `-1` indicates there is no program. It is the low-level counterpart of [ProgLine](ProgLine.md), which maps the same position back to a human-readable source line, and is used during debugging together with [ProgBreaks](ProgBreaks.md)/[ProgBreakThis](ProgBreakThis.md) and [ProgStat](ProgStat.md). Index it `[1]` to `[8]` (or `[12]` on a Central-i master). It is a non-axis status variable and is not saved to flash.

## How it works

The pointer is reported as a **byte offset from the start of the stored program** (range `-1` to 2147483647):

| Value | Meaning |
|----|----|
| -1 | No user program loaded |
| 0 and up | Offset, in bytes, of the next instruction the thread will execute |

After each instruction completes, the controller advances the thread's pointer to the next instruction, so reading `ProgPointer` while a thread runs tracks its progress. Two cases hold the pointer in place rather than advancing it:

- **On a run-time error**, the pointer is left on the failing instruction (see [ProgError](ProgError.md)), so it can be inspected or re-executed.
- **On [ProgHaltThis](ProgHaltThis.md)**, the pointer is held on the halt instruction so execution does not run on; a later resume continues from the instruction after it.

Breakpoints from [ProgBreaks](ProgBreaks.md) are matched against this same offset: when a thread's pointer reaches a breakpoint value, the thread is halted. Resetting a thread with [ProgReset](ProgReset.md) sets its pointer back to the start of the main program.

## Examples

```text
AProgPointer[1]     ; byte offset of thread 1's next instruction (-1 = no program)
```

## See also

- [ProgLine](ProgLine.md) — same position expressed as a source line number
- [ProgStat](ProgStat.md) — running status of a thread
- [ProgError](ProgError.md) — pointer is held here on a run-time error
- [ProgBreaks](ProgBreaks.md) — breakpoints matched against this offset
