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
---
# EventTableBeg

Starting index of the active region within the event table.

## Overview

`EventTableBeg` sets the starting index of the active region within [EventTable](EventTable.md), allowing a subset of the table entries to be used for event generation. It pairs with [EventTableEnd](EventTableEnd.md), which marks the last active entry. The index is 1-based (range 1–100). It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

When table-driven events are armed with [EventOn](EventOn.md) = 1, the controller loads the [EventTable](EventTable.md) entry at the `EventTableBeg` index as the first compare position, and copies that entry's [EventTableSel](EventTableSel.md) selection and [EventTableWid](EventTableWid.md) pulse width into the active output settings. From there it advances one index per generated pulse and stops once it passes [EventTableEnd](EventTableEnd.md).

`EventTableBeg` is read when events are armed, so change it before setting `EventOn` = 1. Setting `EventTableBeg` higher than `EventTableEnd` leaves no active entries and no events are generated.

## Examples

```text
AEventTableBeg=1     ; start event generation at the first table entry
AEventTableBeg      ; query the configured start index
```

## See also

- [EventTableEnd](EventTableEnd.md) — last active table index
- [EventTable](EventTable.md) — table of event positions
- [EventTableSel](EventTableSel.md) — per-entry selection
