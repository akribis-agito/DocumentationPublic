---
keyword: EventTableSel
summary: Per-entry selection array controlling each event table entry's characteristics.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 318
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 7
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableSel

Per-entry selection array controlling each event table entry's characteristics.

## Overview

`EventTableSel` is an array that assigns a width-value index or mode selection to each [EventTable](EventTable.md) entry, controlling per-entry pulse characteristics. It complements the global mode set by [EventSelect](EventSelect.md) and the per-entry pulse widths in [EventTableWid](EventTableWid.md). The active range of entries is bounded by [EventTableBeg](EventTableBeg.md) and [EventTableEnd](EventTableEnd.md). It is an axis-related array parameter and is not saved to flash.

## Examples

```text
AEventTableSel[1]=1      ; selection for the first table entry
AEventTableSel[2]=0      ; selection for the second table entry
AEventTableSel[1]       ; query the first entry's selection
```

## See also

- [EventTable](EventTable.md) — table of event positions
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
- [EventTableBeg](EventTableBeg.md) — first active table index
- [EventTableEnd](EventTableEnd.md) — last active table index
