---
keyword: RelTrgt
summary: Relative target distance (user units) for the next point-to-point move.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 135
attributes:
  access: rw
  scope: axis
  flash: false
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
overrides: {}
---
# RelTrgt

Relative target distance (user units) for the next point-to-point move.

## Overview

`RelTrgt` sets the relative target distance, in user units, for the next point-to-point (PTP) move. When a [Begin](../04-motion-command/Begin.md) command is issued in relative PTP mode, the axis moves by this distance from its current position. It is the relative counterpart of [AbsTrgt](AbsTrgt.md), which specifies an absolute position instead. It is not saved to flash and can be changed at any time.

## Examples

```text
ARelTrgt=5000        ; move 5000 user units from the current position
ARelTrgt=-5000       ; move 5000 user units in the negative direction
```

## See also

- [AbsTrgt](AbsTrgt.md) — absolute target position
- [Targets](Targets.md) — multi-target sequence
- [Begin](../04-motion-command/Begin.md) — start the PTP move
