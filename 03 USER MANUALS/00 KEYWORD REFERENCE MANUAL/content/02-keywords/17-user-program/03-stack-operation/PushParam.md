---
keyword: PushParam
summary: Pushes a parameter's value onto the numeric stack of the current thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 200
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
# PushParam

Pushes a parameter's value onto the numeric stack of the current thread.

## Overview

`PushParam` is a low-level user-program keyword used to push the value of a parameter onto the numeric stack of the current user program thread. The parameter is identified by its complex CAN code. It is the parameter-valued counterpart of [PushConstant](PushConstant.md) and the inverse of [PopParam](PopParam.md); pushed values are typically consumed by a [Math](../02-program-execution/Math.md) operation. Normally the user does not generate the CAN code by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

## Examples

```text
; Push a parameter's value onto the stack (CAN code emitted by the compiler)
APushParam=<complex CAN code of source parameter>
```

## See also

- [PushConstant](PushConstant.md) — push a constant onto the numeric stack
- [PopParam](PopParam.md) — pop the top stack value into a parameter
- [Math](../02-program-execution/Math.md) — operate on values on the numeric stack
