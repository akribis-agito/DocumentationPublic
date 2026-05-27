---
keyword: Return
summary: Returns from a user program function call to the line after the call.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# Return

Returns from a user program function call to the line after the call.

## Overview

`Return` causes a jump back to the user program, continuing execution on the next line after a function call made with [ProgFuncCall](ProgFuncCall.md). It pops the most recent entry from the program-call stack ([ProgCallStack](ProgCallStack.md)) and is also used to complete an event-handler function, after which the event can be triggered again (see [ProgEventStat](ProgEventStat.md)).

> **Note:** Use [ProgHalt](ProgHalt.md) at the end of the program if it is not an endless loop. Otherwise execution continues into the first function and the `Return` keyword causes an error.

## Examples

```text
AProgFuncCall,1     ; call function 1
...
AProgFunc[1]        ; label: start of function 1
; function body
AReturn             ; return to the line after the call
```

## See also

- [ProgFuncCall](ProgFuncCall.md) — call a function
- [ProgFunc](ProgFunc.md) — label marking the start of a function
- [ProgHalt](ProgHalt.md) — halt a thread (place before function definitions)
