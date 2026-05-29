---
keyword: ProgArgLL
summary: "Reads a thread's current function argument slot as a 64-bit signed integer, from outside the function."
availability:
  standalone: []
  central-i:
  - v5
can_code: 787
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgArgLL

Reads a thread's current function argument slot as a 64-bit signed integer, from outside the function.

## Overview

`ProgArgLL` is the 64-bit signed integer form of [ProgArg](ProgArg.md). It reads the arguments of a thread's currently executing function from *outside* that function, returning the requested slot interpreted as a 64-bit signed integer. Like the base keyword it is indexed by thread number, with the argument position supplied as the command value, which makes it useful for monitoring and debugging when the value in that slot is a 64-bit integer. It is a non-axis parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

`ProgArgLL[thread], position` resolves against the named thread's current call-stack frame and returns the value at the given argument position, using the same numbering as [ProgArgThis](ProgArgThis.md): position `1` is the last value pushed before the call, position `2` the one before it, and so on, counting back through the staged arguments in reverse push order.

The only difference from [ProgArg](ProgArg.md) is the data type: `ProgArgLL` returns the slot as a 64-bit signed integer rather than a 32-bit integer. The underlying call-stack slot is the same; the typed forms simply let a host read it back as the type that was stored there. Use it when the slot was staged with [ProgPushArgLL](ProgPushArgLL.md) (or otherwise holds a 64-bit integer).

Because it reads the *current* frame of the selected thread, the value reflects whatever function that thread is executing at the moment of the query. Requesting a position beyond what the thread's current frame contains raises a "no operands in call stack" error.

## Examples

```text
AProgArgLL[1],1     ; read argument position 1 of the function running on thread 1 as a 64-bit integer
AProgArgLL[3],2     ; read argument position 2 of the function running on thread 3 as a 64-bit integer
```

## See also

- [ProgArg](ProgArg.md) — the base (32-bit integer) form
- [ProgArgF](ProgArgF.md) — 32-bit floating-point form
- [ProgArgD](ProgArgD.md) — 64-bit floating-point (double) form
- [ProgArgThisLL](ProgArgThisLL.md) — a function reading its own arguments as 64-bit integers
- [ProgPushArgLL](ProgPushArgLL.md) — stage a 64-bit integer argument before the call
