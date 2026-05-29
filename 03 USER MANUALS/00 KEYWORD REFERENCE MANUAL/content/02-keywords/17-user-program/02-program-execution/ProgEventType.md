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

`ProgEventType` defines the type of trigger condition for an event — for example a rising edge, equal, or not-equal comparison. It is one of the four parameters that define an event trigger, alongside the source parameter [ProgEventPar](ProgEventPar.md), the comparison value [ProgEventVal](ProgEventVal.md), and the bit mask [ProgEventMask](ProgEventMask.md); together they form a structure very similar to a data-recording trigger. The valid range is `1`–`8` (default `1`). It is a non-axis array parameter (indices `[1]`–`[5]`, one per event) and is saved to flash.

## How it works

Each control cycle, for an event that is armed and waiting, the controller takes the monitored parameter ([ProgEventPar](ProgEventPar.md)), applies the mask ([ProgEventMask](ProgEventMask.md)) to both it and the threshold, and evaluates the condition selected here against the (masked) threshold [ProgEventVal](ProgEventVal.md). In the table below *value* is the current masked source reading and *threshold* is the masked [ProgEventVal](ProgEventVal.md):

| Value | Condition | Fires when |
|---|---|---|
| 1 | Greater than | value &gt; threshold |
| 2 | Equal | value == threshold |
| 3 | Not equal | value != threshold |
| 4 | Less than | value &lt; threshold |
| 5 | Rising edge | value crosses up through threshold (previous &le; threshold, now &gt; threshold) |
| 6 | Falling edge | value crosses down through threshold (previous &ge; threshold, now &lt; threshold) |
| 7 | Manual | **not supported for program events** — the sensing loop does nothing for this type and the only writable value of [ProgEventStat](ProgEventStat.md) is `0`, so an event with type `7` can never become pending. The value is reserved for parallel numbering with the data-recorder trigger types. |
| 8 | Changed | value differs from the value captured when the event was armed |

Notes:

- **Edge types (5, 6)** compare the current reading with the previous cycle's reading, so they fire once per crossing rather than continuously while the level condition holds. The "changed" type (8) compares against the reading captured at the moment the event was armed.
- The comparison is performed in the monitored parameter's native data type (integer or floating point). The mask is applied to integer sources; floating-point sources are compared without a mask.

## Examples

```text
AProgEventType[1]=5  ; event 1 fires on a rising-edge crossing of ProgEventVal[1]
AProgEventType[1]=2  ; event 1 fires when the masked source equals ProgEventVal[1]
```

## See also

- [ProgEventPar](ProgEventPar.md) — parameter that triggers the event
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
