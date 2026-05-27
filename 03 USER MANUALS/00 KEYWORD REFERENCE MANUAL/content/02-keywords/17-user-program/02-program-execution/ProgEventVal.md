---
keyword: ProgEventVal
summary: Value used for an event's trigger detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 523
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 6
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
# ProgEventVal

Value used for an event's trigger detection.

## Overview

`ProgEventVal` defines the value used for trigger detection of an event. It is compared against the (optionally masked) monitored parameter according to the condition selected by [ProgEventType](ProgEventType.md). It is one of the four parameters that define an event trigger, alongside the source parameter [ProgEventPar](ProgEventPar.md) and the bit mask [ProgEventMask](ProgEventMask.md). It is a non-axis array parameter (one element per event) and is saved to flash.

## Examples

```text
AProgEventVal[1]=100 ; trigger event 1 when the comparison against 100 is satisfied
```

## See also

- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
