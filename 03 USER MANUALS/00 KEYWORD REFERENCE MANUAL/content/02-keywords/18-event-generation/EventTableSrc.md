---
keyword: EventTableSrc
summary: Selects the position source used to evaluate event table triggers.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 313
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableSrc

Selects the position source used to evaluate event table triggers.

## Overview

`EventTableSrc` selects which set of table positions the comparator uses when generating table-driven events: the raw entries in [EventTable](EventTable.md), or the error-map-corrected entries in [EventTableCor](EventTableCor.md). It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

| Value | Position source compared against feedback |
|-------|-------------------------------------------|
| 0 | Raw table: the values in [EventTable](EventTable.md) are used directly as compare positions. |
| 1 | Corrected table: the values in [EventTableCor](EventTableCor.md), produced by [EventCorrect](EventCorrect.md), are used as compare positions. |

Use `EventTableSrc` = 1 when an encoder error map is active and you want pulses to fire at the *true* commanded positions rather than the uncorrected positions. Run [EventCorrect](EventCorrect.md) to populate [EventTableCor](EventTableCor.md) before arming.

When a pure-software comparison is in effect, the feedback the comparator reads is already error-corrected, so the raw [EventTable](EventTable.md) is used regardless of this setting.

## Examples

```text
AEventTableSrc=0     ; compare against the raw EventTable (default)
AEventTableSrc=1     ; compare against the corrected EventTableCor
AEventTableSrc       ; query the current source
```

## See also

- [EventTable](EventTable.md) — table of event positions
- [EventSelect](EventSelect.md) — selects which output line the event pulse drives
- [EventTableBeg](EventTableBeg.md) — first active table index
