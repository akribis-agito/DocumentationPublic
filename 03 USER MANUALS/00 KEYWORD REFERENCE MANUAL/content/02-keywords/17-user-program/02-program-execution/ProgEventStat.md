---
keyword: ProgEventStat
summary: Reports each event's state and lets a pending event be cleared.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 525
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventStat

Reports each event's state and lets a pending event be cleared.

## Overview

`ProgEventStat` reports the state of each user program event. It works with the trigger definition ([ProgEventPar](ProgEventPar.md), [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), [ProgEventMask](ProgEventMask.md)) and the enable controls ([ProgEventEn](ProgEventEn.md), [ProgEventGEn](ProgEventGEn.md)) to show where each event is in its lifecycle. While an event is being serviced it cannot be triggered again until servicing completes — that is, until the event function executes [Return](Return.md). Although the access is read/write, only `0` may be written, which the user can do to clear a pending event. It is a non-axis array parameter (one element per event) and is not saved to flash.

## How it works

| Value | State |
|----|----|
| 0 | Waiting for trigger |
| 1 | Pending for service (triggered) |
| 2 | In service |

## Examples

```text
ProgEventStat[1]?   ; read the state of event 1
ProgEventStat[1]=0  ; clear a pending occurrence of event 1
```

## See also

- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventGEn](ProgEventGEn.md) — global servicing enable
- [Return](Return.md) — completes servicing of an event function
