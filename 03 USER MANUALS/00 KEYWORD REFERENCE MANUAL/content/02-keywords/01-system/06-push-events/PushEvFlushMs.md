---
keyword: PushEvFlushMs
summary: Longest time a queued push event waits before it is sent, in milliseconds.
availability:
  standalone: []
  central-i:
  - v5
can_code: 913
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
  - 1000
  default: 5
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvFlushMs

Longest time a queued push event waits before it is sent, in milliseconds.

## Overview

`PushEvFlushMs` is the periodic send trigger for [push events](00-overview.md). The controller sends the queued events once more than `PushEvFlushMs` milliseconds have passed since the last **successful** send. The range is 1 to 1000 and the default is **5**. It is a non-axis setting, saved to flash with [Save](../02-operation/Save.md).

It works together with [PushEvFillPct](PushEvFillPct.md): the queue is sent when **either** trigger fires.

## How it works

The timer restarts only when a packet is sent successfully. It does not restart when the queue is empty. As a result:

- **A single event on a quiet channel** is sent on the controller's next background pass, because the time since the last send has usually passed `PushEvFlushMs` already.
- **Under a steady trickle of events**, packets go out at most once every `PushEvFlushMs`. Events that arrive in between are collected and sent together, up to 28 per packet.
- **Under a burst**, the queue reaches the [PushEvFillPct](PushEvFillPct.md) level and is sent without waiting for the timer.

With the 5 ms default, an event reaches the host about as quickly as a host polling every 5 ms would notice it, without the polling traffic. A longer period sends fewer, fuller packets. A machine that prefers the 100 ms cadence that `printf` output uses on the same socket can set `PushEvFlushMs=100`.

`PushEvFlushMs` applies to push events only. It does not change `printf` timing.

The period is counted by the controller's millisecond tick, which runs at 1024 Hz (every 16 control cycles), so one unit is about 0.98 ms.

> **`PushEvFlushMs` does not limit retries.** If a send is refused, the timer is not restarted, so the controller tries again on every background pass until a send succeeds, whatever the setting. If a host is connected but not reading, each of those attempts can hold the background loop for up to about 6 seconds. See the [overview](00-overview.md#how-it-works).

## Examples

```text
APushEvFlushMs       ; read the period
APushEvFlushMs=5     ; default: send queued events within about 5 ms
APushEvFlushMs=100   ; send at most every 100 ms under a steady trickle
```

## See also

- [PushEvFillPct](PushEvFillPct.md) — the fill-level trigger
- [PushEvStat](PushEvStat.md) — free rows in the queue
- [Push Events overview](00-overview.md) — sending rules
