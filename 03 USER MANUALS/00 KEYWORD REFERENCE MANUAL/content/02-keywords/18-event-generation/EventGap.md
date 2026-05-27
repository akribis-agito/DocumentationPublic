---
keyword: EventGap
summary: Position spacing between successive events in by-gap mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

## Examples

```text
EventGap=2000       ; generate an event every 2000 user units
EventGap?           ; query the configured gap
```

## See also

- [EventType](EventType.md) — selects the by-gap mode
- [EventBegPos](EventBegPos.md) — position of the first event
- [EventEndPos](EventEndPos.md) — last position for which events are generated
- [EventPulseWid](EventPulseWid.md) — pulse width; large values can overlap at small gaps
