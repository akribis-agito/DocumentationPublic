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

`EventTableSel` is an array that assigns a selection value (range 0–7) to each [EventTable](EventTable.md) entry, controlling that entry's output characteristics. It is the per-entry counterpart of the global [EventSelect](EventSelect.md): for table-driven events the entry's selection takes the place of the global mode at the moment its pulse is produced. The active range of entries is bounded by [EventTableBeg](EventTableBeg.md) and [EventTableEnd](EventTableEnd.md). It is an axis-related array parameter and is not saved to flash.

## How it works

As the controller advances through the active table range, it reads the `EventTableSel` value for the entry it is about to fire and applies it to the output pulse generator together with that entry's width from [EventTableWid](EventTableWid.md). This lets different entries drive different output configurations within one pass — for example, routing pulses to different event outputs or selecting which entries produce an active pulse versus an idle (blocked) slot. The 3-bit value (0–7) is applied per pulse; the new selection takes effect only after the previous pulse has finished, so closely spaced entries do not corrupt the pulse in progress.

The first active entry's selection (at [EventTableBeg](EventTableBeg.md)) is loaded when events are armed with [EventOn](EventOn.md) = 1; each subsequent entry's selection is loaded as the table advances.

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
