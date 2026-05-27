---
keyword: ProgEventType
summary: Defines the trigger type (edge, equal, not equal, …) for an event.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 522
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
  - 1
  - 8
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventType

Defines the trigger type (edge, equal, not equal, …) for an event.

## Overview

`ProgEventType` defines the type of trigger condition for an event — for example a rising edge, equal, or not equal comparison. It is one of the four parameters that define an event trigger, alongside the source parameter [ProgEventPar](ProgEventPar.md), the comparison value [ProgEventVal](ProgEventVal.md), and the bit mask [ProgEventMask](ProgEventMask.md); together they form a structure very similar to a data-recording trigger. The valid range is `1`–`8`. It is a non-axis array parameter (one element per event) and is saved to flash.

> **Documentation pending:** The mapping of each type code (1–8) to its specific condition is defined in the User Program Language Manual and is not reproduced here.

## Examples

```text
AProgEventType[1]=1  ; set the trigger type for event 1
```

## See also

- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
