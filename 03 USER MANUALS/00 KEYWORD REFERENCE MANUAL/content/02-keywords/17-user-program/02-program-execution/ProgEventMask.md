---
keyword: ProgEventMask
summary: Bitwise mask applied to an event's trigger parameter and trigger value.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ProgEventMask

Bitwise mask applied to an event's trigger parameter and trigger value.

## Overview

`ProgEventMask` defines a bitwise mask that is applied to the monitored event parameter ([ProgEventPar](ProgEventPar.md)) before comparison (indices `[1]`–`[5]`, one per event). The same mask is also applied to the trigger threshold ([ProgEventVal](ProgEventVal.md)), so only the masked bits participate in the condition selected by [ProgEventType](ProgEventType.md). This makes it possible to trigger an event on specific status bits rather than a whole word. It is a non-axis array parameter and is saved to flash.

## How it works

Each control cycle, for an integer trigger source, the controller computes `(source AND mask)` and compares it against `(threshold AND mask)`. Only bits set to `1` in the mask take part:

- To watch a single status bit, set just that bit in the mask and set [ProgEventVal](ProgEventVal.md) to the desired masked value (for example, mask `0x0001` with value `0x0001` fires when bit 0 is set, using the "equal" condition).
- For the edge conditions ([ProgEventType](ProgEventType.md) `5`/`6`), the masked source value is what is tracked across cycles, so an edge is detected on the masked bits only.

The mask is meaningful for integer trigger sources. A floating-point trigger source is compared directly, without masking. The value is held as a wide bit pattern, so masks of full word width are supported (see the version note below for width differences).

## Examples

```text
AProgEventMask[1]=0x0001   ; only bit 0 of the trigger parameter is tested for event 1
AProgEventMask[1]=0xFFFFFFFF ; test the whole 32-bit word (no masking effect)
```

## See also

- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
