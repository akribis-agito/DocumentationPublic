---
keyword: EventAlwaysOn
summary: Forces the event output permanently active, ignoring position and table conditions.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 619
attributes:
  access: rw
  scope: axis
  flash: true
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
# EventAlwaysOn

Forces the event output permanently active, ignoring position and table conditions.

## Overview

`EventAlwaysOn` overrides normal position-based event generation and holds the event output active regardless of the configured positions, ranges, or table. Use it to manually assert the event output (for example, to test wiring or hold a downstream device on) without changing the rest of the event configuration. Normal, position-triggered output is controlled instead by [EventOn](EventOn.md) together with [EventSelect](EventSelect.md) and [EventType](EventType.md). The current output level can be read back through [EventLoopback](EventLoopback.md).

It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
AEventAlwaysOn=1     ; force the event output permanently active
AEventAlwaysOn=0     ; return to normal position-based generation
AEventAlwaysOn      ; query the current setting
```

## See also

- [EventOn](EventOn.md) — enables normal position-triggered event generation
- [EventSelect](EventSelect.md) — selects the event-generator operating mode
- [EventLoopback](EventLoopback.md) — reads back the actual output state
