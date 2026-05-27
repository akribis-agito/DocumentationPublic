---
keyword: ProgClrCall
summary: Clears the program-call stack of a user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 275
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgClrCall

Clears the program-call stack of a user program thread.

## Overview

`ProgClrCall` is a command, indexed by thread, that clears the program-call stack of a user program thread, discarding any pending function return locations and staged arguments. It is the call-stack counterpart of [ProgClrExp](ProgClrExp.md), which clears the numeric (expression) stack. It is a non-axis command and is not saved to flash.

## How it works

`ProgClrCall[thread]` empties the selected thread's call stack in one step: it marks the stack as having no occupied slots and resets the current frame reference to the base. After this, [ProgCallDepth](ProgCallDepth.md) reports the full 100 free slots and [ProgCallStack](ProgCallStack.md) shows nothing occupied.

Clearing only resets the stack bookkeeping; it does not by itself redirect execution. Because it abandons every pending return address, a subsequent [Return](Return.md) would find an empty stack and raise an error. Use it to recover a thread to a known clean state, typically together with [ProgClrExp](ProgClrExp.md) and a reset of the program pointer (see [ProgReset](ProgReset.md) / [ProgResetAll](ProgResetAll.md)), rather than in the middle of a normal call sequence.

## Examples

```text
AProgClrCall[1]     ; clear the call stack of thread 1
```

## See also

- [ProgCallStack](ProgCallStack.md) — program-call stack contents
- [ProgCallDepth](ProgCallDepth.md) — free space remaining in the call stack
- [ProgClrExp](ProgClrExp.md) — clear the numeric (expression) stack
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
