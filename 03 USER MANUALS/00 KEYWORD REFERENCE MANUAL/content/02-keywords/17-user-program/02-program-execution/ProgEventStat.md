---
keyword: ProgEventStat
summary: Reports each event's state and lets a pending event be cleared.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgEventStat` reports the state of each user program event (indices `[1]`–`[5]`, one per event). It works with the trigger definition ([ProgEventPar](ProgEventPar.md), [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), [ProgEventMask](ProgEventMask.md)) and the enable controls ([ProgEventEn](ProgEventEn.md), [ProgEventGEn](ProgEventGEn.md)) to show where each event is in its lifecycle. While an event is being serviced it cannot be triggered again until servicing completes — that is, until the event handler executes [Return](Return.md). Although the access is read/write, only `0` may be written, which the user can do to clear a pending occurrence. It is a non-axis array parameter and is not saved to flash (default `0`).

## How it works

Each element steps through the lifecycle below:

| Value | State | Meaning |
|----|----|----|
| 0 | Waiting for trigger | Armed and being evaluated each cycle; the trigger condition has not (yet) been met |
| 1 | Pending for service (triggered) | The condition was met; the handler has not run yet |
| 2 | In service | The handler is currently running on the main thread |

State transitions:

- **0 → 1** when the trigger condition is met during sensing (requires [ProgEventOn](ProgEventOn.md)` = 1` and the event's [ProgEventEn](ProgEventEn.md)` = 1`).
- **1 → 2** when the controller dispatches the handler. This happens only while [ProgEventGEn](ProgEventGEn.md)` = 1`; the handler runs on the main thread (thread 1), and when several events are pending the lowest event number is serviced first.
- **2 → 0** when the handler executes [Return](Return.md): the event re-arms (its baseline reading is recaptured) and resumes being sensed.

Forcing an element to `0` (the only writable value) clears a pending occurrence and returns the event to the waiting state. Disabling sensing via [ProgEventOn](ProgEventOn.md)` = 0` or the event's [ProgEventEn](ProgEventEn.md)` = 0` also forces it back to `0`.

## Examples

```text
AProgEventStat[1]   ; read the state of event 1
AProgEventStat[1]=0  ; clear a pending occurrence of event 1
```

## See also

- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventGEn](ProgEventGEn.md) — global servicing enable
- [Return](Return.md) — completes servicing of an event function
