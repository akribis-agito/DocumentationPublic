---
keyword: ProgStat
summary: Reports the running status of a specified user program thread.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 259
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStat

Reports the running status of a specified user program thread.

## Overview

`ProgStat` is a read-only array parameter, indexed by thread, that reports the running status of a user program thread. It is the per-thread complement of [ProgStatAll](ProgStatAll.md) (combined status of all tasks) and is used alongside [ProgError](ProgError.md) when diagnosing why a thread stopped. It is a non-axis status variable and is not saved to flash.

## How it works

| Value | Meaning |
|----|----|
| -1 | No user program in the controller |
| 0 | Not running |
| 1 | Running |

## Examples

```text
AProgStat[1]        ; 1 if thread 1 is running, 0 if stopped, -1 if no program
```

## See also

- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
- [ProgError](ProgError.md) — last interpreter error per thread
- [ProgRun](ProgRun.md) — run a task as a thread
