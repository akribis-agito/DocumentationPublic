---
keyword: EventRollOff
summary: Position offset applied to the event grid each time the event counter rolls over.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 739
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
overrides:
  central-i.v5:
    implemented: partial
---
# EventRollOff

Position offset applied to the event grid each time the event counter rolls over.

## Overview

`EventRollOff` sets the position offset, in user units, applied when the event counter rolls over, allowing the event grid to be shifted after each cycle. It works together with [EventRollCntr](EventRollCntr.md), which defines the rollover span. It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
AEventRollOff=100    ; shift the event grid by 100 user units on each rollover
AEventRollOff       ; query the current offset
```

## See also

- [EventRollCntr](EventRollCntr.md) — rollover position span
- [EventSelect](EventSelect.md) — selects the event-generator mode
- [EventTable](EventTable.md) — table of event positions
