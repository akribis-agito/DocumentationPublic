---
keyword: ProgClrCall
summary: Clears the program-call stack of a user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgClrCall` is a command, indexed by thread, that clears the program-call stack of a user program thread, discarding any pending function return locations. It is the call-stack counterpart of [ProgClrExp](ProgClrExp.md), which clears the numeric (expression) stack. It is a non-axis command and is not saved to flash.

> **Documentation pending:** Exact usage details are not described in the source reference. Refer to the User Program Language Manual for complete details.

## See also

- [ProgCallStack](ProgCallStack.md) — program-call stack contents
- [ProgCallDepth](ProgCallDepth.md) — free space remaining in the call stack
- [ProgClrExp](ProgClrExp.md) — clear the numeric (expression) stack
