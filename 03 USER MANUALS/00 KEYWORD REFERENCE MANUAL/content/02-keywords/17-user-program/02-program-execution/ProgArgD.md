---
keyword: ProgArgD
summary: Reads a thread's current function argument slot as a 64-bit floating-point (double) value, from outside the function.
availability:
  standalone: []
  central-i:
  - v5
can_code: 788
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 26
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgArgD

Reads a thread's current function argument slot as a 64-bit floating-point (double) value, from outside the function.

## Overview

`ProgArgD` is the double-precision floating-point form of [ProgArg](ProgArg.md). It reads the arguments of a thread's currently executing function from *outside* that function, returning the requested slot interpreted as a 64-bit floating-point (double) value. Like the base keyword it is indexed by thread number, with the argument position supplied as the command value, which makes it useful for monitoring and debugging when the value in that slot is a double. It is a non-axis parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

`ProgArgD[thread], position` resolves against the named thread's current call-stack frame and returns the value at the given argument position, using the same numbering as [ProgArgThis](ProgArgThis.md): position `1` is the last value pushed before the call, position `2` the one before it, and so on, counting back through the staged arguments in reverse push order.

The only difference from [ProgArg](ProgArg.md) is the data type: `ProgArgD` returns the slot as a 64-bit floating-point (double) value rather than a 32-bit integer. The underlying call-stack slot is the same; the typed forms simply let a host read it back as the type that was stored there. Use it when the slot was staged with [ProgPushArgD](ProgPushArgD.md) (or otherwise holds a double).

Because it reads the *current* frame of the selected thread, the value reflects whatever function that thread is executing at the moment of the query. Requesting a position beyond what the thread's current frame contains raises a "no operands in call stack" error.

## Examples

```text
AProgArgD[1],1      ; read argument position 1 of the function running on thread 1 as a double
AProgArgD[3],2      ; read argument position 2 of the function running on thread 3 as a double
```

## See also

- [ProgArg](ProgArg.md) — the base (32-bit integer) form
- [ProgArgF](ProgArgF.md) — 32-bit floating-point form
- [ProgArgLL](ProgArgLL.md) — 64-bit integer form
- [ProgArgThisD](ProgArgThisD.md) — a function reading its own arguments as doubles
- [ProgPushArgD](ProgPushArgD.md) — stage a double argument before the call
