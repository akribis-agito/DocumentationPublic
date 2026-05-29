---
keyword: PushConstant
summary: Pushes a constant value onto the numeric stack of the current thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 201
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PushConstant

Pushes a constant value onto the numeric stack of the current thread.

## Overview

`PushConstant` is a low-level user-program keyword used to push the value of a constant onto the numeric stack of the current user program thread. It is the constant-literal counterpart of [PushParam](PushParam.md) (which pushes a parameter value), and the pushed values are typically consumed by a [Math](../02-program-execution/Math.md) operation, a [Compare](../02-program-execution/Compare.md), or stored with [PopParam](PopParam.md). Normally the user does not generate the code by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

## How it works

`PushConstant` places the literal value carried by the instruction onto the top of the current thread's numeric stack, growing the stack by one entry. No parameter look-up, axis resolution, or unit scaling is involved — the value is taken exactly as given. Each thread's numeric stack holds up to 50 values; pushing onto a full stack reports a stack-full error. The free space remaining can be read with [ProgExpDepth](../02-program-execution/ProgExpDepth.md). A companion operation pushes floating-point literals; the integer form documented here pushes a 32-bit integer constant.

## Examples

```text
APushConstant=5      ; push the constant 5 onto the numeric stack
```

## See also

- [PushParam](PushParam.md) — push a parameter value onto the numeric stack
- [PopParam](PopParam.md) — pop the top stack value into a parameter
- [Math](../02-program-execution/Math.md) — operate on values on the numeric stack
