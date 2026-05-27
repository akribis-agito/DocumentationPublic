---
keyword: EventTableBeg
summary: Starting index of the active region within the event table.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

## Examples

```text
EventTableBeg=1     ; start event generation at the first table entry
EventTableBeg?      ; query the configured start index
```

## See also

- [EventTableEnd](EventTableEnd.md) — last active table index
- [EventTable](EventTable.md) — table of event positions
- [EventTableSel](EventTableSel.md) — per-entry selection
