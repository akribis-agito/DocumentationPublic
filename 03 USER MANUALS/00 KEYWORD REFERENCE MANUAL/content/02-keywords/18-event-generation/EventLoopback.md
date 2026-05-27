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

`EventLoopback` is a read-only status variable that reflects the current state of the event output signal as seen by the controller's input circuitry, providing a hardware loopback confirmation. Use it to verify that the event output is actually toggling as commanded by [EventOn](EventOn.md) or forced by [EventAlwaysOn](EventAlwaysOn.md). It is an axis-related status variable and is not saved to flash.

## Examples

```text
AEventLoopback      ; read the looped-back output state (0 or 1)
```

## See also

- [EventAlwaysOn](EventAlwaysOn.md) — forces the output active
- [EventOn](EventOn.md) — enables position-triggered output
- [EventSelect](EventSelect.md) — selects the event-generator mode
