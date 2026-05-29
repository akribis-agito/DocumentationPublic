---
keyword: EventEndPos
summary: Bounding position at which by-gap event generation stops.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 183
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
# EventEndPos

Bounding position at which by-gap event generation stops.

## Overview

`EventEndPos` is the bounding position, in user units, for which events are generated in the by-gap event mode (see [EventType](EventType.md)). It bounds the series of events that start at [EventBegPos](EventBegPos.md) and repeat every [EventGap](EventGap.md). `EventEndPos` does not have to coincide with a position where an event is actually generated. After this position is passed, no more events are produced and [EventOn](EventOn.md) must be toggled to restart generation.

## How it works

`EventEndPos` defines both the end of the by-gap window and, together with [EventBegPos](EventBegPos.md), the direction of the window:

- If `EventEndPos` is greater than `EventBegPos`, events run in the positive direction and stop once a compare position would exceed `EventEndPos`.
- If `EventEndPos` is less than `EventBegPos`, events run in the negative direction and stop once a compare position would fall below `EventEndPos`.

After each by-gap event fires, the controller advances the next compare point by [EventGap](EventGap.md) and tests it against `EventEndPos` in the watched direction; when the bound is passed it disarms generation ([EventOn](EventOn.md) returns to `0`). This end check is skipped when [EventAlwaysOn](EventAlwaysOn.md) = 1, which makes by-gap generation run continuously and ignore `EventEndPos`.

## Examples

```text
AEventType=1         ; event generation by gap
AEventBegPos=1000
AEventGap=2000
AEventEndPos=8000
AEventOn=1           ; set this while the axis is at a position smaller than EventBegPos
                    ; to prevent unexpected behavior
```

With the sequence above, the event output turns on for the duration set by [EventPulseWid](EventPulseWid.md) when passing positions 1000, 3000, 5000, and 7000. After passing position 8000 no more events are generated, and `EventOn` must be toggled to restart.

## See also

- [EventType](EventType.md) — selects the by-gap mode
- [EventBegPos](EventBegPos.md) — position of the first event
- [EventGap](EventGap.md) — spacing between events
- [EventAlwaysOn](EventAlwaysOn.md) — bypasses EventEndPos for continuous by-gap generation
- [EventOn](EventOn.md) — must be toggled to restart after EventEndPos is passed
