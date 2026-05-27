---
keyword: ProgCallStack
summary: Program-call stack contents for a user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 276
attributes:
  access: rw
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
  - 99
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgCallStack

Program-call stack contents for a user program thread.

## Overview

`ProgCallStack` is an array parameter, indexed by thread, that exposes the program-call stack of a user program thread — the chain of return locations created when functions are invoked with [ProgFuncCall](ProgFuncCall.md) and unwound by [Return](Return.md). Use [ProgCallDepth](ProgCallDepth.md) to check how much free space remains, and [ProgClrCall](ProgClrCall.md) to clear it. It is a non-axis parameter and is not saved to flash.

> **Documentation pending:** The detailed encoding of each call-stack entry is not described in the source reference. Refer to the User Program Language Manual for complete details.

## See also

- [ProgCallDepth](ProgCallDepth.md) — free space remaining in the call stack
- [ProgClrCall](ProgClrCall.md) — clear the program-call stack
- [ProgFuncCall](ProgFuncCall.md) — call a user program function
- [Return](Return.md) — return from a function call
