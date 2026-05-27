---
keyword: ProgEventPar
summary: Selects (by complex CAN code) the controller parameter that triggers an event.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 520
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
# ProgEventPar

Selects (by complex CAN code) the controller parameter that triggers an event.

## Overview

`ProgEventPar` defines, using a complex CAN code, which controller parameter is monitored to trigger a given event. If `ProgEventPar[EventNumber]` is set to `0` (or to a non-valid complex CAN code), the event is not sensed and not handled. Together with [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), and [ProgEventMask](ProgEventMask.md), it forms the four-part trigger definition for an event — a structure very similar to a data-recording trigger. It is a non-axis array parameter (one element per event) and is saved to flash.

## Examples

```text
ProgEventPar[1]=<CAN code of monitored parameter>   ; choose the trigger source for event 1
```

## See also

- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
