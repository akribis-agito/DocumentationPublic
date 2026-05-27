---
keyword: Math
summary: Low-level user-program op that applies a math operation to the top of the numeric stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 206
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 32
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
# Math

Low-level user-program op that applies a math operation to the top of the numeric stack.

## Overview

`Math` is a low-level user-program keyword. The syntax around `Math` is normally generated automatically by the PC Suite during compilation, so it is rarely written by hand. `Math` performs the requested operation on the top one or two values of the numeric stack — the operands must be pushed first (see [PushParam](../03-stack-operation/PushParam.md) and [PushConstant](../03-stack-operation/PushConstant.md)), and the result is pushed back onto the stack. When `Math` is called over communication, the result is also returned through the communication channel.

Values on the stack and over communication are integers; fractional results are rounded. Internally all operations are performed on `long long` variables, with definitions compatible with C.

> **Note:** `Pop1` is the first value popped from the stack (the "top" value); `Pop2` is the second value popped.

## How it works

The index selects which operation is performed; the number of operands determines how many values are popped:

| Index | Operation | Formula | Operands |
|----|----|----|----|
| 1 | Add | Result = Pop1 + Pop2 | 2 |
| 2 | Subtract | Result = Pop2 − Pop1 | 2 |
| 3 | Multiply | Result = Pop1 × Pop2 | 2 |
| 4 | Divide | Result = Pop2 / Pop1 | 2 |
| 5 | Negate | Result = −Pop1 | 1 |
| 6 | Invert | Result = 1 / Pop1 | 1 |
| 7 | Modulo | Result = Pop2 % Pop1 | 2 |
| 8 | Power | Result = Pop2 ^ Pop1 (^ as power operator) | 2 |
| 9 | Square root | Result = √(Pop1) | 1 |
| 10 | Sine | Result = sin(Pop1) | 1 |
| 11 | Cosine | Result = cos(Pop1) | 1 |
| 12 | Tangent | Result = tan(Pop1) | 1 |
| 13 | Cotangent | Result = tan⁻¹(Pop1) | 1 |
| 14 | Inverse sine | Result = arcsin(Pop1) | 1 |
| 15 | Inverse cosine | Result = arccos(Pop1) | 1 |
| 16 | Inverse tangent | Result = arctan(Pop1) | 1 |
| 17 | Bitwise NOT | Result = ~Pop1 | 1 |
| 18 | Bitwise AND | Result = Pop1 & Pop2 | 2 |
| 19 | Bitwise OR | Result = Pop1 \| Pop2 | 2 |
| 20 | Bitwise XOR | Result = Pop1 ^ Pop2 (^ as XOR, as in C) | 2 |
| 21 | Shift left | Result = Pop1 << Pop2 | 2 |
| 22 | Shift right | Result = Pop1 >> Pop2 | 2 |
| 23 | Absolute | Result = abs(Pop1) | 1 |
| 24 | Logarithm | Result = log to base Pop2 of Pop1 | 2 |
| 25 | Base-10 logarithm | Result = log10(Pop1) | 1 |

## Examples

```text
; Compute 3 + 4 (operations normally emitted by the PC Suite compiler)
APushConstant=3      ; push first operand
APushConstant=4      ; push second operand
AMath[1]             ; index 1 = Add, result 7 is pushed back to the stack
```

## See also

- [PushParam](../03-stack-operation/PushParam.md) — push a parameter value onto the numeric stack
- [PushConstant](../03-stack-operation/PushConstant.md) — push a constant onto the numeric stack
- [PopParam](../03-stack-operation/PopParam.md) — pop the top stack value into a parameter
- [ProgExpStack](ProgExpStack.md) — read the top of the numeric stack without popping
