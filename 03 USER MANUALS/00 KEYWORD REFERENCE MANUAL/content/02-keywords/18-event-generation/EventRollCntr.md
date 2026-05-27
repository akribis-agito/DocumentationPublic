---
keyword: EventRollCntr
summary: Position span after which the event position counter wraps around (rollover threshold).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 738
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
# EventRollCntr

Position span after which the event position counter wraps around (rollover threshold).

## Overview

`EventRollCntr` sets the rollover threshold for the event-generation mechanism, defining the position span, in user units, after which the event position counter wraps around. It is used with [EventRollOff](EventRollOff.md), which shifts the event grid after each rollover, to support cyclic or rotary applications. It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
EventRollCntr=360000    ; wrap the event counter every 360000 user units
EventRollCntr?          ; query the current rollover threshold
```

## See also

- [EventRollOff](EventRollOff.md) — offset applied on rollover
- [EventSelect](EventSelect.md) — selects the event-generator mode
- [EventTable](EventTable.md) — table of event positions
