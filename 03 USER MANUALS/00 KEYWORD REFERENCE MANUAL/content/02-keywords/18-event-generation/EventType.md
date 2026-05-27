---
keyword: EventType
summary: Selects the compare scheme for event generation (single, by-gap, or by-table).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
| 0 | **Single event** — one pulse is generated when the feedback position reaches [EventBegPos](EventBegPos.md), then generation stops and [EventOn](EventOn.md) returns to `0`. |
| 1 | **Event by gap** — a first pulse is generated at [EventBegPos](EventBegPos.md); a further pulse is generated each time the distance set by [EventGap](EventGap.md) is passed. Pulses stop once the position passes [EventEndPos](EventEndPos.md) (unless [EventAlwaysOn](EventAlwaysOn.md) forces continuous operation). |
| 2 | **Events by table** — a table of compare positions is used, bounded by [EventTableBeg](EventTableBeg.md) (start index) and [EventTableEnd](EventTableEnd.md) (end index). The controller loads each position in turn and reloads [EventSelect](EventSelect.md) from [EventTableSel](EventTableSel.md) for every event, so each position can fire on a chosen output line. Compare positions are taken from [EventTable](EventTable.md), or from the corrected table [EventTableCor](EventTableCor.md) when so selected. |
| 3 | **Events by table (hardware-buffered)** — same table-driven scheme as mode 2, but the full list of compare positions is pre-loaded into the compare hardware's buffer (FIFO) at arming rather than reloaded one at a time. This supports higher event rates than mode 2 because the hardware advances through the buffered positions without per-event servicing. Available where the compare hardware supports it. |
| 4 | **Trigger now** — fires a single pulse immediately when [EventOn](EventOn.md) is set, without waiting for a position crossing. Use it to assert the event output on demand (for example, to test downstream wiring). |

The by-gap scheme produces a regular pulse train across the window:

<svg xmlns="http://www.w3.org/2000/svg" width="560" height="170" viewBox="0 0 560 170" role="img" aria-label="By-gap event pulse train between EventBegPos and EventEndPos">
  <line x1="40" y1="120" x2="540" y2="120" stroke="#444" stroke-width="1"/>
  <polygon points="540,120 532,116 532,124" fill="#444"/>
  <text x="500" y="140" font-family="sans-serif" font-size="12" fill="#444">position</text>
  <!-- pulses at Beg, Beg+Gap, Beg+2Gap, Beg+3Gap -->
  <g stroke="#1f6feb" stroke-width="2" fill="none">
    <path d="M100,120 L100,60 L112,60 L112,120"/>
    <path d="M210,120 L210,60 L222,60 L222,120"/>
    <path d="M320,120 L320,60 L332,60 L332,120"/>
    <path d="M430,120 L430,60 L442,60 L442,120"/>
  </g>
  <!-- window markers -->
  <line x1="100" y1="50" x2="100" y2="130" stroke="#cb2431" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="470" y1="50" x2="470" y2="130" stroke="#cb2431" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="70" y="45" font-family="sans-serif" font-size="11" fill="#cb2431">EventBegPos</text>
  <text x="442" y="45" font-family="sans-serif" font-size="11" fill="#cb2431">EventEndPos</text>
  <!-- gap arrow -->
  <line x1="112" y1="150" x2="210" y2="150" stroke="#444" stroke-width="1"/>
  <polygon points="112,150 120,146 120,154" fill="#444"/>
  <polygon points="210,150 202,146 202,154" fill="#444"/>
  <text x="135" y="146" font-family="sans-serif" font-size="11" fill="#444">EventGap</text>
</svg>

## Examples

```text
AEventType=0         ; single event at EventBegPos
AEventType=1         ; event by gap
AEventType=2         ; events by table
AEventType=3         ; events by table, hardware-buffered
AEventType=4         ; trigger one event immediately on EventOn
AEventType          ; query the current compare scheme
```

## See also

- [EventOn](EventOn.md) — arms event generation for the selected type
- [EventBegPos](EventBegPos.md) — first event position (modes 0 and 1)
- [EventGap](EventGap.md) — spacing between events (mode 1)
- [EventEndPos](EventEndPos.md) — last event position (mode 1)
- [EventAlwaysOn](EventAlwaysOn.md) — continuous (endless) by-gap generation (mode 1)
- [EventTable](EventTable.md) / [EventTableCor](EventTableCor.md) — position tables (modes 2 and 3)
- [EventTableSel](EventTableSel.md) — per-entry output-line selection (modes 2 and 3)
