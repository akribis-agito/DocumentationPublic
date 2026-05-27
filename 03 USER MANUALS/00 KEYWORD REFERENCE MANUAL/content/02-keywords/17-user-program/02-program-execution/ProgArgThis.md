---
keyword: ProgArgThis
summary: Reads back the argument values received by the currently executing task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 433
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 27
---
# ProgArgThis

Reads back the argument values received by the currently executing task.

## Overview

`ProgArgThis` is an array parameter that gives the currently executing function access to its own arguments and local variables. It is the in-function view of the values staged with [ProgPushArg](ProgPushArg.md) before the call. `ProgArgThis` is readable and writable, so the same array also serves as the function's local-variable storage. It is a non-axis parameter and is not saved to flash.

## How it works

A function's arguments live on the call stack relative to the current frame. `ProgArgThis[k]` addresses the slot `k` positions below the frame reference, so:

- `ProgArgThis[1]` is the *last* value pushed with [ProgPushArg](ProgPushArg.md) before the call.
- `ProgArgThis[2]` is the value pushed before that, and so on, counting back through the staged arguments in reverse push order.

Reading an index returns that slot's value; writing an index stores into it, which is how a function keeps local variables and how it prepares output values before [Return](Return.md). The index is resolved against the *current* frame, so the values automatically refer to the right function even when functions are nested.

The array spans the function's combined argument and local-variable space: up to 20 entries on smaller models and up to 26 on larger ones (the sum of input arguments, output arguments and local variables for one function). Reading an index beyond what the current frame contains raises a "no operands in call stack" error.

The integer form shown here is the most common; matching variant keywords read or write the same slots as floating-point, 64-bit integer or double-precision values.

## Examples

```text
AProgArgThis[1]     ; read the most-recently-pushed argument of this function
AProgArgThis[2]     ; read the argument pushed before it
AProgArgThis[3]=0   ; use the third slot as a local variable
```

## See also

- [ProgPushArg](ProgPushArg.md) — stage an argument before the call
- [ProgFuncCall](ProgFuncCall.md) — call a function
- [ProgArg](ProgArg.md) — read another thread's argument slots from outside the function
- [Return](Return.md) — return output values to the caller
