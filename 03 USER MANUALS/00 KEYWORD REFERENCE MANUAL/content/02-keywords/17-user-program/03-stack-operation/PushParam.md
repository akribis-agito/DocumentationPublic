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

`PushParam` is a low-level user-program keyword used to push the value of a parameter onto the numeric stack of the current user program thread. The parameter is identified by an encoded reference that names the keyword, the axis, and the array index to read. It is the parameter-valued counterpart of [PushConstant](PushConstant.md) and the inverse of [PopParam](PopParam.md); pushed values are typically consumed by a [Math](../02-program-execution/Math.md) operation. Normally the user does not generate the reference by hand — the PC Suite user-program IDE produces it automatically during compilation. It is a non-axis command and is not saved to flash.

## How it works

Each thread has its own numeric (expression) stack. `PushParam` reads the named parameter and places its value on the top of that thread's stack, growing the stack by one entry. The pushed value keeps the parameter's data type (32-bit integer, 64-bit integer, 32-bit float, or 64-bit double).

A few behaviours are worth noting:

- **Axis resolution.** When the reference does not name a specific axis, the axis is taken from the thread's [ChooseAxis](../02-program-execution/ChooseAxis.md) entry, so the same instruction follows whichever axis the thread is currently working on.
- **Indirect (computed) array index.** If the reference targets an array but leaves the index unspecified, `PushParam` first pops one value off the stack and uses it as the array index. This lets a program compute an index (for example with [Math](../02-program-execution/Math.md)) and then read the corresponding array element.
- **Unit scaling.** Parameters expressed in user units are converted to user units as they are pushed, matching how the same parameter reads over communication.
- **Limits.** Pushing onto a full stack reports a stack-full error, and a keyword that is a function (rather than a value) cannot be pushed.

## Examples

```text
; Push a parameter's value onto the stack (encoded reference emitted by the compiler)
APushParam=<encoded reference to source parameter>
```

## See also

- [PushConstant](PushConstant.md) — push a constant onto the numeric stack
- [PopParam](PopParam.md) — pop the top stack value into a parameter
- [Math](../02-program-execution/Math.md) — operate on values on the numeric stack
