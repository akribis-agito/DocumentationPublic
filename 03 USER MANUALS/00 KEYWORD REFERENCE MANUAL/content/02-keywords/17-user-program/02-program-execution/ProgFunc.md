---
summary: Label keyword marking the start of a user program function.
---
# ProgFunc

Label keyword marking the start of a user program function.

## Overview

`ProgFunc` is used as a label in user programs, marking the entry point of a function. When a [ProgFuncCall](ProgFuncCall.md) to the matching index is reached, execution jumps to the location of the `ProgFunc[]` label with that index. A [Return](Return.md) at the end of the function jumps back to the caller and continues on the next line. Use multiple `ProgFunc[]` labels to define multiple functions.

> **Note:** Use [ProgHalt](ProgHalt.md) at the end of the program if it is not an endless loop. Otherwise execution continues into the first function and the `Return` keyword causes an error.

## Examples

```text
...
AProgFuncCall,1     ; call function 1
...
AProgFunc[1]        ; label: start of function 1
; the contents of function 1
AReturn             ; return to the line after the call
```

## See also

- [ProgFuncCall](ProgFuncCall.md) — call a function defined by a ProgFunc label
- [Return](Return.md) — return from a function call
- [ProgHalt](ProgHalt.md) — halt a thread (place before function definitions)
