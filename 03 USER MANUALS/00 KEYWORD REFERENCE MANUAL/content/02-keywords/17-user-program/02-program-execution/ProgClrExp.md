---
keyword: ProgClrExp
summary: Clears the numeric (expression) stack of the current thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 203
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
# ProgClrExp

Clears the numeric (expression) stack of the current thread.

## Overview

`ProgClrExp` is a low-level user-program keyword, indexed by thread, that clears the numeric (expression) stack. It is recommended to begin a new program with `ProgClrExp` so that no stale values left by [PushParam](../03-stack-operation/PushParam.md), [PushConstant](../03-stack-operation/PushConstant.md), or [Math](Math.md) operations remain on the stack. It is the expression-stack counterpart of [ProgClrCall](ProgClrCall.md), which clears the program-call stack. It is a non-axis command and is not saved to flash.

## How it works

The numeric stack is where expressions are evaluated: keywords such as [PushParam](../03-stack-operation/PushParam.md) and [PushConstant](../03-stack-operation/PushConstant.md) push operands, [Math](Math.md) pops operands and pushes the result, and [PopParam](../03-stack-operation/PopParam.md) pops the final value into a parameter. There is one such stack per thread, holding up to 50 values.

`ProgClrExp[thread]` empties that stack in one step by marking it as having no occupied locations. It does not change any value already popped into a parameter; it only discards whatever operands are still on the stack. This is the clean-slate operation to run at the start of a program so that a leftover operand from a previous run cannot corrupt the first expression — for example an expression that ends without a matching `PopParam`, or a sequence interrupted partway through.

## Examples

```text
AProgClrExp[1]      ; clear the numeric stack of thread 1 at program start
```

## See also

- [ProgExpStack](ProgExpStack.md) — read a value on the numeric stack without popping
- [ProgExpDepth](ProgExpDepth.md) — free space remaining in the numeric stack
- [PopParam](../03-stack-operation/PopParam.md) — pop the top stack value into a parameter
- [ProgClrCall](ProgClrCall.md) — clear the program-call stack
