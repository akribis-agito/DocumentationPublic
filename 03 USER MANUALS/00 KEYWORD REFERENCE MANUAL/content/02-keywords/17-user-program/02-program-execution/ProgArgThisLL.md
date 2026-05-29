---
keyword: ProgArgThisLL
summary: Reads or writes the current function's argument and local-variable slots as 64-bit signed integers.
availability:
  standalone: []
  central-i:
  - v5
can_code: 785
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 27
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgArgThisLL

Reads or writes the current function's argument and local-variable slots as 64-bit signed integers.

## Overview

`ProgArgThisLL` is the 64-bit signed integer form of [ProgArgThis](ProgArgThis.md). It gives the currently executing function access to its own arguments and local variables, reading and writing each slot as a 64-bit signed integer. It is the in-function view of the values staged with [ProgPushArgLL](ProgPushArgLL.md) before the call. Like the base keyword it is readable and writable, so the same slots also serve as the function's local-variable storage. It is a non-axis parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

A function's arguments live on the call stack relative to the current frame. `ProgArgThisLL[k]` addresses the slot `k` positions below the frame reference, exactly as [ProgArgThis](ProgArgThis.md) does:

- `ProgArgThisLL[1]` is the *last* value pushed with [ProgPushArgLL](ProgPushArgLL.md) before the call.
- `ProgArgThisLL[2]` is the value pushed before that, and so on, counting back through the staged arguments in reverse push order.

The only difference from [ProgArgThis](ProgArgThis.md) is the data type: `ProgArgThisLL` reads and writes the slot as a 64-bit signed integer rather than a 32-bit integer. The underlying call-stack slots are the same — the typed forms select how the bits in a slot are interpreted — so a function chooses the variant that matches the type it stored. Reading an index returns that slot's value; writing an index stores into it, which is how a function keeps local variables and prepares output values before [Return](Return.md). The index is resolved against the *current* frame, so the values automatically refer to the right function even when functions are nested.

Like the base keyword, `ProgArgThisLL` is only valid from within a running user program (it addresses the current call frame); issuing it from a plain communication command is rejected with a run-time error.

The array spans the function's combined argument and local-variable space (the sum of input arguments, output arguments and local variables for one function). Reading an index beyond what the current frame contains raises a "no operands in call stack" error.

## Examples

```text
AProgArgThisLL[1]   ; read the most-recently-pushed argument of this function as a 64-bit integer
AProgArgThisLL[2]   ; read the argument pushed before it as a 64-bit integer
AProgArgThisLL[3]=0 ; use the third slot as a 64-bit integer local variable
```

## See also

- [ProgArgThis](ProgArgThis.md) — the base (32-bit integer) form
- [ProgArgThisF](ProgArgThisF.md) — 32-bit floating-point form
- [ProgArgThisD](ProgArgThisD.md) — 64-bit floating-point (double) form
- [ProgPushArgLL](ProgPushArgLL.md) — stage a 64-bit integer argument before the call
- [ProgArgLL](ProgArgLL.md) — read another thread's argument slots as 64-bit integers from outside the function
