---
keyword: ProgExpStack
summary: Reads a value on the numeric (expression) stack without popping it.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 204
attributes:
  access: rw
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
  - 51
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgExpStack

Reads a value on the numeric (expression) stack without popping it.

## Overview

`ProgExpStack` is a low-level user-program keyword, indexed by thread, used to read a value on the numeric (expression) stack without popping it. It is most useful for debugging, where you want to inspect what an expression has produced without disturbing the stack. Use [ProgExpDepth](ProgExpDepth.md) to find how many values are present and [ProgClrExp](ProgClrExp.md) to clear the stack. It is a non-axis array parameter and is not saved to flash.

## How it works

`ProgExpStack[thread], location` reads one location of the selected thread's numeric stack by its position, counted from the base (location `0` is the deepest value). The read is non-destructive — the stack contents and depth are unchanged.

Locations are valid from `0` up to the highest occupied location; the stack holds up to 50 values. Reading a location above the current top, or outside the valid range, raises a stack-range error. [ProgExpDepth](ProgExpDepth.md) reports how many slots are still free, so the highest occupied location is `50` minus the free count, minus one. A location holding a floating-point value is returned as a raw bit pattern for the host to interpret as a float; matching variant keywords read the same locations directly as floating-point, 64-bit integer or double-precision.

## Examples

```text
AProgExpStack[1],0  ; read the deepest value on thread 1's numeric stack
```

## See also

- [ProgExpDepth](ProgExpDepth.md) — free space remaining in the numeric stack
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
- [PopParam](../03-stack-operation/PopParam.md) — pop the top stack value into a parameter
