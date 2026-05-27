---
keyword: EventLoopback
summary: Read-only state of the event output as seen by the controller's input circuitry (hardware loopback).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 565
attributes:
  access: ro
  scope: axis
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
overrides:
  central-i.v5:
    can_code: 372
---
# EventLoopback

Read-only state of the event output as seen by the controller's input circuitry (hardware loopback).

## Overview

`EventLoopback` is a read-only status variable that reflects the current state of the event output as seen by the controller's input circuitry, providing a hardware loopback confirmation. Use it to verify that the output is actually active when expected. It is an axis-related status variable and is not saved to flash.

## How it works

| Value | Meaning |
|-------|---------|
| 0 | Event output is idle (no pulse currently active). |
| 1 | Event output is active (a pulse is in progress). |

The controller reads the looped-back output state each control cycle, so `EventLoopback` follows the actual hardware line rather than the commanded value. Because event pulses can be very short relative to the control cycle, a single brief pulse may not be observed as a `1` on every read; use [EventCntr](EventCntr.md) to confirm how many pulses were produced. `EventLoopback` is most useful for confirming a continuously asserted or long-duration output.

## Examples

```text
AEventLoopback      ; read the looped-back output state (0 or 1)
```

## See also

- [EventOn](EventOn.md) — enables position-triggered output
- [EventCntr](EventCntr.md) — counts pulses; use it to verify short events
- [EventAlwaysOn](EventAlwaysOn.md) — continuous by-gap generation
- [EventSelect](EventSelect.md) — selects which output line a pulse drives
