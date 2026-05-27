---
keyword: ProgArg
summary: Argument values passed to an indexed user program task.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# ProgArg

Argument values passed to an indexed user program task.

## Overview

`ProgArg` is an array parameter that holds the argument values passed to a user program task. Each element corresponds to one argument slot for the indexed task. It is the counterpart to [ProgArgThis](ProgArgThis.md), which a running task uses to read back its own arguments, and works together with [ProgPushArg](ProgPushArg.md), which pushes argument values onto a task's argument stack before it runs. `ProgArg` is a non-axis parameter and is not saved to flash.

## Examples

```text
AProgArg[1]         ; query the first argument slot
```

## See also

- [ProgArgThis](ProgArgThis.md) — read back the arguments received by the running task
- [ProgPushArg](ProgPushArg.md) — push an argument value onto a task's argument stack
