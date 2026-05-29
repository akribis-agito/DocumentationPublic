---
keyword: PushConstantF
summary: "Pushes a 32-bit floating-point (float) constant onto the numeric stack of the current thread."
availability:
  standalone: []
  central-i:
  - v5
can_code: 720
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PushConstantF

Pushes a 32-bit floating-point (float) constant onto the numeric stack of the current thread.

## Overview

`PushConstantF` is the single-precision floating-point form of [PushConstant](PushConstant.md). It pushes the value of a 32-bit floating-point (float) constant onto the numeric stack of the current user program thread. Like the base keyword it is the constant-literal counterpart of [PushParam](PushParam.md) (which pushes a parameter value), and the pushed values are typically consumed by a [Math](../02-program-execution/Math.md) operation, a [Compare](../02-program-execution/Compare.md), or stored with [PopParam](PopParam.md). Normally the user does not generate the code by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

`PushConstantF` places the literal value carried by the instruction onto the top of the current thread's numeric stack, growing the stack by one entry. No parameter look-up, axis resolution, or unit scaling is involved — the value is taken exactly as given. Pushing onto a full stack reports a stack-full error.

The only difference from [PushConstant](PushConstant.md) is the data type pushed: `PushConstantF` pushes a 32-bit floating-point (float) literal rather than a 32-bit integer constant. The stack slot is the same; the typed forms simply control how the value is stored so it is interpreted correctly when consumed.

## Examples

```text
APushConstantF=2.5      ; push the float constant 2.5 onto the numeric stack
```

## See also

- [PushConstant](PushConstant.md) — the base (32-bit integer) form
- [PushConstantD](PushConstantD.md) — 64-bit floating-point (double) form
- [PushConstLL](PushConstLL.md) — 64-bit integer form
- [PushParam](PushParam.md) — push a parameter value onto the numeric stack
- [PopParam](PopParam.md) — pop the top stack value into a parameter
