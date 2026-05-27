---
keyword: EventOn
summary: Arms event generation; loads the first compare position and is mutually exclusive with Lock.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 178
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventOn

Arms event generation; loads the first compare position and is mutually exclusive with Lock.

## Overview

`EventOn = 1` loads the first position (according to [EventType](EventType.md)) into the position comparator and turns event generation on. It should be set while the motor is at a position smaller than the first requested event to prevent unexpected behavior. Toggling `EventOn` also resets [EventCntr](EventCntr.md).

Event and Lock are mutually exclusive functions: setting `EventOn = 1` automatically forces `LockEN` to `0`.

## Examples

```text
AEventOn=1           ; arm event generation (set while below the first event position)
AEventOn=0           ; disable event generation
AEventOn            ; query the current state
```

## See also

- [EventType](EventType.md) — determines which position is loaded first
- [EventCntr](EventCntr.md) — reset when EventOn is toggled
- [EventAlwaysOn](EventAlwaysOn.md) — forces the output active regardless of position
