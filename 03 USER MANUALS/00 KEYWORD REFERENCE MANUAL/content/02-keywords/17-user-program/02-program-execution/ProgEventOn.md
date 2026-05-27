---
keyword: ProgEventOn
summary: Activates or disables handling of user program events.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 527
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
# ProgEventOn

Activates or disables handling of user program events.

## Overview

`ProgEventOn` activates (`1`) or disables (`0`) the handling of user program events. When disabled, all pending events are cleared and events are not handled or processed at all — this also stops the sensing of events. Whereas [ProgEventGEn](ProgEventGEn.md) suspends servicing while still sensing events, disabling `ProgEventOn` stops sensing entirely; [ProgEventEn](ProgEventEn.md) provides the same on/off control per individual event. It is a non-axis scalar parameter and is not saved to flash.

## Examples

```text
AProgEventOn=1       ; enable event handling
AProgEventOn=0       ; disable handling and clear all pending events
```

## See also

- [ProgEventGEn](ProgEventGEn.md) — global enable that keeps sensing active
- [ProgEventEn](ProgEventEn.md) — per-event enable/disable
- [ProgEventStat](ProgEventStat.md) — per-event state
