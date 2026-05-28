---
keyword: ProgEventOn
summary: Activates or disables handling of user program events.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 527
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
---
# ProgEventOn

Activates or disables handling of user program events.

## Overview

`ProgEventOn` is the master switch for the whole user-program event system. It activates (`1`) or disables (`0`) both the *sensing* of events and the *servicing* of events. When set to `0`, every event is forced back to "waiting for trigger", so all pending occurrences are discarded and no further events are sensed or serviced. It is a non-axis scalar parameter and is not saved to flash (default `0`).

A user program event lets the controller run a handler function automatically whenever a chosen parameter meets a chosen condition — without the program having to poll for it. Up to **5 events** (numbered 1–5) can be defined. Each event is described by four parameters that form a trigger definition very similar to a data-recording trigger:

- [ProgEventPar](ProgEventPar.md) — the monitored parameter (the trigger source)
- [ProgEventType](ProgEventType.md) — the comparison/edge condition
- [ProgEventVal](ProgEventVal.md) — the threshold value compared against
- [ProgEventMask](ProgEventMask.md) — a bitmask applied before comparison

Two further switches gate this engine alongside `ProgEventOn`: [ProgEventGEn](ProgEventGEn.md) (global) and [ProgEventEn](ProgEventEn.md) (per event). The difference is what they do to *sensing*:

| Control | Scope | Effect of setting to 0 |
|---|---|---|
| `ProgEventOn` | all events | Stops sensing **and** servicing; clears all pending occurrences (forces every event back to "waiting for trigger") |
| [ProgEventGEn](ProgEventGEn.md) | all events | Stops servicing only; events are still sensed and may become pending |
| [ProgEventEn](ProgEventEn.md) | one event | Stops servicing of that one event only; the event is still sensed and may become pending, but is not serviced while disabled |

## How it works

Three conditions must all be true for a triggered event to actually run its handler: `ProgEventOn = 1`, [ProgEventGEn](ProgEventGEn.md)` = 1`, and [ProgEventEn](ProgEventEn.md) of that event `= 1`. The full pipeline is:

1. **Sense (evaluate).** While sensing is enabled, the controller evaluates each defined event every control cycle: it reads the monitored parameter, applies the mask, and tests the condition selected by [ProgEventType](ProgEventType.md) against [ProgEventVal](ProgEventVal.md). An event is evaluated only while it is in the "waiting for trigger" state.
2. **Fire.** When the condition is met, the event moves to the "pending for service" state (reported by [ProgEventStat](ProgEventStat.md)`= 1`).
3. **Run the handler.** The handler runs on the main program thread (thread 1). Each pass, the controller scans events 1→5 and services the first one that is enabled and pending, so a lower event number takes precedence when several are pending at once. The handler is called like a function: the current execution point is pushed onto the call stack and execution jumps to the event's handler; the event moves to the "in service" state (`ProgEventStat = 2`).
4. **Complete.** When the handler executes [Return](Return.md), execution resumes where it was interrupted and the event returns to "waiting for trigger", re-armed for the next occurrence. An event cannot fire again while it is being serviced.

## Examples

```text
AProgEventOn=1       ; enable the event system (sensing + servicing)
AProgEventOn=0       ; disable everything and clear all pending events
```

## See also

- [ProgEventGEn](ProgEventGEn.md) — global servicing enable that keeps sensing active
- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventStat](ProgEventStat.md) — per-event state (waiting / pending / in service)
- [ProgEventPar](ProgEventPar.md) — monitored parameter (trigger source)
- [Return](Return.md) — completes servicing of an event handler
