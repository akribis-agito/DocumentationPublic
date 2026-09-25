---
keyword: PushEvFillPct
summary: Push-event queue fill level, in percent, that forces a send.
availability:
  standalone: []
  central-i:
  - v5
can_code: 914
attributes:
  access: rw
  scope: non-axis
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
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvFillPct

Push-event queue fill level, in percent, that forces a send.

## Overview

`PushEvFillPct` is the pressure trigger for [push events](00-overview.md). When the event queue is at least `PushEvFillPct` percent full, the controller sends the queued events at once, without waiting for [PushEvFlushMs](PushEvFlushMs.md). The range is 1 to 100 and the default is **50**. It is a non-axis setting, saved to flash with [Save](../02-operation/Save.md).

The queue is sent when **either** this trigger or the `PushEvFlushMs` timer fires.

## How it works

The fill level is compared against the queue depth of 64 rows:

| `PushEvFillPct` | Sent as soon as the queue holds |
|---|---|
| `1` | 1 event |
| `25` | 16 events |
| `50` (default) | 32 events |
| `100` | 64 events (the queue is full) |

A packet carries at most 28 events and the controller sends one packet per background pass, so a large backlog drains over several passes.

The setting is a percentage rather than a row count so that it keeps its meaning if the queue depth changes. [Identity](../01-status/Identity.md)`[75]` reports the depth.

`PushEvFillPct` applies to push events only. `printf` output on the same socket keeps its own fixed trigger.

## Examples

```text
APushEvFillPct       ; read the fill trigger
APushEvFillPct=50    ; default: send once the queue is half full
APushEvFillPct=25    ; send earlier under a burst
```

## See also

- [PushEvFlushMs](PushEvFlushMs.md) — the periodic trigger
- [PushEvStat](PushEvStat.md) — free rows in the queue
- [Push Events overview](00-overview.md) — sending rules
