---
keyword: EventRollOff
summary: Position offset applied to the event grid each time the event counter rolls over.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 739
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: '0'
overrides:
  central-i.v4:
    implemented: final
  central-i.v5:
    implemented: partial
---
# EventRollOff

Position offset applied to the event grid each time the event counter rolls over.

## Overview

`EventRollOff` sets the position offset, in user units, applied when the event counter rolls over, allowing the event grid to be shifted after each cycle. It works together with [EventRollCntr](EventRollCntr.md), which defines the rollover span. It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

`EventRollOff` doubles as the enable for the rollover feature. The controller reads it together with [EventRollCntr](EventRollCntr.md) when events are armed with [EventOn](EventOn.md) = 1, for the single-event and by-gap schemes ([EventType](EventType.md) = 0 and 1):

- `EventRollOff` = 0 — rollover is disabled. The controller also forces [EventRollCntr](EventRollCntr.md) to 0, and the comparator runs without wrapping.
- `EventRollOff` non-zero — rollover is enabled. Each time the comparator's position reference reaches the [EventRollCntr](EventRollCntr.md) span it wraps, and the event grid is shifted by `EventRollOff` so the next cycle's pulses fall at the intended positions.

Set both values before arming; changing them while events are running does not retroactively re-arm the rollover unit.

## Examples

```text
AEventRollCntr=360000    ; rollover span
AEventRollOff=100        ; shift the event grid by 100 user units on each rollover
AEventRollOff            ; query the current offset
```

## Changes between versions

On central-i v5 the rollover feature is only partially implemented. Use rollover-based cyclic event generation on v4; on v5 verify the behavior for your configuration before relying on it.

## See also

- [EventRollCntr](EventRollCntr.md) — rollover position span
- [EventSelect](EventSelect.md) — selects which output line the event pulse drives
- [EventTable](EventTable.md) — table of event positions
