---
keyword: ProgPushArg
summary: Pushes a value onto the argument stack of a target user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 431
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPushArg

Pushes a value onto the argument stack of a target user program task.

## Overview

`ProgPushArg` pushes a value onto the running thread's call stack to stage it as an argument for an upcoming function call. Each `ProgPushArg` you issue before a [ProgFuncCall](ProgFuncCall.md) becomes one input argument that the called function reads with [ProgArgThis](ProgArgThis.md). It is a non-axis command and is not saved to flash.

## How it works

Arguments are passed on the call stack, not in dedicated registers. To call a function with arguments you push them first, then call:

1. Each `ProgPushArg` pushes one value onto the current thread's call stack and tags that slot as an argument or local variable. The stack must have a free slot, otherwise the command fails with a stack-full error.
2. The subsequent [ProgFuncCall](ProgFuncCall.md) pushes the return address and frame location *above* the staged arguments, so the arguments end up just below the new frame.
3. Inside the function, [ProgArgThis](ProgArgThis.md) reads those slots relative to the frame: the last value pushed becomes `ProgArgThis[1]`, the one pushed before it `ProgArgThis[2]`, and so on.

`ProgPushArg` stages an integer. Floating-point, 64-bit integer and double-precision values are staged the same way using the matching variant keywords; the value is stored as the function's argument regardless of type. The call stack holds up to 100 entries per thread; monitor free space with [ProgCallDepth](ProgCallDepth.md).

## Examples

```text
AProgPushArg=10     ; stage 10 — becomes ProgArgThis[2] in the callee
AProgPushArg=20     ; stage 20 — becomes ProgArgThis[1] in the callee
AProgFuncCall,1     ; call function 1 with the two staged arguments
```

## See also

- [ProgFuncCall](ProgFuncCall.md) — call a function with the staged arguments
- [ProgArgThis](ProgArgThis.md) — read back the arguments inside the called function
- [ProgArg](ProgArg.md) — read a thread's argument slots from outside the function
- [ProgCallDepth](ProgCallDepth.md) — free space remaining in the call stack
