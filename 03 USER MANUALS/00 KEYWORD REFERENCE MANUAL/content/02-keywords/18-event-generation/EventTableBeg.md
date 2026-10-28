---
keyword: EventTableBeg
summary: Starting index of the active region within the event table.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 184
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
  - 1
  - 100
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# EventTableBeg

Starting index of the active region within the event table.

## Overview

`EventTableBeg` sets the starting index of the active region within [EventTable](EventTable.md), allowing a subset of the table entries to be used for event generation. It pairs with [EventTableEnd](EventTableEnd.md), which marks the last active entry. The index is 1-based; its upper limit equals the table size — 100 on standalone controllers and up to 65000 on central-i. It is an axis-related parameter saved to flash and can normally be changed at any time; the prepared hardware-table restrictions below apply to EventLoad-managed mode 3.

## How it works

For software-table mode and older implementations, when table-driven events are armed with [EventOn](EventOn.md) = 1, the controller loads the [EventTable](EventTable.md) entry at the `EventTableBeg` index as the first compare position, and copies that entry's [EventTableSel](EventTableSel.md) selection and [EventTableWid](EventTableWid.md) pulse width into the active output settings. From there it advances one index per generated pulse and stops once it passes [EventTableEnd](EventTableEnd.md).

For older implementations and software-table mode, `EventTableBeg` is read when events are armed, so change it before setting `EventOn` = 1. The pair is not range-checked against each other: arming always uses the entry at `EventTableBeg` as the first compare position, and the index then advances and stops once it passes `EventTableEnd`. If `EventTableBeg` is set higher than `EventTableEnd`, only the single entry at `EventTableBeg` fires, after which generation stops.

### Prepared hardware-table runs

For AGM800 `EventType=3` with [EventLoad](EventLoad.md), `EventTableBeg` and `EventTableEnd` select the inclusive range to preload (1–2048 rows). The range must satisfy `EventTableBeg <= EventTableEnd`; reversed or empty selections are refused during preparation. The first selected index need not be 1. [EventTblMode](EventTblMode.md)=0 resolves settings from this first selected row. Changing the selected range invalidates a ready load; stop and load the new range before arming.


## Examples

```text
AEventTableBeg=1     ; start event generation at the first table entry
AEventTableBeg      ; query the configured start index
```

## See also

- [EventTableEnd](EventTableEnd.md) — last active table index
- [EventTable](EventTable.md) — table of event positions
- [EventTableSel](EventTableSel.md) — per-entry selection
