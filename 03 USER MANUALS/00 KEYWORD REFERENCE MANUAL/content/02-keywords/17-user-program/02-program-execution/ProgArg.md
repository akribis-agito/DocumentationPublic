---
keyword: ProgArg
summary: Argument values passed to an indexed user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 439
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 26
---
# ProgArg

Argument values passed to an indexed user program task.

## Overview

`ProgArg` reads the arguments of a thread's currently executing function from *outside* that function — it is indexed by thread number, with the argument position supplied as the command value. Where [ProgArgThis](ProgArgThis.md) lets a function read its own arguments, `ProgArg` lets the host or another context inspect any thread's current arguments, which makes it useful for monitoring and debugging. It is a non-axis parameter and is not saved to flash.

## How it works

`ProgArg[thread], position` resolves against the named thread's current call-stack frame and returns the value at the given argument position, using the same numbering as [ProgArgThis](ProgArgThis.md): position `1` is the last value pushed with [ProgPushArg](ProgPushArg.md) before the call, position `2` the one before it, and so on. The valid position range is `0`–`20` (`0`–`26` on central-i v5), covering the combined argument and local-variable space of a function; position `1` is the first (last-pushed) argument, while position `0` addresses the frame-reference/return slot rather than a user-supplied argument.

Because it reads the *current* frame of the selected thread, the values reflect whatever function that thread is executing at the moment of the query. Requesting a position beyond what the thread's current frame contains raises a "no operands in call stack" error.

## Examples

```text
AProgArg[1],1       ; read argument position 1 of the function running on thread 1
AProgArg[3],2       ; read argument position 2 of the function running on thread 3
```

## See also

- [ProgArgThis](ProgArgThis.md) — a function reading its own arguments
- [ProgPushArg](ProgPushArg.md) — stage an argument before the call
- [ProgCallStack](ProgCallStack.md) — full call-stack contents per thread
