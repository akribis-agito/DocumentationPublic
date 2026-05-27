---
keyword: ProgBreaks
summary: Per-thread breakpoint settings for user program debugging.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 294
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 4
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
# ProgBreaks

Per-thread breakpoint settings for user program debugging.

## Overview

`ProgBreaks` is a read/write array that holds up to **3 breakpoints** (indices `[1]`–`[3]`) used when debugging a user program. Each element holds a program location ([ProgPointer](ProgPointer.md) value) at which execution should stop; the default `-1` means the slot is empty. The breakpoints are global — they apply to whichever thread reaches the location — and are typically managed by the PC Suite debugger together with [ProgSingle](ProgSingle.md) (single-step) and [ProgBreakThis](ProgBreakThis.md) (break the currently running task). It is a non-axis parameter and is not saved to flash.

## How it works

Before executing the next instruction of any running thread, the controller compares that thread's current program location ([ProgPointer](ProgPointer.md)) against the `ProgBreaks` list. The list is scanned from index `[1]`; the first empty slot (`-1`) terminates the scan, so set breakpoints contiguously from `[1]`. If the thread's location matches a breakpoint, that thread is halted at that instruction: it stops running but keeps its state, so you can inspect it with [ProgPointer](ProgPointer.md), [ProgCallStack](ProgCallStack.md), and the program snapshot ([ProgSnapVal](ProgSnapVal.md)), then resume with [ProgRun](ProgRun.md) or step with [ProgSingle](ProgSingle.md).

A breakpoint hit on the very first instruction after a [ProgRun](ProgRun.md) or [ProgSingle](ProgSingle.md) command is ignored, so a thread sitting on a breakpoint can be resumed past it without immediately stopping again. Setting a slot to `-1` removes that breakpoint.

## Examples

```text
AProgBreaks[1]=<program location to break at>  ; set the first breakpoint
AProgBreaks[1]=-1                              ; clear the first breakpoint
AProgBreaks                                    ; read the breakpoint list
```

## See also

- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgSingle](ProgSingle.md) — single-step execution of a thread
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
