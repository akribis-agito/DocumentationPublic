---
keyword: ProgEventPar
summary: Selects (by complex CAN code) the controller parameter that triggers an event.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ProgEventPar` defines, using a complex CAN code, which controller parameter is monitored to trigger a given event (indices `[1]`–`[5]`, one per event). If `ProgEventPar[EventNumber]` is set to `0` — or to a complex code that does not resolve to a valid, readable parameter — the event is not sensed and not handled. Together with [ProgEventType](ProgEventType.md), [ProgEventVal](ProgEventVal.md), and [ProgEventMask](ProgEventMask.md), it forms the four-part trigger definition for an event — a structure very similar to a data-recording trigger. It is a non-axis array parameter and is saved to flash (default `0`).

## How it works

Each element holds a **complex CAN code** that names the exact parameter to monitor, not just a bare CAN code. The complex value packs three fields:

| Bits | Field |
|---|---|
| 0–9 | CAN code of the parameter |
| 10–14 | Axis number (0 = A; ignored for non-axis parameters) |
| 16–31 | Array index (for array parameters; use 0 for scalars) |

For a scalar parameter on axis A the complex code is just the plain CAN code. When you write `ProgEventPar`, the controller validates the selection: the CAN code must exist, must be a parameter (not a command), and the axis and array index must be in range. If validation fails, that event's trigger is pointed at an always-zero internal source so it can never fire (the event is effectively disabled until you correct the selection).

When the selection is valid, the controller resolves the source and, at the same time, converts the trigger threshold [ProgEventVal](ProgEventVal.md) into the source parameter's internal (raw) units — applying that parameter's user-unit scaling or scaling factor as appropriate — so the comparison at trigger time is fast and unit-correct. For this reason, set [ProgEventVal](ProgEventVal.md) in the same user units as the monitored parameter.

## Examples

```text
AProgEventPar[1]=<complex CAN code of monitored parameter>   ; choose the trigger source for event 1
AProgEventPar[1]=0   ; disable the trigger source for event 1
```

## See also

- [ProgEventType](ProgEventType.md) — trigger type (edge, equal, not equal, …)
- [ProgEventVal](ProgEventVal.md) — value used for trigger detection
- [ProgEventMask](ProgEventMask.md) — bitwise mask applied to the trigger
