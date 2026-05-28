---
keyword: ProgEventEn
summary: Enables or disables servicing of an individual user program event.
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

Enables or disables servicing of an individual user program event.

## Overview

`ProgEventEn` enables (`1`) or disables (`0`) servicing of one specific user program event, indexed by event number. While an event is disabled, its handler is never run — even if the trigger condition occurs and the event becomes pending. Sensing is unaffected: as long as [ProgEventOn](ProgEventOn.md)` = 1`, a disabled event still evaluates its trigger and can become pending; it simply is not serviced until it is re-enabled. This makes it the per-event servicing gate, alongside [ProgEventGEn](ProgEventGEn.md) (which suspends servicing for all events) and [ProgEventOn](ProgEventOn.md) (the master switch that gates sensing as well as servicing). The trigger for each event is defined by [ProgEventPar](ProgEventPar.md), [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), and [ProgEventMask](ProgEventMask.md). It is a non-axis array parameter with one element per event (indices `[1]`–`[5]`, for up to 5 events) and is not saved to flash (default `0`).

## How it works

An event's handler runs only when all three gates are open: [ProgEventOn](ProgEventOn.md)` = 1`, [ProgEventGEn](ProgEventGEn.md)` = 1`, and `ProgEventEn` of that event `= 1`. With [ProgEventOn](ProgEventOn.md)` = 1`, each control cycle the controller reads the monitored parameter ([ProgEventPar](ProgEventPar.md)), applies [ProgEventMask](ProgEventMask.md), and tests it against [ProgEventVal](ProgEventVal.md) using the condition in [ProgEventType](ProgEventType.md); when the condition is met the event becomes pending. `ProgEventEn` then decides whether a pending occurrence of *that* event is serviced: with `ProgEventEn[n] = 1` its handler runs on the main thread and the event re-arms after the handler's [Return](Return.md); with `ProgEventEn[n] = 0` the handler is held off, even though the event is still sensed and may sit pending. To clear all pending occurrences and force every event back to "waiting for trigger", set [ProgEventOn](ProgEventOn.md)` = 0`.

## Examples

```text
AProgEventEn[1]=1    ; enable servicing of event 1
AProgEventEn[1]=0    ; stop servicing event 1 (it is still sensed and may stay pending)
```

## See also

- [ProgEventGEn](ProgEventGEn.md) — global enable for all events
- [ProgEventStat](ProgEventStat.md) — per-event state (waiting / pending / in service)
- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
