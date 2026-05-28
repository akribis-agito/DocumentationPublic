---
keyword: ProgExpDepth
summary: Reports the free space remaining in a thread's numeric (expression) stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 205
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
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
# ProgExpDepth

Reports the free space remaining in a thread's numeric (expression) stack.

## Overview

`ProgExpDepth` is a low-level user-program keyword, indexed by thread, that reports the number of empty (free) slots remaining in a thread's numeric (expression) stack. A freshly cleared stack reports 50 (its full capacity) and the value falls by one for each value pushed. It is mainly a debugging aid, complementing [ProgExpStack](ProgExpStack.md) (which reads a value without popping) and [ProgClrExp](ProgClrExp.md) (which clears the stack). It is a non-axis array parameter and is not saved to flash.

## How it works

Each thread has its own numeric stack, holding up to 50 values, on which expressions are built and evaluated (see [PushParam](../03-stack-operation/PushParam.md), [PushConstant](../03-stack-operation/PushConstant.md), [Math](Math.md) and [PopParam](../03-stack-operation/PopParam.md)). `ProgExpDepth[thread]` returns *free* slots — the capacity (50) minus the slots currently in use — so it starts at `50` on a cleared or balanced stack, falls by one for each value pushed, and rises by one for each value popped.

A correctly balanced expression leaves the stack as it found it. Checking `ProgExpDepth` is therefore the quickest way to confirm an expression sequence is balanced — a value other than expected after a sequence of pushes and pops indicates a missing [PopParam](../03-stack-operation/PopParam.md) or an extra push, which would otherwise leave stale operands behind.

## Examples

```text
AProgExpDepth[1]    ; free numeric-stack slots for thread 1 (50 when empty, 49 with one value)
```

## See also

- [ProgExpStack](ProgExpStack.md) — read a value on the numeric stack without popping
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
- [Math](Math.md) — operate on values on the numeric stack
