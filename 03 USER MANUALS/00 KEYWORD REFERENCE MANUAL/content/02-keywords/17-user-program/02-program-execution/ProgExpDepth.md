---
keyword: ProgExpDepth
summary: Returns the highest occupied location of the numeric (expression) stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 205
attributes:
  access: ro
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
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgExpDepth

Returns the highest occupied location of the numeric (expression) stack.

## Overview

`ProgExpDepth` is a low-level user-program keyword that returns the highest full location of the relevant numeric stack. An empty stack returns `-1`; with one value on the stack the highest full location is `0`, with two values it is `1`, and so on. It is mainly a debugging aid, complementing [ProgExpStack](ProgExpStack.md) (which reads the top value) and [ProgClrExp](ProgClrExp.md) (which clears the stack). It is a non-axis array parameter and is not saved to flash.

## Examples

```text
ProgExpDepth?       ; -1 if the numeric stack is empty, 0 if it holds one value
```

## See also

- [ProgExpStack](ProgExpStack.md) — read the top of the numeric stack without popping
- [ProgClrExp](ProgClrExp.md) — clear the numeric stack
- [Math](Math.md) — operate on values on the numeric stack
