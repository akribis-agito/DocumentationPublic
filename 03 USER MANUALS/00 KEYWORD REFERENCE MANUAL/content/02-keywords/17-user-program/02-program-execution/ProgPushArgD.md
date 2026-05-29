---
keyword: ProgPushArgD
summary: "Pushes a 64-bit floating-point (double) value onto the running thread's argument stack ahead of a function call."
availability:
  standalone: []
  central-i:
  - v5
can_code: 784
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPushArgD

Pushes a 64-bit floating-point (double) value onto the running thread's argument stack ahead of a function call.

## Overview

`ProgPushArgD` is the double-precision floating-point form of [ProgPushArg](ProgPushArg.md). It pushes a 64-bit floating-point (double) value onto the running thread's call stack to stage it as an argument for an upcoming function call. Each `ProgPushArgD` you issue before a [ProgFuncCall](ProgFuncCall.md) becomes one input argument that the called function reads with [ProgArgThisD](ProgArgThisD.md). It is a non-axis command and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

Arguments are passed on the call stack, not in dedicated registers. To call a function with arguments you push them first, then call:

1. Each `ProgPushArgD` pushes one value onto the current thread's call stack and tags that slot as an argument or local variable. The stack must have a free slot, otherwise the command fails with a stack-full error.
2. The subsequent [ProgFuncCall](ProgFuncCall.md) pushes the return address and frame location *above* the staged arguments, so the arguments end up just below the new frame.
3. Inside the function, [ProgArgThisD](ProgArgThisD.md) reads those slots relative to the frame: the last value pushed becomes `ProgArgThisD[1]`, the one pushed before it `ProgArgThisD[2]`, and so on.

The only difference from [ProgPushArg](ProgPushArg.md) is the data type pushed: `ProgPushArgD` stages a 64-bit floating-point (double) value rather than a 32-bit integer. The call-stack slot is the same; the typed forms simply control how the value is stored so the callee can read it back at full width with the matching variant. Like the base keyword, `ProgPushArgD` is only valid from within a running user program; issuing it from a plain communication command is rejected. The call stack holds up to 100 entries per thread; monitor free space with [ProgCallDepth](ProgCallDepth.md).

## Examples

```text
AProgPushArgD=1.5   ; stage 1.5 — becomes ProgArgThisD[2] in the callee
AProgPushArgD=2.5   ; stage 2.5 — becomes ProgArgThisD[1] in the callee
AProgFuncCall,1     ; call function 1 with the two staged arguments
```

## See also

- [ProgPushArg](ProgPushArg.md) — the base (32-bit integer) form
- [ProgPushArgF](ProgPushArgF.md) — 32-bit floating-point form
- [ProgPushArgLL](ProgPushArgLL.md) — 64-bit integer form
- [ProgArgThisD](ProgArgThisD.md) — read back the double argument inside the called function
- [ProgFuncCall](ProgFuncCall.md) — call a function with the staged arguments
