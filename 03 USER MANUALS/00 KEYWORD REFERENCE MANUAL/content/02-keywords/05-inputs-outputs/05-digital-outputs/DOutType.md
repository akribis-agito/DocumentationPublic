---
keyword: DOutType
summary: Per-output sink/source mode for single-ended digital outputs (bitfield).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 209
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutType

Per-output sink/source mode for single-ended digital outputs (bitfield).

## Overview

`DOutType` configures each digital output for sink or source mode, as a bitfield (0-based: bit 0 = output 1). Each bit: `0` = sink, `1` = source. It applies only to single-ended outputs that have configurable sink/source type — see the individual product manual.

| Bit value | Mode |
|-----------|------|
| 0 | Sink |
| 1 | Source |

## Examples

`DOutType = 9` (binary `…1001`) puts outputs 1 and 4 in source mode; the rest stay sink.

## See also

- [DOutPort](DOutPort.md) — output states
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md) — output function assignment
