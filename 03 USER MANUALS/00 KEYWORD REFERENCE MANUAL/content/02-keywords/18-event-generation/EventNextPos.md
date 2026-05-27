---
keyword: EventNextPos
summary: Read-only position at which the next event pulse will be generated.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 319
attributes:
  access: ro
  scope: axis
  flash: false
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
# EventNextPos

Read-only position at which the next event pulse will be generated.

## Overview

`EventNextPos` is a read-only status variable that reports the position, in user units, at which the next event output pulse will be generated. Use it to monitor where the next event is expected and to confirm the generator is advancing through the configured positions. It is an axis-related status variable and is not saved to flash.

## How it works

When [EventOn](EventOn.md) is armed, `EventNextPos` is set to the first compare position for the selected [EventType](EventType.md). After each pulse fires, the controller advances it to the next compare point:

| EventType | Value of EventNextPos |
|-----------|-----------------------|
| Single (0) | [EventBegPos](EventBegPos.md) (only one event). |
| By gap (1) | The most recent compare position plus [EventGap](EventGap.md), until [EventEndPos](EventEndPos.md) is passed. |
| By table (2, 3) | The next position from [EventTable](EventTable.md) (or [EventTableCor](EventTableCor.md) when the corrected table is selected). |

Once generation stops (single event done, by-gap window passed, or table exhausted), `EventNextPos` retains the last value until the engine is re-armed.

## Examples

```text
AEventNextPos       ; read the position of the next pending event
```

## See also

- [EventType](EventType.md) — determines how the next position is computed
- [EventGap](EventGap.md) — increment applied in by-gap mode
- [EventTable](EventTable.md) / [EventTableCor](EventTableCor.md) — position tables (table modes)
- [EventCntr](EventCntr.md) — count of events generated so far
