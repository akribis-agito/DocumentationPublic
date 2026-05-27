---
keyword: ProgClrExp
summary: Clears the numeric (expression) stack of the current thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgClrExp` is a low-level user-program keyword that clears the numeric stack of the current thread. It is recommended to begin a new program with `ProgClrExp` so that no stale values left by [PushParam](../03-stack-operation/PushParam.md), [PushConstant](../03-stack-operation/PushConstant.md), or [Math](Math.md) operations remain on the stack. It is the expression-stack counterpart of [ProgClrCall](ProgClrCall.md), which clears the program-call stack. It is a non-axis command and is not saved to flash.

## Examples

```text
AProgClrExp          ; clear the numeric stack at program start
```

## See also

- [ProgExpStack](ProgExpStack.md) — read the top of the numeric stack without popping
- [ProgExpDepth](ProgExpDepth.md) — highest occupied location of the numeric stack
- [ProgClrCall](ProgClrCall.md) — clear the program-call stack
