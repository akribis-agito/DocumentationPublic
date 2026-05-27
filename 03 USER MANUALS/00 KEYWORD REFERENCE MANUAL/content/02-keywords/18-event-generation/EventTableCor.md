---
keyword: EventTableCor
summary: Read-only array of corrected event positions produced by EventCorrect.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 315
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableCor

Read-only array of corrected event positions produced by EventCorrect.

## Overview

`EventTableCor` is a read-only array that holds the corrected event positions after applying the position correction computed by [EventCorrect](EventCorrect.md). It mirrors [EventTable](EventTable.md) entry-for-entry but with the encoder error-map correction applied, expressed in user units. It is an axis-related array status variable and is not saved to flash.

## How it works

When the axis runs with an active encoder error map, the commanded table positions in [EventTable](EventTable.md) do not coincide with the *true* positions the comparator sees, because the map shifts feedback. Running [EventCorrect](EventCorrect.md) walks each active entry, looks up the mapping correction at that position (1D, 2D, or 3D interpolation, depending on the map), and writes the adjusted value into the matching `EventTableCor` element. The result is the position at which the corrected feedback will actually reach the intended commanded point.

`EventTableCor` is used as the comparator source only when [EventTableSrc](EventTableSrc.md) = 1. With `EventTableSrc` = 0 the raw [EventTable](EventTable.md) is used and `EventTableCor` is ignored. When a pure-software comparison is in effect the feedback is already corrected, so the raw table is sufficient and the corrected table is not needed.

## Examples

```text
AEventTableCor[1]   ; read the first corrected event position
AEventTableCor[2]   ; read the second corrected event position
```

## See also

- [EventTable](EventTable.md) — uncorrected source positions
- [EventCorrect](EventCorrect.md) — command that computes the correction
- [EventTableSel](EventTableSel.md) — per-entry selection
