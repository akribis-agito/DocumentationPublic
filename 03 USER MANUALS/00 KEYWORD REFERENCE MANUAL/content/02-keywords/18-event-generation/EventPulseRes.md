---
keyword: EventPulseRes
summary: Sets the position resolution of the event pulse generator (minimum spacing between events).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 517
attributes:
  access: rw
  scope: axis
  flash: true
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
# EventPulseRes

Sets the position resolution of the event pulse generator (minimum spacing between events).

## Overview

`EventPulseRes` sets the position resolution of the event output pulse generator, defining the minimum spacing between events in encoder counts. It works together with [EventPulseWid](EventPulseWid.md), which sets how long each pulse stays active. It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
AEventPulseRes=1     ; set the pulse-generator resolution
AEventPulseRes      ; query the current setting
```

## See also

- [EventPulseWid](EventPulseWid.md) — duration of each event pulse
- [EventSelect](EventSelect.md) — selects the event-generator mode
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
