---
keyword: PushEvStat
summary: Free rows in the push-event queue.
availability:
  standalone: []
  central-i:
  - v5
can_code: 911
attributes:
  access: ro
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
  - 64
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvStat

Free rows in the push-event queue.

## Overview

`PushEvStat` is a read-only count of the free rows in the [push-event](00-overview.md) queue. The queue holds **64 rows**, and each row holds one event. `PushEvStat` reads 64 when the queue is empty and 0 when it is full.

The controller's background loop updates it on every pass, whether or not anything is sent. The same figure goes to the host in every packet header, as the `freeRows` field, so a host that reads the push socket does not need to poll this keyword. The header value is taken when the packet is built, before the events in it are removed from the queue.

It is a non-axis value and is not saved to flash.

## How to read it

| Value | Meaning |
|---|---|
| `64` | queue empty: every event so far has been sent |
| `1`-`63` | events are waiting to be sent |
| `0` | queue full: the next event will be dropped and counted in [PushEvLost](PushEvLost.md) |

A value that stays low while [PushEvEnable](PushEvEnable.md) is 1 can mean that no host is reading the push socket, so the controller's sends are failing and events are accumulating.

The queue depth (64) is also reported in [Identity](../01-status/Identity.md)`[75]`.

## Examples

```text
APushEvStat          ; free rows in the event queue (64 = empty)
```

## See also

- [PushEvLost](PushEvLost.md) / [PushEvTotLost](PushEvTotLost.md) — events dropped when the queue is full
- [PushEvFillPct](PushEvFillPct.md) — fill level that forces a send
- [Push Events overview](00-overview.md)
