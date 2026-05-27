---
keyword: ProgEventEn
summary: Enables or disables handling of an individual user program event.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 524
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 6
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
---
# ProgEventEn

Enables or disables handling of an individual user program event.

## Overview

`ProgEventEn` enables (`1`) or disables (`0`) one specific user program event, indexed by event number. When an event is disabled, any pending occurrence of it is cleared and the event is not processed at all — including sensing — so a disabled event neither evaluates its trigger nor runs its handler. This makes it the per-event equivalent of [ProgEventOn](ProgEventOn.md) (which acts on all events), as distinct from [ProgEventGEn](ProgEventGEn.md), which only suspends servicing while leaving sensing active. The trigger for each event is defined by [ProgEventPar](ProgEventPar.md), [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), and [ProgEventMask](ProgEventMask.md). It is a non-axis array parameter with one element per event (indices `[1]`–`[5]`, for up to 5 events) and is not saved to flash (default `0`).

## How it works

An event's handler runs only when all three gates are open: [ProgEventOn](ProgEventOn.md)` = 1`, [ProgEventGEn](ProgEventGEn.md)` = 1`, and `ProgEventEn` of that event `= 1`. Setting `ProgEventEn[n] = 1` arms event *n*: each control cycle the controller reads the monitored parameter ([ProgEventPar](ProgEventPar.md)), applies [ProgEventMask](ProgEventMask.md), and tests it against [ProgEventVal](ProgEventVal.md) using the condition in [ProgEventType](ProgEventType.md). When the condition is met the event becomes pending; when serviced, its handler runs on the main thread and the event re-arms after the handler's [Return](Return.md). Setting `ProgEventEn[n] = 0` immediately returns event *n* to the "waiting for trigger" state and discards any pending occurrence.

## Examples

```text
AProgEventEn[1]=1    ; enable (arm) event 1
AProgEventEn[1]=0    ; disable event 1 and clear any pending occurrence
```

## See also

- [ProgEventGEn](ProgEventGEn.md) — global enable for all events
- [ProgEventStat](ProgEventStat.md) — per-event state (waiting / pending / in service)
- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
