---
keyword: EventTableCor
summary: Read-only array of corrected event positions produced by EventCorrect.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`EventTableCor` is a read-only array that holds the corrected event positions after applying the position correction computed by [EventCorrect](EventCorrect.md). It mirrors [EventTable](EventTable.md) but with mapping offsets applied, expressed in user units. It is an axis-related array status variable and is not saved to flash.

## Examples

```text
AEventTableCor[1]   ; read the first corrected event position
AEventTableCor[2]   ; read the second corrected event position
```

## See also

- [EventTable](EventTable.md) — uncorrected source positions
- [EventCorrect](EventCorrect.md) — command that computes the correction
- [EventTableSel](EventTableSel.md) — per-entry selection
