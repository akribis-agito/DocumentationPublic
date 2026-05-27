---
keyword: Return
summary: Returns from a user program function call to the line after the call.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 432
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 10
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 16
---
# Return

Returns from a user program function call to the line after the call.

## Overview

`Return` causes a jump back to the user program, continuing execution on the next line after a function call made with [ProgFuncCall](ProgFuncCall.md). It unwinds the most recent frame from the program-call stack ([ProgCallStack](ProgCallStack.md)) and is also used to complete an event-handler function, after which the event can be triggered again (see [ProgEventStat](ProgEventStat.md)).

`Return` can also return values: any array elements supplied are pushed back to the caller as output arguments, while the command value tells the engine how many input arguments the function received. The supported input-argument count is `0`–`10`, extended to `0`–`16` on central-i v5.

> **Note:** Use [ProgHalt](ProgHalt.md) at the end of the program if it is not an endless loop. Otherwise execution continues into the first function and the `Return` keyword causes an error.

## How it works

When `Return` runs it operates on the current thread's call stack. The command value is the count of *input* arguments the function received; the number of array elements supplied is the count of *output* arguments to return. The engine then:

1. Checks the call stack is not empty — a `Return` with nothing to return to is an error. It also checks the stack actually contains the declared input arguments, output arguments, return address and frame location, and that the numeric (expression) stack has room for the output values.
2. Pops the *return address* and resumes execution on the line after the originating [ProgFuncCall](ProgFuncCall.md).
3. Pushes the function's output arguments onto the numeric (expression) stack, so the caller can read them with the stack-operation keywords. Each output value occupies one numeric-stack location.
4. Restores the caller's frame location and discards the whole frame (input arguments, output arguments, return address and frame location) from the call stack.

When the frame being unwound was entered as a program-event handler rather than a normal call, `Return` instead re-arms that event so it can trigger again (see [ProgEventStat](ProgEventStat.md)); an event-handler `Return` must declare no input or output arguments.

Two common errors: calling `Return` when the call stack is empty (for example, when execution falls through into a function — see [ProgFunc](ProgFunc.md)), and declaring more output arguments than the numeric stack can hold.

## Examples

```text
AProgFuncCall,1     ; call function 1
...
AProgFunc[1]        ; label: start of function 1
; function body
AReturn             ; return to the line after the call (no arguments)

AReturn[42],99      ; return two output values (42, 99) onto the numeric stack
```

## See also

- [ProgFuncCall](ProgFuncCall.md) — call a function
- [ProgFunc](ProgFunc.md) — label marking the start of a function
- [ProgArgThis](ProgArgThis.md) — read the arguments inside the function
- [ProgCallStack](ProgCallStack.md) — program-call stack contents
- [ProgHalt](ProgHalt.md) — halt a thread (place before function definitions)
