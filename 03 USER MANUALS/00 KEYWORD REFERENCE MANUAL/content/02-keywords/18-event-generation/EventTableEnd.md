---
keyword: EventTableEnd
summary: Ending index of the active region within the event table.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 185
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
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventTableEnd

Ending index of the active region within the event table.

## Verified hardware table (EventType=3 with an EventLoad session)

[EventLoad](EventLoad.md) captures the inclusive selected range before arming: N=EventTableEnd−EventTableBeg+1 must be 1..2048. Invalid ranges are refused rather than truncated or treated as a single event. The larger controller-side array remains available, but only the selected range enters one hardware session. Strict ordering in one direction is required in both original and corrected remote coordinates; no duplicates, reversals or signed-counter rollover. Configure before loading. Changes invalidate Ready; conflicting writes while transfer/arm/run owns the session are refused. EventOn=1 does not reread or upload the live table.

The remaining legacy behavior below also applies to EventType=3 when no verified-table session owns the axis. The verified-table capability gates EventLoad, not legacy hardware-table arming.

## Overview

`EventTableEnd` sets the ending index of the active region within [EventTable](EventTable.md), defining the last entry used for event generation. It pairs with [EventTableBeg](EventTableBeg.md), which marks the first active entry. The index is 1-based (range 1–100). It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

In table-driven mode ([EventType](EventType.md) = 2) the controller advances through [EventTable](EventTable.md) one index per generated pulse, starting at [EventTableBeg](EventTableBeg.md). After producing the pulse for the `EventTableEnd` entry, the next advance carries the index past `EventTableEnd` and event generation stops; the controller clears [EventOn](EventOn.md) to 0. The number of pulses a full pass produces is therefore `EventTableEnd − EventTableBeg + 1`, which you can confirm with [EventCntr](EventCntr.md).

## Examples

```text
AEventTableEnd=10    ; use table entries up to index 10
AEventTableEnd      ; query the configured end index
```

## See also

- [EventTableBeg](EventTableBeg.md) — first active table index
- [EventTable](EventTable.md) — table of event positions
- [EventTableSel](EventTableSel.md) — per-entry selection
