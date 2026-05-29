---
keyword: EventOn
summary: Arms event generation; loads the first compare position and is mutually exclusive with Lock.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 178
attributes:
  access: rw
  scope: axis
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
# EventOn

Arms event generation; loads the first compare position and is mutually exclusive with Lock.

## Overview

`EventOn = 1` arms the position-compare engine: the controller loads the first compare position (according to [EventType](EventType.md)) and starts watching the feedback position so an output pulse is fired each time a configured compare position is crossed. It should be set while the axis is at a position before the first requested event (smaller than [EventBegPos](EventBegPos.md) when moving in the positive direction) to prevent unexpected behavior.

Arming is a `0 → 1` edge: writing `EventOn = 1` while it is already `1` does nothing. The `0 → 1` transition resets [EventCntr](EventCntr.md) to `0` (and, on standalone products, clears the position-capture enable since the two functions share the same pin).

## How it works

### Arming (0 → 1)

When `EventOn` transitions from `0` to `1` the controller:

1. Resets [EventCntr](EventCntr.md) to `0`.
2. Selects the first compare position from the scheme set by [EventType](EventType.md): [EventBegPos](EventBegPos.md) for single-event and by-gap modes, or the first table entry (start index) for table modes.
3. Determines the expected travel direction — for single-event mode from the current position relative to [EventBegPos](EventBegPos.md); for by-gap mode from [EventEndPos](EventEndPos.md) relative to [EventBegPos](EventBegPos.md) (so the window may run in either direction); in table mode the direction is derived per entry as the engine advances.
4. Configures the output-pulse shape from [EventPulseWid](EventPulseWid.md) and the routing from [EventSelect](EventSelect.md) / [EventTableSel](EventTableSel.md), loads the first compare position, and starts the compare unit.

The first compare position is reported in [EventNextPos](EventNextPos.md).

### Per-cycle compare → fire → advance

Once armed, each control cycle the engine compares the feedback position against [EventNextPos](EventNextPos.md). When the position reaches the compare point in the expected direction, the output pulse is fired, [EventCntr](EventCntr.md) increments, and the next compare position is prepared:

- **Single event** — generation stops; `EventOn` returns to `0`.
- **By gap** — the compare point advances by [EventGap](EventGap.md). Generation continues until the point passes [EventEndPos](EventEndPos.md), then stops and `EventOn` returns to `0` (unless continuous operation is forced by [EventAlwaysOn](EventAlwaysOn.md)).
- **By table** — the engine steps to the next table entry and reloads [EventSelect](EventSelect.md) from [EventTableSel](EventTableSel.md). After the last entry, generation stops and `EventOn` returns to `0`.

On an incremental (or SIN-COS) encoder the compare and the pulse are performed in hardware, so the pulse is placed precisely at the crossing; the controller only services the bookkeeping each cycle. On an absolute / other non-incremental encoder the compare is done in firmware against the feedback position once per control cycle, so timing is limited to the control-cycle granularity.

### Mutual exclusivity with Lock (standalone only)

On standalone products the position-compare output and the position-capture trigger ([LockEn](../03-encoder/03-event-based-feedback-logging/LockEn-AuxLockEn.md)) share the same hardware pin, so only one can be active at a time. Arming `EventOn = 1` automatically clears `LockEn`, and arming `LockEn` automatically clears `EventOn`. This restriction does not apply to Central-i products, where the two features use independent hardware in the remote drive.

## Examples

```text
AEventOn=1           ; arm event generation (set while below the first event position)
AEventOn=0           ; disable event generation
AEventOn            ; query the current state
```

## See also

- [EventType](EventType.md) — determines which position is loaded first
- [EventNextPos](EventNextPos.md) — reports the next compare position while armed
- [EventCntr](EventCntr.md) — reset to 0 on the 0 → 1 arming edge
- [EventAlwaysOn](EventAlwaysOn.md) — forces continuous (endless) by-gap generation
- [LockEn](../03-encoder/03-event-based-feedback-logging/LockEn-AuxLockEn.md) — position capture; shares the same pin on standalone products
