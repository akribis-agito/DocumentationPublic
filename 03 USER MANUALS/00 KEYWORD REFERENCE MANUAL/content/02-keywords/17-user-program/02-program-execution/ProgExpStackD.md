---
keyword: ProgExpStackD
summary: Reads a value on the numeric (expression) stack as a 64-bit floating-point (double), without popping it.
availability:
  standalone: []
  central-i:
  - v5
can_code: 794
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 51
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgExpStackD

Reads a value on the numeric (expression) stack as a 64-bit floating-point (double), without popping it.

## Overview

`ProgExpStackD` is the double-precision floating-point form of [ProgExpStack](ProgExpStack.md). Indexed by thread, it reads one value on the numeric (expression) stack and returns it interpreted as a 64-bit floating-point (double), without popping it. It is most useful for debugging, where you want to inspect what an expression has produced without disturbing the stack. Use [ProgExpDepth](ProgExpDepth.md) to find how much space is free and [ProgClrExp](ProgClrExp.md) to clear the stack. It is a non-axis array parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

`ProgExpStackD[thread], location` reads one location of the selected thread's numeric stack by its position, counted from the base (location `0` is the deepest value). The read is non-destructive — the stack contents and depth are unchanged.

The only difference from [ProgExpStack](ProgExpStack.md) is the data type returned: `ProgExpStackD` reports the location directly as a 64-bit floating-point (double) value, rather than as a 32-bit integer or a raw bit pattern. The underlying stack location is the same; the typed forms simply control how the bits are interpreted, so use the variant that matches the type the value was stored as.

Locations are valid from `0` up to the highest occupied location; the stack holds up to 50 values. Reading a location above the current top, or outside the valid range, raises a stack-range error. [ProgExpDepth](ProgExpDepth.md) reports how many slots are still free, so the highest occupied location is `50` minus the free count, minus one.

## Examples

```text
AProgExpStackD[1],0 ; read the deepest value on thread 1's numeric stack as a double
```

## See also

- [ProgExpStack](ProgExpStack.md) — the base (32-bit integer) form
- [ProgExpStackF](ProgExpStackF.md) — 32-bit floating-point form
- [ProgExpStckLL](ProgExpStckLL.md) — 64-bit integer form
- [ProgExpDepth](ProgExpDepth.md) — free space remaining in the numeric stack
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
