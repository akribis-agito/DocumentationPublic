---
keyword: EventCntr
summary: Reports event progress; verified hardware tables count retired targets.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 186
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventCntr

Counts events generated since the last EventOn; resettable by the user.

## Verified hardware table (EventType=3 with an EventLoad session)

Reports **retired targets**, not measured electrical pulses or edges, from the current coherent remote snapshot. A zero-width or output-mask-zero record can retire without an edge; toggle records have different edge/cycle counts. Accepted EventLoad clears the count; completion/abort retain terminal counts until a new accepted load. Use EventStatus for full session/freshness/completion checks. Writes are blocked while the table lease owns this state; writing the counter is not a remote engine reset. The legacy pulse-count description below does not apply to this mode.

The remaining legacy behavior below also applies to EventType=3 when no verified-table session owns the axis. The verified-table capability gates EventLoad, not legacy hardware-table arming.

## Overview

`EventCntr` counts the events that have occurred since the last time [EventOn](EventOn.md) was armed. Use it to confirm how many event pulses were produced during a move or to verify expected event coverage against the configured table or range.

## How it works

The controller increments `EventCntr` by one each time the event output fires — that is, on every position crossing that produces a pulse (including the final event of a single-event or table sequence). The counter is reset to `0` on the [EventOn](EventOn.md) `0 → 1` arming edge, so each armed run starts the count from zero. The user may also reset it at any time by writing `0`.

Because it is incremented per fired pulse, `EventCntr` is the reliable way to confirm short events that may be too brief to observe through [EventLoopback](EventLoopback.md).

## Examples

```text
AEventCntr          ; read the number of events since the last EventOn
AEventCntr=0         ; reset the counter
```

## See also

- [EventOn](EventOn.md) — toggling it resets this counter
- [EventNextPos](EventNextPos.md) — position of the next event to be generated
