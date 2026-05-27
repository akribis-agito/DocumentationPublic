---
keyword: ProgEventMask
summary: Bitwise mask applied to an event's trigger parameter and trigger value.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 521
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
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventMask

Bitwise mask applied to an event's trigger parameter and trigger value.

## Overview

`ProgEventMask` defines a bitwise mask that is applied to the user-defined event trigger parameter ([ProgEventPar](ProgEventPar.md)) before comparison. The same mask is also applied to the trigger value ([ProgEventVal](ProgEventVal.md)), so only the masked bits participate in the trigger condition selected by [ProgEventType](ProgEventType.md). This makes it possible to trigger an event on specific status bits rather than a whole word. It is a non-axis array parameter (one element per event) and is saved to flash.

## Examples

```text
ProgEventMask[1]=0x0001   ; only bit 0 of the trigger parameter is tested for event 1
```

## See also

- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
