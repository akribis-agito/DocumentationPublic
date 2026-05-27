---
keyword: EventSelect
summary: Chooses the operating mode of the event output generator.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 317
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
  - 7
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventSelect

Chooses the operating mode of the event output generator.

## Overview

`EventSelect` chooses the operating mode of the event output generator, such as table-driven, periodic, or always-on operation. It sits above the per-move settings: [EventType](EventType.md) selects the position-trigger scheme (single, by-gap, or table), and [EventOn](EventOn.md) arms generation. It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
EventSelect=1       ; select the event-generator mode (default)
EventSelect?        ; query the current mode
```

## See also

- [EventAlwaysOn](EventAlwaysOn.md) — forces the output permanently active
- [EventType](EventType.md) — single / by-gap / table position-trigger scheme
- [EventTableSel](EventTableSel.md) — per-entry table selection
- [EventOn](EventOn.md) — arms event generation
