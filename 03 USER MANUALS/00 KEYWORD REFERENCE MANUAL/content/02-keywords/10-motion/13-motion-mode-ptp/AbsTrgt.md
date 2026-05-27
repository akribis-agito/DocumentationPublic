---
keyword: AbsTrgt
summary: Absolute target position (user units) for the next point-to-point move.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 134
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
# AbsTrgt

Absolute target position (user units) for the next point-to-point move.

## Overview

`AbsTrgt` sets the absolute target position, in user units, for the next point-to-point (PTP) move. When a [Begin](../04-motion-command/Begin.md) command is issued in absolute PTP mode, the axis moves to this position. It is the absolute counterpart of [RelTrgt](RelTrgt.md), which specifies a relative distance instead. It is not saved to flash and can be changed at any time.

## Examples

```text
AAbsTrgt=100000      ; move to absolute position 100000 (user units)
```

## See also

- [RelTrgt](RelTrgt.md) — relative target distance
- [Targets](Targets.md) — multi-target sequence
- [Begin](../04-motion-command/Begin.md) — start the PTP move
