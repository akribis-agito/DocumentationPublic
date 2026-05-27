---
keyword: EventSelect
summary: Selects which output line of a multi-event output group the current event pulse drives.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 317
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
  - 7
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventSelect

Selects which output line of a multi-event output group the current event pulse drives.

## Overview

The event generator can drive a group of event output lines. `EventSelect` chooses which line (or lines) of that group the next event pulse is routed to, leaving the other lines in their idle ("blocked") state. It does **not** choose the position-trigger scheme — that is [EventType](EventType.md) — nor does it arm generation, which is done with [EventOn](EventOn.md).

`EventSelect` is an axis-related parameter saved to flash and can be changed at any time. The default value is `1` (the first output line).

## How it works

When `EventSelect` is written, the controller programs the event-output routing so the next pulse appears only on the selected line(s); the unselected lines are held at their idle level. The idle level of the blocked lines follows the sign of [EventPulseWid](EventPulseWid.md):

| EventPulseWid sign | Idle level of blocked lines |
|--------------------|-----------------------------|
| Positive (normal polarity) | low (`0`) |
| Negative (inverted polarity) | high (`1`) |

In table mode ([EventType](EventType.md) = 2 or 3) the active line is taken from the per-entry value in [EventTableSel](EventTableSel.md) instead of from a single `EventSelect` setting: as the generator advances through the table, `EventSelect` is reloaded from the table entry for each event, so different positions can fire on different output lines. Reading `EventSelect` during a table sequence therefore reports the line used by the most recent event.

## Examples

```text
AEventSelect=1       ; route event pulses to output line 1 (default)
AEventSelect        ; read the line used by the current/most recent event
```

## See also

- [EventTableSel](EventTableSel.md) — per-entry output-line selection used in table mode
- [EventType](EventType.md) — single / by-gap / table position-trigger scheme
- [EventPulseWid](EventPulseWid.md) — pulse width and polarity; its sign sets the idle level of blocked lines
- [EventOn](EventOn.md) — arms event generation
