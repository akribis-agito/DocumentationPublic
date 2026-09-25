---
keyword: PushEvEnable
summary: Master switch for push events; any 0-1 change empties the event queue.
availability:
  standalone: []
  central-i:
  - v5
can_code: 907
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvEnable

Master switch for push events; any 0-1 change empties the event queue.

## Overview

`PushEvEnable = 1` turns on [push events](00-overview.md): the controller starts detecting the event types selected in [PushEvSelect](PushEvSelect.md) and sends them to the host on the push socket (TCP port 50010). `PushEvEnable = 0` (default) turns them off, and no events are detected or queued.

The keyword is **not saved to flash**. Push events are always off after power-up, and the host that wants them turns them on.

## How it works

Any real change of value, from 0 to 1 or from 1 to 0, resets the event queue:

- every queued event is discarded, so [PushEvStat](PushEvStat.md) returns to 64 (all rows free);
- [PushEvLost](PushEvLost.md) is cleared to 0. [PushEvTotLost](PushEvTotLost.md) is not changed.

Writing the value the keyword already holds changes nothing, and the queue is kept.

When push events are turned on in the middle of a move, the move already in progress is not reported as having ended at the moment of the switch. The controller records the current motion state of every axis before it starts detecting, so only a later ending produces an event.

To start a host session with an empty queue, for example after reconnecting to the push socket, write `0` and then `1`.

## Examples

```text
APushEvEnable=1      ; start detecting and sending push events
APushEvEnable        ; read the switch
APushEvEnable=0      ; stop; the queue is emptied
```

## See also

- [Push Events overview](00-overview.md) — event types, sending rules and packet format
- [PushEvSelect](PushEvSelect.md) — which event types are detected on each axis
- [PushEvStat](PushEvStat.md) / [PushEvLost](PushEvLost.md) — queue state after a reset
