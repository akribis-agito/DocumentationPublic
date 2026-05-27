---
keyword: PopParam
summary: Pops the top value of the numeric stack into a parameter.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`PopParam` is a low-level user-program keyword. It pops the last ("top") value from the numeric stack of the current thread and assigns it to the requested parameter, which is identified by an encoded reference naming the keyword, axis, and array index. It is the inverse of [PushParam](PushParam.md), which pushes a parameter value onto the stack, and is typically used to store the result of a [Math](../02-program-execution/Math.md) operation back into a parameter. Normally the user does not generate the reference by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

## How it works

`PopParam` removes the top value from the current thread's numeric stack and writes it to the named parameter, shrinking the stack by one entry. Because writing a parameter is an assignment, `PopParam` applies the same validity checks the controller performs for any parameter write (range, access, and motion/motor-state rules for that keyword), so an out-of-range or otherwise rejected write reports an error.

Two patterns are common in compiled code:

- **Direct store.** The target parameter is named directly in the instruction, and the top stack value is written to it.
- **Store through a computed target.** The program can compute which parameter to write — for example, the encoded reference of the destination is itself left on the stack so that the assignment uses a pointer rather than a fixed target. This is how the compiler implements assignment to an element whose index was calculated at run time.

As with [PushParam](PushParam.md), when the reference does not name a specific axis the axis is taken from the thread's [ChooseAxis](../02-program-execution/ChooseAxis.md) entry.

## Examples

```text
; Store the top stack value into a parameter (encoded reference emitted by the compiler)
APopParam=<encoded reference to target parameter>
```

## See also

- [PushParam](PushParam.md) — push a parameter value onto the numeric stack
- [PushConstant](PushConstant.md) — push a constant onto the numeric stack
- [Math](../02-program-execution/Math.md) — operate on values on the numeric stack
