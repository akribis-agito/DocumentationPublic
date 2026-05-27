---
keyword: ProgSnapSrc
summary: Selects which parameters the program snapshot mechanism captures.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 537
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgSnapSrc

Selects which parameters the program snapshot mechanism captures.

## Overview

`ProgSnapSrc` configures which controller parameters are captured by the program snapshot mechanism — the debugging counterpart, for user programs, of the fault snapshot configured by [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md). When a user-program thread hits a run-time error, the controller freezes a per-thread snapshot of the program's state into [ProgSnapVal](ProgSnapVal.md); `ProgSnapSrc` chooses the user-selectable parameters that go into it, so you can capture exactly the variables you need to diagnose the failure. It is a non-axis array, saved to flash (default `0`).

## How it works

Each thread gets **4 user-configurable source slots**. The array is laid out per thread, 4 slots each, for up to 8 threads: thread 1 uses `ProgSnapSrc[1]…[4]`, thread 2 uses `[5]…[8]`, and so on (index `[0]` is unused so indices start at 1). These four slots fill the user portion of that thread's [ProgSnapVal](ProgSnapVal.md) block; the rest of each block is filled automatically with fixed program-state values you do not configure here (see [ProgSnapVal](ProgSnapVal.md)).

Each slot holds a **complex CAN code** that names the parameter to capture, encoding three fields:

| Bits | Field |
|---|---|
| 0–9 | CAN code of the parameter |
| 10–14 | Axis number (0 = A; ignored for non-axis parameters) |
| 16–31 | Array index (for array parameters; use 0 for scalars) |

For a scalar parameter on axis A the complex code is just the plain CAN code. Writing `0` to a slot disables it (its [ProgSnapVal](ProgSnapVal.md) entry stays at `-1`). When you set `ProgSnapSrc`, the controller validates the selection, resolves an internal pointer plus a scaling factor for fast capture, and **resets all [ProgSnapVal](ProgSnapVal.md) entries to `-1`**, discarding any previous snapshot — so configure the sources before the error you want to diagnose. Captured values for scaled parameters are stored in raw (internal) units.

## Examples

```text
AProgSnapSrc[1]=<complex CAN code of parameter to capture>   ; thread 1, first user snapshot source
AProgSnapSrc[1]=0   ; disable thread 1's first user slot
AProgSnapSrc        ; read the whole snapshot source configuration
```

## See also

- [ProgSnapVal](ProgSnapVal.md) — values captured by the snapshot mechanism
- [ProgError](ProgError.md) — the per-thread run-time error that triggers the capture
- [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md) — fault-snapshot source selection
