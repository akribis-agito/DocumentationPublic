---
keyword: ProgSnapVal
summary: Holds the values captured by the program snapshot mechanism.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 538
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ProgSnapVal

Holds the values captured by the program snapshot mechanism.

## Overview

`ProgSnapVal` is a read-only array holding the values captured by the program snapshot mechanism when a user-program thread hits a run-time error. It is the program-debugging counterpart of the fault-snapshot values in [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md): reading it after an error gives a frozen picture of that thread's program state at the instant it failed. The default element value is `-1`, meaning nothing has been captured for that slot (also the state after [ProgSnapSrc](ProgSnapSrc.md) is reconfigured). It is a non-axis status variable and is not saved to flash.

## How it works

The snapshot is taken in one shot at the moment a user-program thread raises a run-time error — the same event that sets that thread's [ProgError](ProgError.md), appends to [ErrLog](../../07-status-and-faults/ErrLog.md), and halts the thread.

The array is organized as one **10-element block per thread** (up to 8 threads on a standalone controller, or 12 on a Central-i master): thread 1 occupies `ProgSnapVal[1]…[10]`, thread 2 `[11]…[20]`, and so on (index `[0]` is unused so indices start at 1). Within each thread's block the layout is fixed; only the first four entries come from your [ProgSnapSrc](ProgSnapSrc.md) configuration:

| Slot in block | Captured value | Source |
|---|---|---|
| 1 | User-selected parameter 1 | [ProgSnapSrc](ProgSnapSrc.md) slot 1 |
| 2 | User-selected parameter 2 | [ProgSnapSrc](ProgSnapSrc.md) slot 2 |
| 3 | User-selected parameter 3 | [ProgSnapSrc](ProgSnapSrc.md) slot 3 |
| 4 | User-selected parameter 4 | [ProgSnapSrc](ProgSnapSrc.md) slot 4 |
| 5 | Program location ([ProgPointer](ProgPointer.md)) | fixed |
| 6 | Free space in the numeric (expression) stack ([ProgExpDepth](ProgExpDepth.md)) | fixed |
| 7 | Free space in the call stack ([ProgCallDepth](ProgCallDepth.md)) | fixed |
| 8 | Reserved | fixed |
| 9 | Run-time error code ([ProgError](ProgError.md)) | fixed |
| 10 | Capture time (s since power-on) | fixed |

A user slot whose [ProgSnapSrc](ProgSnapSrc.md) entry is `0` (disabled) stays at `-1`. Captured values for scaled parameters are stored in raw (internal) units.

To read a value for a given thread, compute its slot: `(thread − 1) × 10 + slot-in-block`. For example, thread 2's run-time error code is `ProgSnapVal[19]`.

## Examples

```text
AProgSnapVal[1]     ; thread 1, first user-selected snapshot source
AProgSnapVal[9]     ; thread 1, the run-time error code (ProgError) at capture
AProgSnapVal[10]    ; thread 1, capture time (s since power-on)
AProgSnapVal[19]    ; thread 2, the run-time error code
AProgSnapVal        ; read the whole snapshot
```

## Changes between versions

In v4 the captured values are 32-bit. In v5 (Central-i) they are 64-bit: wide values are captured at full resolution, and floating-point parameters are stored as their bit pattern rather than a truncated integer. The per-thread block layout above is the same in both versions.

## See also

- [ProgSnapSrc](ProgSnapSrc.md) — selects the four user parameters per thread
- [ProgError](ProgError.md) — the run-time error that triggers the capture (also captured in the block)
- [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md) — fault-snapshot captured values
