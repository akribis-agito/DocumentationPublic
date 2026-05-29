---
keyword: Math
summary: Low-level user-program op that applies a math operation to the top of the numeric stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    array_size: 113
---
# Math

Low-level user-program op that applies a math operation to the top of the numeric stack.

## Overview

`Math` is a low-level user-program keyword. The syntax around `Math` is normally generated automatically by the PC Suite during compilation, so it is rarely written by hand. `Math` performs the requested operation on the top one or two values of the numeric stack — the operands must be pushed first (see [PushParam](../03-stack-operation/PushParam.md) and [PushConstant](../03-stack-operation/PushConstant.md)), and the result is pushed back onto the stack. When `Math` is called over communication, the result is also returned through the communication channel.

Each operation exists in several typed variants, selected by the operation index: a 32-bit integer set (the operations listed in the first table below), and matching 32-bit floating-point, 64-bit integer, and 64-bit double-precision floating-point sets at higher indices. The compiler chooses the variant that matches the operand types. The transcendental functions (trigonometry, logarithm, exponential, invert) are only meaningful in the floating-point and double variants — they are not evaluated on the integer set. Type-cast operations are also available to convert a value between the four numeric types in place.

> **Note:** `Pop1` is the first value popped from the stack (the "top" value); `Pop2` is the second value popped.

## How it works

The index selects which operation is performed and on which data type; the number of operands determines how many values are popped. The base (32-bit integer) operations are:

| Index | Operation | Formula | Operands |
|----|----|----|----|
| 1 | Add | Result = Pop1 + Pop2 | 2 |
| 2 | Subtract | Result = Pop2 − Pop1 | 2 |
| 3 | Multiply | Result = Pop1 × Pop2 | 2 |
| 4 | Divide | Result = Pop2 / Pop1 (integer division; division by 0 is an error) | 2 |
| 5 | Negate | Result = −Pop1 | 1 |
| 7 | Modulo | Result = Pop2 % Pop1 (remainder; division by 0 is an error) | 2 |
| 8 | Power | Result = Pop2 raised to Pop1 (Pop1 must be ≥ 0) | 2 |
| 9 | Square root | Result = √(Pop1) (Pop1 must be ≥ 0) | 1 |
| 17 | Bitwise NOT | Result = ~Pop1 | 1 |
| 18 | Bitwise AND | Result = Pop2 &amp; Pop1 | 2 |
| 19 | Bitwise OR | Result = Pop2 \| Pop1 | 2 |
| 20 | Bitwise XOR | Result = Pop2 ^ Pop1 (^ as XOR, as in C) | 2 |
| 21 | Shift left | Result = Pop1 &lt;&lt; Pop2 | 2 |
| 22 | Shift right | Result = Pop1 &gt;&gt; Pop2 | 2 |
| 23 | Absolute | Result = abs(Pop1) | 1 |
| 28 | Logical AND | Result = (Pop1 != 0) AND (Pop2 != 0) | 2 |
| 29 | Logical OR | Result = (Pop1 != 0) OR (Pop2 != 0) | 2 |
| 30 | Logical NOT | Result = (Pop1 == 0) | 1 |
| 31 | Value pointed to | Result = value of the parameter whose code is Pop1 | 1 |

> **Integer set limitations:** Invert (`1 / Pop1`), the trigonometric functions, logarithm, base-10 logarithm and exponential have no integer result — index `6` (invert) reports "operation not implemented", and the trigonometric/logarithmic indices on the integer set do not produce a value. Use the floating-point or double variants for these (see below).

Higher index ranges repeat the operation set for the other data types and add casts. **These are Central-i v5 only**: on v4 (standalone and Central-i) the maximum operation index is `31`, and selecting any index from `32` upward is rejected as an out-of-range operation.

| Index range | Data type / purpose | Available on |
|----|----|----|
| 32–53 | 32-bit floating-point operations (full arithmetic, trigonometry in radians, logarithm, base-10 logarithm, exponential, two-argument arctangent, modulo, power, invert, square root, absolute) | v5 only |
| 54–58 | Cast 32-bit integer to/from float; round, floor and ceiling of a float | v5 only |
| 59–77 | 64-bit integer operations (arithmetic, bitwise, shifts, logical, square root, absolute) | v5 only |
| 78–99 | 64-bit double-precision floating-point operations (same coverage as the float set) | v5 only |
| 100–109 | Casts between 32-bit integer, 64-bit integer, float and double | v5 only |
| 110–112 | Round, floor and ceiling of a double | v5 only |

Values are integers in the integer variants; in the floating-point and double variants the operands and result carry their floating-point representation. It is the program's (normally the compiler's) responsibility to use the variant that matches the operand types.

## Examples

```text
; Compute 3 + 4 (operations normally emitted by the PC Suite compiler)
APushConstant=3      ; push first operand
APushConstant=4      ; push second operand
AMath[1]             ; index 1 = Add (32-bit integer), result 7 is pushed back to the stack
```

## See also

- [PushParam](../03-stack-operation/PushParam.md) — push a parameter value onto the numeric stack
- [PushConstant](../03-stack-operation/PushConstant.md) — push a constant onto the numeric stack
- [PopParam](../03-stack-operation/PopParam.md) — pop the top stack value into a parameter
- [ProgExpStack](ProgExpStack.md) — read the top of the numeric stack without popping
