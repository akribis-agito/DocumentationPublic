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

`EventNextPos` is a read-only status variable that reports the position, in user units, at which the next event output pulse will be generated, based on the current event table and selection. Use it to monitor where the next event is expected and to confirm the generator is advancing through the configured positions. It is an axis-related status variable and is not saved to flash.

## Examples

```text
AEventNextPos       ; read the position of the next pending event
```

## See also

- [EventTable](EventTable.md) — table of event positions
- [EventTableSel](EventTableSel.md) — per-entry selection within the table
- [EventCntr](EventCntr.md) — count of events generated so far
