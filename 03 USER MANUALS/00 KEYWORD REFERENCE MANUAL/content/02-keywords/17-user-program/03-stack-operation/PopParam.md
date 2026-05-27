---
keyword: PopParam
summary: Pops the top value of the numeric stack into a parameter.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 202
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
# PopParam

Pops the top value of the numeric stack into a parameter.

## Overview

`PopParam` is a low-level user-program keyword. It pops the last ("top") value from the numeric stack of the current thread and assigns it to the requested parameter, which is identified by its complex CAN code. It is the inverse of [PushParam](PushParam.md), which pushes a parameter value onto the stack, and is typically used to store the result of a [Math](../02-program-execution/Math.md) operation back into a parameter. Normally the user does not generate the CAN code by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

## Examples

```text
; Store the top stack value into a parameter (CAN code emitted by the compiler)
APopParam=<complex CAN code of target parameter>
```

## See also

- [PushParam](PushParam.md) — push a parameter value onto the numeric stack
- [PushConstant](PushConstant.md) — push a constant onto the numeric stack
- [Math](../02-program-execution/Math.md) — operate on values on the numeric stack
