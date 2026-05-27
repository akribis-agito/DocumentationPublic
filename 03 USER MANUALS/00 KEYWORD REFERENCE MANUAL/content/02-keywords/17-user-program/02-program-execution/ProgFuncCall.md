---
keyword: ProgFuncCall
summary: Calls a user program function defined by a ProgFunc label.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 430
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
  - 1
  - 254
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgFuncCall

Calls a user program function defined by a ProgFunc label.

## Overview

`ProgFuncCall` calls a user program function. When `AProgFuncCall,1` is reached, execution jumps to the location of the [ProgFunc](ProgFunc.md) label with index `1`. A [Return](Return.md) at the end of the function jumps back and continues on the next line after the call. Use multiple `ProgFunc[]` labels to define multiple functions, each invoked by its index. It is a non-axis command and is not saved to flash.

> **Note:** Use [ProgHalt](ProgHalt.md) at the end of the program if it is not an endless loop. Otherwise execution continues into the first function and the `Return` keyword causes an error.

## Examples

```text
AProgFuncCall,1     ; jump to ProgFunc[1]; Return resumes on the next line
```

## See also

- [ProgFunc](ProgFunc.md) — label marking the start of a function
- [Return](Return.md) — return from a function call
- [ProgCallStack](ProgCallStack.md) — program-call stack contents
