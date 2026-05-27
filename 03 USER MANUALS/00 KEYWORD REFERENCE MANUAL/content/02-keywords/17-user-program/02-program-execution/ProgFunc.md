---
summary: Label keyword marking the start of a user program function.
---
# ProgFunc

Label keyword marking the start of a user program function.

## Overview

`ProgFunc` is used as a label in user programs, marking the entry point of a function. When a [ProgFuncCall](ProgFuncCall.md) to the matching index is reached, execution jumps to the location of the `ProgFunc[]` label with that index. A [Return](Return.md) at the end of the function jumps back to the caller and continues on the next line. Use multiple `ProgFunc[]` labels to define multiple functions.

## How it works

`ProgFunc[]` is a label marking a program location, not an executed command — it records where a function begins so that [ProgFuncCall](ProgFuncCall.md) can jump to it by index. The function index is the link between the two: `AProgFuncCall,3` always jumps to `AProgFunc[3]`.

A function may receive input arguments and return output values. Arguments are staged on the calling thread's call stack with [ProgPushArg](ProgPushArg.md) before the call, read inside the function with [ProgArgThis](ProgArgThis.md), and any output values are placed back on the numeric stack by [Return](Return.md). The sum of input arguments, output arguments and local variables for one function is limited (up to 26 entries on larger models, up to 20 on smaller ones); see [ProgArgThis](ProgArgThis.md).

Because labels only mark locations, execution *falls through* into a function body if the preceding code reaches it linearly. Place a [ProgHalt](ProgHalt.md) (or an endless loop) before the first `ProgFunc[]` label so the main program does not run into the functions — doing so would reach a [Return](Return.md) with an empty call stack and raise an error.

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
- [ProgPushArg](ProgPushArg.md) — stage an argument before the call
- [ProgArgThis](ProgArgThis.md) — read the arguments inside the function
- [ProgHalt](ProgHalt.md) — halt a thread (place before function definitions)
