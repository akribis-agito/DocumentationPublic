---
keyword: ProgThread
summary: "Reports the user-program thread number that is currently executing."
availability:
  standalone: []
  central-i:
  - v5
can_code: 737
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
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgThread

Reports the user-program thread number that is currently executing.

## Overview

`ProgThread` is a read-only status keyword that returns the number of the user-program thread that is currently executing. User programs are multi-threaded: the controller runs each active thread in turn, advancing one of them per scheduling cycle. `ProgThread` tells you which thread that is, so code or a host can know "which thread am I?" — for example to index per-thread state with [ProgStat](../02-program-execution/ProgStat.md), [ProgError](../02-program-execution/ProgError.md), or [ProgPointer](../02-program-execution/ProgPointer.md). It is a non-axis parameter and is not saved to flash.

This keyword is available from v5 (central-i).

## How it works

The controller schedules the active threads in a rotating order, executing a line of one thread each cycle (subject to each thread's [ProgPriority](../02-program-execution/ProgPriority.md)). `ProgThread` reports the number of whichever thread is the current one. Thread numbering starts at `1`; the main thread is thread `1`. When read from inside a running user program, the value is that program's own thread number, which makes it the natural way for shared code to discover which thread it is running on.

The default value is `1`. The reported number stays within the supported thread range for the model.

## Examples

```text
AProgThread         ; read the thread number currently executing
```

## See also

- [ProgStat](../02-program-execution/ProgStat.md) — running/stopped state of a given thread
- [ProgPriority](../02-program-execution/ProgPriority.md) — per-thread scheduling priority
- [ProgError](../02-program-execution/ProgError.md) — run-time error code of a given thread
- [ProgPointer](../02-program-execution/ProgPointer.md) — current program offset of a given thread
