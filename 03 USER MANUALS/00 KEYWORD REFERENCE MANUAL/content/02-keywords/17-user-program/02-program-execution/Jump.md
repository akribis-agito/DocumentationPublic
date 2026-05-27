---
keyword: Jump
summary: Low-level user-program op that branches execution to another point in the program.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# Jump

Low-level user-program op that branches execution to another point in the program.

## Overview

`Jump` is a low-level user-program language keyword that redirects program execution to another location. Syntax involving `Jump` can only be generated automatically by the PC Suite during compilation, because the command carries a pointer for the jump target that depends on the structure of the compiled program file. It implements the branching used to build loops and conditional flow, typically acting on the result that [Compare](Compare.md) pushes onto the numeric stack.

> **Documentation pending:** This page is marked `implemented: partial`. The jump-target encoding is compiler-generated; verify against current firmware before relying on hand-written usage.

## See also

- [Compare](Compare.md) — produces the condition values used for conditional jumps
- [Math](Math.md) — arithmetic/bitwise operations on the numeric stack
- [ProgPointer](ProgPointer.md) — current program-execution pointer
