---
keyword: ProgEventGEn
summary: Global enable for servicing all user program events.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 526
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
# ProgEventGEn

Global enable for servicing all user program events.

## Overview

`ProgEventGEn` globally enables (`1`) or disables (`0`) the *servicing* of all user program events, without affecting whether they are sensed. Unlike [ProgEventOn](ProgEventOn.md) (which gates sensing as well as servicing, and clears all pending occurrences when set to 0), `ProgEventGEn` gates servicing only. Like the per-event servicing gate [ProgEventEn](ProgEventEn.md), setting `ProgEventGEn = 0` leaves sensing fully active: events still evaluate their triggers and may move to the "pending for service" state ([ProgEventStat](ProgEventStat.md)`= 1`), but no handler runs. When `ProgEventGEn` is set back to `1`, any event that became pending in the meantime is then serviced. Use it to suspend and resume event handling as a whole without losing pending triggers. It is a non-axis scalar parameter and is not saved to flash (default `0`).

## How it works

For an event's handler to run, all three gates must be open at once: [ProgEventOn](ProgEventOn.md)` = 1`, `ProgEventGEn = 1`, and that event's [ProgEventEn](ProgEventEn.md)` = 1`. The handler-dispatch step (which scans events 1→5 and runs the first enabled, pending event on the main thread) is the part `ProgEventGEn` gates. Because sensing continues while `ProgEventGEn = 0`, this is the right switch for a critical section: pending events queue up and are serviced in order once you re-enable servicing.

## Examples

```text
AProgEventGEn=0      ; suspend servicing of all events (events still sensed)
AProgEventGEn=1      ; resume servicing; pending events are then handled
```

## See also

- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventStat](ProgEventStat.md) — per-event state
- [ProgEventOn](ProgEventOn.md) — event-handling enable
