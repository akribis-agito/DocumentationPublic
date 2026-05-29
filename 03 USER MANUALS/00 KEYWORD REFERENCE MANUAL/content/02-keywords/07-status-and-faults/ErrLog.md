---
keyword: ErrLog
summary: Read-only circular log of recent errors with their timestamps.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 235
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 257
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ErrLog

Read-only circular log of recent errors with their timestamps.

## Overview

`ErrLog` holds the controller's error log. It is a unit-wide (non-axis), read-only array that records errors as they occur, together with the time each one happened, so you can reconstruct the sequence of faults after a problem. It is not saved to flash. Each positive [ConFlt](ConFlt.md) value is appended here automatically — as are other internal errors such as bad user-program loads and communication errors — and the entire log can be wiped with [ClearErr](ClearErr.md).

The easiest way to read `ErrLog` is with the Agito PCSuite software, which translates each error code to text and converts the power-on time to a clock reading using the PC clock.

## How it works

Each error occupies **two** consecutive array elements (a "pair"):

- **Element 1 of the pair** — the tagged error code (source tag in the upper 8 bits, error code in the lower 24 bits).
- **Element 2 of the pair** — the error time, in seconds since the unit was powered on (a copy of [Time](../01-system/03-timing/Time.md) at the instant of logging).

The first error is therefore in `ErrLog[1]` / `ErrLog[2]`, the second in `ErrLog[3]` / `ErrLog[4]`, and so on. The array holds **128 event pairs** (256 used elements; index `[0]` is unused so that the first usable index is `[1]`). When the buffer is full it wraps back to `ErrLog[1]` and overwrites the oldest pair — it is a circular log, so it always keeps the most recent 128 events but has no overflow flag.

The buffer length scales with the unit's axis count: it is 64 entries per axis plus one unused leading element (`64 x axes + 1`). On this product that is 257 elements = 128 event pairs (256 used; index `[0]` is unused); a unit with a different number of axes has proportionally more or fewer pairs (for example a 3-axis unit is 193 elements = 96 pairs). In all cases it wraps after the last pair, overwriting the oldest, with no overflow flag.

![Two views of ErrLog: the top row shows the 256-element ring as 128 pairs of (code, time), wrapping after pair 128 and overwriting the oldest pair; the bottom row shows the 32-bit layout of pair element 1, with the source tag in the upper 8 bits and the error code in the lower 24 bits](errlog-ring-pairs.svg)

### Tagged error code (pair element 1)

The lower 24 bits are the error code (for controller faults, the same value as [ConFlt](ConFlt.md) — see [Controller error codes](../../04-error-codes/controller-error-codes.md)). The upper 8 bits identify the source:

| Upper 8 bits | Source |
|---|---|
| 0 | Not axis-related (unit-wide error) |
| 1 | Axis A |
| 2 | Axis B |
| 3 | Axis C |
| 4 | Axis D |
| 5 | Axis E |
| 6 | Axis F |
| 7 | Axis G |
| 8 | Axis H |
| 16 + *n* | User-program thread *n* (e.g. 17 = thread 1) |

To split a logged value: `code = ErrLog[k] & 0xFFFFFF` and `source = (ErrLog[k] >> 24) & 0xFF`. Note this differs from the 1-based axis letters elsewhere — here axis A is reported as **1**, not 0, and source 0 means a non-axis error.

## Examples

```text
AErrLog[1]          ; tagged source + error code of the first logged error
AErrLog[2]          ; time (s since power-on) of the first logged error
AErrLog[3]          ; tagged source + error code of the second logged error
AErrLog             ; read the full log
```

To decode the first entry: error code = `AErrLog[1] & 0xFFFFFF`, source = `(AErrLog[1] >> 24) & 0xFF` (1 = axis A, 0 = non-axis).

## See also

- [ClearErr](ClearErr.md) — clear all entries from this log
- [ConFlt](ConFlt.md) — per-axis fault code appended to this log
- [Controller error codes](../../04-error-codes/controller-error-codes.md) — meaning of each error code
- [Time](../01-system/03-timing/Time.md) — power-on time used for the timestamp element
