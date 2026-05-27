---
keyword: ProgHaltAll
summary: Halts all currently active user program threads.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 278
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
# ProgHaltAll

Halts all currently active user program threads.

## Overview

`ProgHaltAll` halts all currently active user program threads. As with [ProgHalt](ProgHalt.md), halting is not the same as resetting: threads can be resumed with [ProgRun](ProgRun.md). To stop all threads and also reset their pointers and stacks, use [ProgResetAll](ProgResetAll.md) instead. It is a non-axis command and is not saved to flash.

## Examples

```text
ProgHaltAll         ; halt every active user program thread
```

## See also

- [ProgHalt](ProgHalt.md) — halt a single thread
- [ProgHaltThis](ProgHaltThis.md) — halt the running task
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
