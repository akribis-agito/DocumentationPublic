---
keyword: EventCntr
summary: Counts events generated since the last EventOn; resettable by the user.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 186
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventCntr

Counts events generated since the last EventOn; resettable by the user.

## Overview

`EventCntr` counts the events that have occurred since the last time [EventOn](EventOn.md) was set. Toggling `EventOn` resets the counter; the user may also reset it directly. Use it to confirm how many event pulses were produced during a move or to verify expected event coverage against the configured table or range.

## Examples

```text
AEventCntr          ; read the number of events since the last EventOn
AEventCntr=0         ; reset the counter
```

## See also

- [EventOn](EventOn.md) — toggling it resets this counter
- [EventNextPos](EventNextPos.md) — position of the next event to be generated
