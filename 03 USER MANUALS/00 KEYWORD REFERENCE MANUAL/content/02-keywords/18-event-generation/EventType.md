---
keyword: EventType
summary: Selects the compare scheme for event generation (single, by-gap, or by-table).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 180
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
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventType

Selects the compare scheme for event generation (single, by-gap, or by-table).

## Overview

Events are pulses on a designated output generated when the actual feedback position equals a required compare position. `EventType` determines how those compare positions are derived, and is armed with [EventOn](EventOn.md). The pulse shape is set by [EventPulseWid](EventPulseWid.md).

## How it works

| Value | Compare scheme |
|-------|----------------|
| 0 | Single event: a pulse is generated when the feedback position equals [EventBegPos](EventBegPos.md). |
| 1 | Event by gap: a first pulse is generated when the position equals [EventBegPos](EventBegPos.md); another pulse is generated every time the distance set by [EventGap](EventGap.md) is passed. Pulses stop once the position exceeds [EventEndPos](EventEndPos.md). |
| 2 | Events by table: a table of positions where events should be generated is entered into the `GenData[]` array. [EventTableBeg](EventTableBeg.md) is the index of the table start and [EventTableEnd](EventTableEnd.md) is the index of the table end. The positions in the table must be ordered from low to high. |

> **Documentation pending:** the attribute range allows values up to 4, but only modes 0–2 are described in the source reference. Modes 3 and 4 are not yet documented.

## Examples

```text
AEventType=0         ; single event at EventBegPos
AEventType=1         ; event by gap
AEventType=2         ; events by table
AEventType          ; query the current compare scheme
```

## See also

- [EventOn](EventOn.md) — arms event generation for the selected type
- [EventBegPos](EventBegPos.md) — first event position (modes 0 and 1)
- [EventGap](EventGap.md) — spacing between events (mode 1)
- [EventEndPos](EventEndPos.md) — last event position (mode 1)
- [EventTable](EventTable.md) — position table (mode 2)
