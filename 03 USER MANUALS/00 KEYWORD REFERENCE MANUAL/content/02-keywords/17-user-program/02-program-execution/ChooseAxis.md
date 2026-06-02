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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ChooseAxis

Per-thread array selecting which physical axis each user-program thread acts on.

## Overview

`ChooseAxis` is an array parameter that selects which physical axis a given user-program thread acts on when a command uses the `P` (or `p`) axis letter as a placeholder instead of a fixed axis letter. Each element corresponds to one thread; the value stored at that element is the axis number substituted for the `P` placeholder in that thread's axis-specific commands. This lets a multi-threaded program run independent logic against different axes at the same time. The array is indexed by thread number, and its size matches the maximum number of concurrent threads.

It works alongside the thread/task model exposed by [ProgTask](ProgTask.md), which reports the task associated with program execution.

## How it works

When a thread executes a keyword (or an encoded parameter reference) whose axis letter is the `P` placeholder, the program engine substitutes the axis from `ChooseAxis` at the running thread's index. This is the same rule the stack operations [PushParam](../03-stack-operation/PushParam.md) and [PopParam](../03-stack-operation/PopParam.md) follow: an encoded reference whose axis token is the `P` placeholder takes its axis from the thread's `ChooseAxis` entry. A command that names an explicit axis letter — for example `AMotorOn=1` — is unaffected by `ChooseAxis` and always runs on the named axis. Changing the element redirects only that thread's subsequent `P`-placeholder commands, without affecting other threads. Each thread keeps its own entry, so several threads can drive different axes concurrently from the same downloaded program.

The default value is 0, so a thread that never sets `ChooseAxis` resolves the `P` placeholder to axis 0. When a `P`-placeholder command is issued directly over communication rather than from inside a running program, the substituted axis is taken from a separate, dedicated `ChooseAxis` entry reserved for the communication channel, not from any thread's entry.

## Examples

```text
AChooseAxis[1]=0     ; thread 1 resolves the P placeholder to axis 0
AChooseAxis[2]=1     ; thread 2 resolves the P placeholder to axis 1
AChooseAxis[1]      ; query the axis assigned to thread 1
PMotorOn=1           ; runs on the calling thread's ChooseAxis axis
```

## See also

- [ProgTask](ProgTask.md) — task associated with a running program thread
- [ProgRun](ProgRun.md) — start a user-program thread
