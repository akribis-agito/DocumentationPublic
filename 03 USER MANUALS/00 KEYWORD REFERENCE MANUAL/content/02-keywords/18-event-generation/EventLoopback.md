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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# EventLoopback

Read-only state of the event output as seen by the controller's input circuitry (hardware loopback).

## Overview

`EventLoopback` is a read-only status variable that reports whether event generation is currently in progress for the axis. Use it to confirm that the event output is active when expected. It is an axis-related status variable and is not saved to flash.

This status is maintained only on Central-i products, where it is driven from an "events in progress" indication reported back by the remote drive each control cycle. On standalone products the firmware does not update this variable, so it stays at `0`.

## How it works

| Value | Meaning |
|-------|---------|
| 0 | No event generation in progress. |
| 1 | Event generation is in progress for the axis. |

On Central-i products the controller refreshes this status each control cycle from the indication reported by the remote drive. Because the value tracks the drive's in-progress indication rather than each individual pulse edge, a single very short pulse may not always be observed as a `1`; use [EventCntr](EventCntr.md) to confirm how many pulses were produced. `EventLoopback` is most useful for confirming a continuously asserted or long-duration output.

## Examples

```text
AEventLoopback      ; read whether event generation is in progress (0 or 1)
```

## See also

- [EventOn](EventOn.md) — enables position-triggered output
- [EventCntr](EventCntr.md) — counts pulses; use it to verify short events
- [EventAlwaysOn](EventAlwaysOn.md) — continuous by-gap generation
- [EventSelect](EventSelect.md) — selects which output line a pulse drives
