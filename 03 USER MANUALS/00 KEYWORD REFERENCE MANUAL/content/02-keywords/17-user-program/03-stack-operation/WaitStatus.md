---
keyword: WaitStatus
summary: Holds a user program thread until a selected status reaches a required value.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 194
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 34
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# WaitStatus

Holds a user program thread until a selected status reaches a required value.

## Overview

`WaitStatus` is a low-level user-program keyword, used only in user program compilation; it cannot be commanded normally over communication channels. `WaitStatus` holds the user program thread until the selected status reaches the required value. It is the status-driven counterpart of [WaitTime](WaitTime.md), which instead waits for a fixed time. The status to wait on is chosen by the array index, and the required value is the assigned value.

## How it works

While the condition is not yet satisfied, `WaitStatus` marks the thread as waiting and yields, so the thread re-checks the status on each pass without consuming the program engine; other threads keep running. As soon as the status matches the required value, the wait ends and the thread continues with the next instruction. For the counter status types the wait ends when the counter reaches the requested value (the down-counters when they have counted down to it, the up-counters when they have counted up to it); for the bit-type status types the required value is the bit state to wait for (0 or 1).

`WaitStatus` is axis-related: bit-type conditions that belong to a motor or axis are evaluated for the axis the running thread is currently working on (see [ChooseAxis](../02-program-execution/ChooseAxis.md)).

The array index selects which status counter or bit the thread waits on:

| Status type | Description | Required value |
|----|----|----|
| 1 | Down counter 1 | counter target (≥ 0) |
| 2 | Down counter 2 | counter target (≥ 0) |
| 3 | Down counter 3 | counter target (≥ 0) |
| 4 | Down counter 4 | counter target (≥ 0) |
| 5 | Up counter 1 | counter target (≥ 0) |
| 6 | Up counter 2 | counter target (≥ 0) |
| 7 | In motion | 0 or 1 |
| 8 | In repetitive wait | 0 or 1 |
| 9 | In repetitive stop | 0 or 1 |
| 10 | In stop request | 0 or 1 |
| 11 | In acceleration | 0 or 1 |
| 12 | In deceleration | 0 or 1 |
| 13 | In wait-end smooth | 0 or 1 |
| 14 | In ECAM stop | 0 or 1 |
| 15 | In FIFO stop | 0 or 1 |
| 16 | Commutation done | 0 or 1 |
| 17 | In target | 0 or 1 |
| 18 | Recording trigger detected | 1 or 2 |
| 19 | Recording completed | 1 or 2 |
| 20 | Digital input 1 | 0 or 1 |
| 21 | Digital input 2 | 0 or 1 |
| 22 | Digital input 3 | 0 or 1 |
| 23 | Digital input 4 | 0 or 1 |
| 24 | Digital input 5 | 0 or 1 |
| 25 | Digital input 6 | 0 or 1 |
| 26 | Digital input 7 | 0 or 1 |
| 27 | Digital input 8 | 0 or 1 |
| 28 | Digital input 9 | 0 or 1 |
| 29 | Digital input 10 | 0 or 1 |
| 30 | Digital input 11 | 0 or 1 |
| 31 | Digital input 12 | 0 or 1 |
| 32 | Digital input 13 | 0 or 1 |
| 33 | Digital input 14 | 0 or 1 |

## Examples

```text
AWaitStatus[17],1   ; hold until the axis reaches and settles in target (In target = 1)
AWaitStatus[7],0    ; hold until motion has stopped (In motion = 0)
AWaitStatus[20],1   ; hold until digital input 1 is high
```

## See also

- [WaitTime](WaitTime.md) — hold a task for a fixed time instead of a status
