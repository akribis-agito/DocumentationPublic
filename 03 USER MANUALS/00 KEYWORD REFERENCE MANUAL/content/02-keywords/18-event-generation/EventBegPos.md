---
keyword: EventBegPos
summary: Position of the first generated event in single-event and by-gap modes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 181
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
# EventBegPos

Position of the first generated event in single-event and by-gap modes.

## Overview

`EventBegPos` is the position, in user units, of the first event that is generated in the single-event and by-gap event modes (see [EventType](EventType.md)). In by-gap mode it is the starting position from which subsequent events are spaced by [EventGap](EventGap.md) up to [EventEndPos](EventEndPos.md). For correct behavior, [EventOn](EventOn.md) should be set while the axis is at a position before `EventBegPos` in the direction of travel.

## How it works

`EventBegPos` is loaded as the first compare position when [EventOn](EventOn.md) is armed, and is reported in [EventNextPos](EventNextPos.md). It also sets the expected travel direction the generator watches for:

- In **single-event** mode the direction is taken from the current position relative to `EventBegPos`: if the axis is below `EventBegPos` the engine waits for an upward crossing, otherwise a downward crossing.
- In **by-gap** mode the direction is taken from [EventEndPos](EventEndPos.md) relative to `EventBegPos`: if `EventEndPos` is greater than `EventBegPos` the window runs in the positive direction, otherwise in the negative direction. This allows the by-gap window to be defined for motion in either direction.

Arming while the axis has already passed `EventBegPos` in the watched direction may cause the first event to be missed or fired immediately, which is why arming should be done before reaching `EventBegPos`.

## Examples

```text
AEventBegPos=1000    ; first event at position 1000 (user units)
AEventBegPos        ; query the configured start position
```

## See also

- [EventType](EventType.md) — selects single-event vs. by-gap vs. table modes
- [EventGap](EventGap.md) — spacing between events in by-gap mode
- [EventEndPos](EventEndPos.md) — last position for which events are generated; its sign vs. EventBegPos sets the by-gap direction
- [EventNextPos](EventNextPos.md) — reports the loaded first compare position
- [EventOn](EventOn.md) — arms event generation
