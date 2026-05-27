---
keyword: ProgExpStack
summary: Reads the top value of the numeric (expression) stack without popping it.
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

Reads the top value of the numeric (expression) stack without popping it.

## Overview

`ProgExpStack` is a low-level user-program keyword used to read the top number of the numeric stack without popping it. It is most useful for debugging, where you want to inspect what an expression has produced without disturbing the stack. Use [ProgExpDepth](ProgExpDepth.md) to find how many values are present and [ProgClrExp](ProgClrExp.md) to clear the stack. It is a non-axis array parameter and is not saved to flash.

## Examples

```text
AProgExpStack       ; peek at the top value of the numeric stack (does not pop)
```

## See also

- [ProgExpDepth](ProgExpDepth.md) — highest occupied location of the numeric stack
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
- [PopParam](../03-stack-operation/PopParam.md) — pop the top stack value into a parameter
