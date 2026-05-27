---
keyword: Jump
summary: Low-level user-program op that branches execution to another point in the program.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 196
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
  range: null
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    array_size: 34
---
# Jump

Low-level user-program op that branches execution to another point in the program.

## Overview

`Jump` is a low-level user-program language keyword that redirects program execution to another location. Syntax involving `Jump` can only be generated automatically by the PC Suite during compilation, because the command carries a target that is an offset into the compiled program file and therefore depends on the file's exact layout. For the same reason `Jump` cannot be issued over a communication channel; it runs only as part of a downloaded program. It implements the branching used to build loops and conditional flow, typically acting on the result that [Compare](Compare.md) pushes onto the numeric stack.

## How it works

`Jump` takes an operation index and a target. The target is applied by setting the running thread's program pointer to the start of the program plus the target offset, so execution continues from that point. The operation index decides whether the jump is taken:

- Operation `1` is an **unconditional** jump — execution always continues at the target.
- The **conditional** operations pop their operand(s) from the numeric stack and jump only if the condition holds; otherwise execution falls through to the next instruction.

The conditional operations mirror the comparison set used by [Compare](Compare.md), and like `Compare` they are provided for each operand data type — 32-bit integer (the default), 32-bit floating point, 64-bit integer, and 64-bit double-precision floating point. As in `Compare`, `pop1` is the value popped first (top of stack) and `pop2` the one beneath it; two-operand tests read as `pop2 (operator) pop1`.

| Operation | 32-bit integer | float | 64-bit integer | double | Jump if |
| --------- | -------------- | ----- | -------------- | ------ | ------- |
| Unconditional        | 1 | — | — | — | always |
| `==` (equal)         | 2 | 10 | 18 | 26 | pop2 == pop1 |
| `>` (greater than)   | 3 | 11 | 19 | 27 | pop2 > pop1  |
| `>=` (greater/equal) | 4 | 12 | 20 | 28 | pop2 >= pop1 |
| `<` (less than)      | 5 | 13 | 21 | 29 | pop2 < pop1  |
| `<=` (less/equal)    | 6 | 14 | 22 | 30 | pop2 <= pop1 |
| `!=` (not equal)     | 7 | 15 | 23 | 31 | pop2 != pop1 |
| Zero                 | 8 | 16 | 24 | 32 | pop1 == 0    |
| Not zero             | 9 | 17 | 25 | 33 | pop1 != 0    |

In compiled programs the most common pattern is a [Compare](Compare.md) (which leaves `1` or `0` on the stack) followed by a "jump if zero" (operation 8) or "jump if not zero" (operation 9): the comparison forms the condition and the jump implements the branch. Together they build the `if`, `while`, and `for` structures of the high-level program.

## See also

- [Compare](Compare.md) — produces the condition values used for conditional jumps
- [Math](Math.md) — arithmetic/bitwise operations on the numeric stack
- [ProgPointer](ProgPointer.md) — current program-execution pointer
