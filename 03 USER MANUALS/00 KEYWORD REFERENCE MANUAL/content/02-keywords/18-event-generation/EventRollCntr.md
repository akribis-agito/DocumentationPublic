---
keyword: EventRollCntr
summary: Position span after which the event position counter wraps around (rollover threshold).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 738
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
  implemented: final
overrides:
  central-i.v5:
    implemented: partial
---
# EventRollCntr

Position span after which the event position counter wraps around (rollover threshold).

## Overview

`EventRollCntr` sets the rollover threshold for the event-generation mechanism, defining the position span, in user units, after which the event position counter wraps around. It is used with [EventRollOff](EventRollOff.md), which shifts the event grid after each rollover, to support cyclic or rotary applications. It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

In a rotary or repetitive application the comparator can keep firing indefinitely by wrapping its internal position reference instead of running off the end of the table or range. `EventRollCntr` sets the span after which that wrap occurs, and [EventRollOff](EventRollOff.md) sets how far the event grid is shifted on each wrap so the next cycle's events land at the intended positions.

These settings are read and applied to the rollover unit when events are armed with [EventOn](EventOn.md) = 1, for the single-event and by-gap schemes ([EventType](EventType.md) = 0 and 1). If [EventRollOff](EventRollOff.md) is 0, rollover is disabled: the controller forces `EventRollCntr` to 0 and the comparator runs without wrapping. Set both `EventRollCntr` (the span) and a non-zero [EventRollOff](EventRollOff.md) before arming to enable the cyclic behavior.

## Examples

```text
AEventRollOff=0          ; shift per cycle; non-zero enables rollover
AEventRollCntr=360000    ; wrap the event counter every 360000 user units
AEventRollCntr           ; query the current rollover threshold
```

## Changes between versions

On central-i v5 the rollover feature is only partially implemented. Use rollover-based cyclic event generation on v4; on v5 verify the behavior for your configuration before relying on it.

## See also

- [EventRollOff](EventRollOff.md) — offset applied on rollover
- [EventSelect](EventSelect.md) — selects which output line the event pulse drives
- [EventTable](EventTable.md) — table of event positions
