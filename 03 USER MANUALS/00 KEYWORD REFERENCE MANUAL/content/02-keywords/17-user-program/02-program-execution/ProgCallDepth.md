---
keyword: ProgCallDepth
summary: Reports the free space remaining in a thread's program-call stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 277
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
# ProgCallDepth

Reports the free space remaining in a thread's program-call stack.

## Overview

`ProgCallDepth` is a read-only array parameter, indexed by thread, that reports the number of empty (free) slots remaining in the program-call stack of the specified thread. It complements [ProgCallStack](ProgCallStack.md), which exposes the call-stack contents, and is useful for diagnosing deeply nested function calls (see [ProgFuncCall](ProgFuncCall.md)). It is a non-axis status variable and is not saved to flash.

## Examples

```text
AProgCallDepth[1]   ; free call-stack slots for thread 1
```

## See also

- [ProgCallStack](ProgCallStack.md) — program-call stack contents per thread
- [ProgFuncCall](ProgFuncCall.md) — call a user program function
- [ProgClrCall](ProgClrCall.md) — clear the program-call stack
