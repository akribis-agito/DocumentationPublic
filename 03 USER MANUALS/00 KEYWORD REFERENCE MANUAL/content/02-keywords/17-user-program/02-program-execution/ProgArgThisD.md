---
keyword: ProgArgThisD
summary: "Reads or writes the current function's argument and local-variable slots as 64-bit floating-point (double) values."
availability:
  standalone: []
  central-i:
  - v5
can_code: 786
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgArgThisD

Reads or writes the current function's argument and local-variable slots as 64-bit floating-point (double) values.

## Overview

`ProgArgThisD` is the double-precision floating-point form of [ProgArgThis](ProgArgThis.md). It gives the currently executing function access to its own arguments and local variables, reading and writing each slot as a 64-bit floating-point (double) value. It is the in-function view of the values staged with [ProgPushArgD](ProgPushArgD.md) before the call. Like the base keyword it is readable and writable, so the same slots also serve as the function's local-variable storage. It is a non-axis parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

A function's arguments live on the call stack relative to the current frame. `ProgArgThisD[k]` addresses the slot `k` positions below the frame reference, exactly as [ProgArgThis](ProgArgThis.md) does:

- `ProgArgThisD[1]` is the *last* value pushed with [ProgPushArgD](ProgPushArgD.md) before the call.
- `ProgArgThisD[2]` is the value pushed before that, and so on, counting back through the staged arguments in reverse push order.

The only difference from [ProgArgThis](ProgArgThis.md) is the data type: `ProgArgThisD` reads and writes the slot as a 64-bit floating-point (double) value rather than a 32-bit integer. The underlying call-stack slots are the same — the typed forms select how the bits in a slot are interpreted — so a function chooses the variant that matches the type it stored. Reading an index returns that slot's value; writing an index stores into it, which is how a function keeps local variables and prepares output values before [Return](Return.md). The index is resolved against the *current* frame, so the values automatically refer to the right function even when functions are nested.

The array spans the function's combined argument and local-variable space (the sum of input arguments, output arguments and local variables for one function). Reading an index beyond what the current frame contains raises a "no operands in call stack" error.

## Examples

```text
AProgArgThisD[1]    ; read the most-recently-pushed argument of this function as a double
AProgArgThisD[2]    ; read the argument pushed before it as a double
AProgArgThisD[3]=0  ; use the third slot as a double local variable
```

## See also

- [ProgArgThis](ProgArgThis.md) — the base (32-bit integer) form
- [ProgArgThisF](ProgArgThisF.md) — 32-bit floating-point form
- [ProgArgThisLL](ProgArgThisLL.md) — 64-bit integer form
- [ProgPushArgD](ProgPushArgD.md) — stage a double argument before the call
- [ProgArgD](ProgArgD.md) — read another thread's argument slots as doubles from outside the function
