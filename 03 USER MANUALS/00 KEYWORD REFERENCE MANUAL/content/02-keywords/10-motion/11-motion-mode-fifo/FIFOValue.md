---
keyword: FIFOValue
summary: Read-only array reporting the data value paired with each FIFO motion entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 280
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 129
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
# FIFOValue

Read-only array reporting the data value paired with each FIFO motion entry.

## Overview

`FIFOValue` reports the data value associated with each entry currently held in the FIFO motion queue. Each queue entry consists of a **type**, reported by [FIFOType](FIFOType.md), and a **value**, reported here. Read at the same index, the two arrays together describe one queued entry. The array has 129 elements (index 0 reserved; communication indexes start at 1), matching [FIFOType](FIFOType.md).

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

The meaning of the value depends on the entry type reported at the same index in [FIFOType](FIFOType.md):

| Type (from `FIFOType`) | What the value means |
|----|----|
| 1 — Linear by position delta | Position delta to travel during the segment. |
| 2 — Linear by velocity | Velocity reference held constant for the segment. |
| 3 — Parabolic by position delta | Position delta to travel during the segment. |
| 4 — Parabolic by acceleration | Acceleration reference held constant for the segment. |
| 5 — Cycle time | Segment duration, in control samples, applied to following segments. |

The value stored here is exactly the value supplied to the matching `FIFOPush*` function. To inspect a queued entry, read `FIFOType` and `FIFOValue` at the same index.

## Examples

```text
AFIFOValue[1]       ; read the value of the first entry currently in the queue
```

## See also

- [FIFOType](FIFOType.md) — type paired with each FIFO entry value; full FIFO mode description
- [FIFOStatus](FIFOStatus.md) — queue depth and free/used entries
