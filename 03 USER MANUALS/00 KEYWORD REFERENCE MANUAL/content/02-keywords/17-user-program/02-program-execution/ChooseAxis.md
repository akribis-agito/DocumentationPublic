---
keyword: ChooseAxis
summary: Per-thread array selecting which physical axis each user-program thread acts on.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 563
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ChooseAxis

Per-thread array selecting which physical axis each user-program thread acts on.

## Overview

`ChooseAxis` is an array parameter that selects which physical axis a given user-program thread operates on. Each element corresponds to one thread (or task); the value stored at that element is the axis number that thread's axis-specific commands are directed to. This lets a multi-threaded program run independent logic against different axes at the same time. The array size (10) equals the maximum number of concurrent threads.

It works alongside the thread/task model exposed by [ProgTask](ProgTask.md), which reports the task associated with program execution.

## Examples

```text
ChooseAxis[1]=0     ; thread 1 operates on axis 0
ChooseAxis[2]=1     ; thread 2 operates on axis 1
ChooseAxis[1]?      ; query the axis assigned to thread 1
```

## See also

- [ProgTask](ProgTask.md) — task associated with a running program thread
- [ProgRun](ProgRun.md) — start a user-program thread
