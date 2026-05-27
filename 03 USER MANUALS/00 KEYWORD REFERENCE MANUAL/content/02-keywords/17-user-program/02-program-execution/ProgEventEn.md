---
keyword: ProgEventEn
summary: Enables or disables handling of an individual user program event.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgEventEn` enables (`1`) or disables (`0`) the handling of a specific user program event. When an event is disabled, any pending occurrence of it is cleared and the event is not processed at all, including the sensing of the event. This is the per-event control; [ProgEventGEn](ProgEventGEn.md) is the global switch that gates all events at once. The trigger for each event is defined by [ProgEventPar](ProgEventPar.md), [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), and [ProgEventMask](ProgEventMask.md). It is a non-axis array parameter (one element per event) and is not saved to flash.

## Examples

```text
AProgEventEn[1]=1    ; enable handling of event 1
AProgEventEn[1]=0    ; disable event 1 and clear any pending occurrence
```

## See also

- [ProgEventGEn](ProgEventGEn.md) — global enable for all events
- [ProgEventStat](ProgEventStat.md) — per-event state (waiting / pending / in service)
- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
