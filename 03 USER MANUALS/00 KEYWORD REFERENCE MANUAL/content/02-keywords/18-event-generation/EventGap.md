---
keyword: EventGap
summary: Position spacing between successive events in by-gap mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 182
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventGap

Position spacing between successive events in by-gap mode.

## Overview

`EventGap` defines the position gap, in user units, between successive event generations in the by-gap event mode (see [EventType](EventType.md)). Events begin at [EventBegPos](EventBegPos.md) and repeat every `EventGap` until [EventEndPos](EventEndPos.md) is passed. If `EventGap` is small and the velocity is high, a large [EventPulseWid](EventPulseWid.md) may cause successive events to overlap.

## How it works

After each by-gap event fires, the controller adds `EventGap` to the most recent compare position to obtain the next one, then loads it as [EventNextPos](EventNextPos.md). The window direction is set by [EventBegPos](EventBegPos.md) and [EventEndPos](EventEndPos.md) (see [EventEndPos](EventEndPos.md)); use a positive `EventGap` for a window running in the positive direction. The grid of event positions is therefore `EventBegPos`, `EventBegPos + EventGap`, `EventBegPos + 2·EventGap`, …, continuing while it stays within `EventEndPos` (or indefinitely when [EventAlwaysOn](EventAlwaysOn.md) = 1).

The maximum sustainable event rate is bounded by `EventGap` divided by the axis velocity: as that interval approaches the time needed to emit one pulse of width [EventPulseWid](EventPulseWid.md), pulses begin to merge.

## Examples

```text
AEventGap=2000       ; generate an event every 2000 user units
AEventGap           ; query the configured gap
```

## See also

- [EventType](EventType.md) — selects the by-gap mode
- [EventBegPos](EventBegPos.md) — position of the first event
- [EventEndPos](EventEndPos.md) — last position for which events are generated
- [EventNextPos](EventNextPos.md) — next compare position (previous plus EventGap)
- [EventAlwaysOn](EventAlwaysOn.md) — continuous by-gap generation
- [EventPulseWid](EventPulseWid.md) — pulse width; large values can overlap at small gaps
