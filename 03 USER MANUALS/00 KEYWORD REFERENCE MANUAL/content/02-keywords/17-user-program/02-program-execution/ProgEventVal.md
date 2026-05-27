---
keyword: ProgEventVal
summary: Value used for an event's trigger detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ProgEventVal

Value used for an event's trigger detection.

## Overview

`ProgEventVal` defines the threshold value used for trigger detection of an event (indices `[1]`–`[5]`, one per event). It is compared against the monitored parameter — after both are masked by [ProgEventMask](ProgEventMask.md) — according to the condition selected by [ProgEventType](ProgEventType.md). It is one of the four parameters that define an event trigger, alongside the source parameter [ProgEventPar](ProgEventPar.md) and the bit mask [ProgEventMask](ProgEventMask.md). It is a non-axis array parameter and is saved to flash (default `0`).

## How it works

Enter `ProgEventVal` in the **same user units** as the monitored parameter selected by [ProgEventPar](ProgEventPar.md). When the trigger source is (re)assigned, the controller converts this threshold into the source parameter's internal (raw) units once, applying that parameter's user-unit scaling or scaling factor, so each cycle's comparison is fast. The mask from [ProgEventMask](ProgEventMask.md) is applied to the threshold (for integer sources) before it is compared, so only the masked bits participate. For the edge conditions ([ProgEventType](ProgEventType.md) `5`/`6`) the threshold is the level that the source must cross; for the "changed" condition (`8`) the threshold is not used, since the comparison is against the value captured when the event was armed.

## Examples

```text
AProgEventVal[1]=100 ; threshold of 100 (in the monitored parameter's user units) for event 1
```

## See also

- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
