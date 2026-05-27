---
keyword: ProgStatAll
summary: Returns a combined status word for all user program tasks.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 298
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStatAll

Returns a combined status word for all user program tasks.

## Overview

`ProgStatAll` is a read-only parameter that returns a combined status word reflecting the execution state of all user program tasks. It is the aggregate counterpart of [ProgStat](ProgStat.md), which reports a single thread, and is useful for a quick health check of the whole interpreter. It is a non-axis status variable and is not saved to flash.

## Examples

```text
AProgStatAll        ; combined status of all user program tasks
```

## See also

- [ProgStat](ProgStat.md) — running status of one thread
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
- [ProgPriority](ProgPriority.md) — task scheduling priority
- [ProgReset](ProgReset.md) — reset a task to its initial state
