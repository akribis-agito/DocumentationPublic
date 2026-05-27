---
keyword: ProgExpDepth
summary: Returns the highest occupied location of the numeric (expression) stack.
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

Returns the highest occupied location of the numeric (expression) stack.

## Overview

`ProgExpDepth` is a low-level user-program keyword, indexed by thread, that reports the occupancy of a thread's numeric (expression) stack. An empty stack returns `-1`; with one value on the stack the highest full location is `0`, with two values it is `1`, and so on. It is mainly a debugging aid, complementing [ProgExpStack](ProgExpStack.md) (which reads a value without popping) and [ProgClrExp](ProgClrExp.md) (which clears the stack). It is a non-axis array parameter and is not saved to flash.

## How it works

Each thread has its own numeric stack, holding up to 50 values, on which expressions are built and evaluated (see [PushParam](../03-stack-operation/PushParam.md), [PushConstant](../03-stack-operation/PushConstant.md), [Math](Math.md) and [PopParam](../03-stack-operation/PopParam.md)). `ProgExpDepth[thread]` reports how full that stack is, tracking the highest occupied location: it starts at `-1` on a cleared or balanced stack, rises by one for each value pushed, and falls by one for each value popped.

A correctly balanced expression leaves the stack as it found it. Checking `ProgExpDepth` is therefore the quickest way to confirm an expression sequence is balanced — a value other than expected after a sequence of pushes and pops indicates a missing [PopParam](../03-stack-operation/PopParam.md) or an extra push, which would otherwise leave stale operands behind.

## Examples

```text
AProgExpDepth[1]    ; -1 if thread 1's numeric stack is empty, 0 if it holds one value
```

## See also

- [ProgExpStack](ProgExpStack.md) — read a value on the numeric stack without popping
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
- [Math](Math.md) — operate on values on the numeric stack
