---
keyword: ProgEventGEn
summary: Global enable for servicing all user program events.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 526
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventGEn

Global enable for servicing all user program events.

## Overview

`ProgEventGEn` globally enables (`1`) or disables (`0`) the servicing of all user program events. Unlike [ProgEventEn](ProgEventEn.md), setting `ProgEventGEn` to `0` does not disable the *sensing* of events: events are still sensed and may become pending, to be serviced once servicing is re-enabled. Use it to suspend and resume event handling as a whole without losing pending triggers. It is a non-axis scalar parameter and is not saved to flash.

## Examples

```text
AProgEventGEn=0      ; suspend servicing of all events (events still sensed)
AProgEventGEn=1      ; resume servicing; pending events are then handled
```

## See also

- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventStat](ProgEventStat.md) — per-event state
- [ProgEventOn](ProgEventOn.md) — event-handling enable
