---
keyword: ChooseAxis
summary: Per-thread array selecting which physical axis each user-program thread acts on.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ChooseAxis

Per-thread array selecting which physical axis each user-program thread acts on.

## Overview

`ChooseAxis` is an array parameter that selects which physical axis a given user-program thread acts on when a command does not name a specific axis. Each element corresponds to one thread; the value stored at that element is the axis number used for that thread's axis-specific commands that are issued without an explicit axis. This lets a multi-threaded program run independent logic against different axes at the same time. The array is indexed by thread number, and its size matches the maximum number of concurrent threads.

It works alongside the thread/task model exposed by [ProgTask](ProgTask.md), which reports the task associated with program execution.

## How it works

When a thread executes a keyword (or an encoded parameter reference) that does not name a specific axis, the program engine takes the axis from `ChooseAxis` at the running thread's index. This is the same rule the stack operations [PushParam](../03-stack-operation/PushParam.md) and [PopParam](../03-stack-operation/PopParam.md) follow: when the reference does not name a specific axis, the axis is taken from the thread's `ChooseAxis` entry. A command that does name an explicit axis letter — for example `AMotorOn=1` — is unaffected by `ChooseAxis` and always runs on the named axis. Changing the element redirects only that thread's subsequent axis-specific commands that are issued without an explicit axis, without affecting other threads. Each thread keeps its own entry, so several threads can drive different axes concurrently from the same downloaded program.

The default value is 0, so a thread that never sets `ChooseAxis` operates on axis 0.

## Examples

```text
AChooseAxis[1]=0     ; thread 1 operates on axis 0
AChooseAxis[2]=1     ; thread 2 operates on axis 1
AChooseAxis[1]      ; query the axis assigned to thread 1
```

## See also

- [ProgTask](ProgTask.md) — task associated with a running program thread
- [ProgRun](ProgRun.md) — start a user-program thread
