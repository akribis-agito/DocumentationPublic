---
keyword: ProgCallStack
summary: Program-call stack contents for a user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 276
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
  - 99
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgCallStack

Program-call stack contents for a user program thread.

## Overview

`ProgCallStack` is an array parameter, indexed by thread, that exposes the raw contents of a thread's program-call stack — the structure built up when functions are invoked with [ProgFuncCall](ProgFuncCall.md) and unwound by [Return](Return.md). Each call adds a frame holding the staged arguments, the return address and the caller's frame reference. Use [ProgCallDepth](ProgCallDepth.md) to check how much free space remains, and [ProgClrCall](ProgClrCall.md) to clear it. It is primarily a debugging aid. It is a non-axis parameter and is not saved to flash.

## How it works

`ProgCallStack[thread], location` reads one stack slot of the selected thread by its absolute location (counted from the base of the stack, not relative to the current frame). Locations run from `0` up to the highest occupied slot; the stack holds up to 100 slots per thread. The reading is non-destructive — it does not change the stack.

The value returned depends on what the slot holds:

- **Return address** — reported as an offset, in the same units as [ProgPointer](ProgPointer.md), from the start of the program. This is the line execution will resume on when the matching [Return](Return.md) runs.
- **Argument, local variable, or frame reference** — reported as the stored value as-is. A slot holding a floating-point argument is returned as the raw bit pattern, which the host interprets as a float.

Reading a location above the highest occupied slot, or outside the `0`–99 range, raises a stack-range error.

## Examples

```text
AProgCallStack[1],0     ; read the deepest occupied slot of thread 1
AProgCallStack[1],1     ; read the next slot up
```

## See also

- [ProgCallDepth](ProgCallDepth.md) — free space remaining in the call stack
- [ProgClrCall](ProgClrCall.md) — clear the program-call stack
- [ProgFuncCall](ProgFuncCall.md) — call a user program function
- [Return](Return.md) — return from a function call
- [ProgPointer](ProgPointer.md) — current execution offset within the program
