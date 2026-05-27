---
keyword: EventBegPos
summary: Position of the first generated event in single-event and by-gap modes.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`EventBegPos` is the position, in user units, of the first event that is generated in the single-event and by-gap event modes (see [EventType](EventType.md)). In by-gap mode it is the starting position from which subsequent events are spaced by [EventGap](EventGap.md) up to [EventEndPos](EventEndPos.md). For correct behavior, [EventOn](EventOn.md) should be set while the motor is at a position smaller than `EventBegPos`.

## Examples

```text
AEventBegPos=1000    ; first event at position 1000 (user units)
AEventBegPos        ; query the configured start position
```

## See also

- [EventType](EventType.md) — selects single-event vs. by-gap vs. table modes
- [EventGap](EventGap.md) — spacing between events in by-gap mode
- [EventEndPos](EventEndPos.md) — last position for which events are generated
- [EventOn](EventOn.md) — arms event generation
