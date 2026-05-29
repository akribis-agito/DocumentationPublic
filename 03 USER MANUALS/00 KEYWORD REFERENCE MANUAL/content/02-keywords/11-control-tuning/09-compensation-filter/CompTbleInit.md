---
keyword: CompTbleInit
summary: "Position, in encoder counts, of the first point of the compensation table."
availability:
  standalone: []
  central-i:
  - v5
can_code: 838
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CompTbleInit

Position, in encoder counts, of the first point of the compensation table.

## Overview

`CompTbleInit` defines where the compensation table starts along the position axis. It is the position, in main-encoder counts, that corresponds to table index 1 in [CompFiltTble](CompFiltTble.md). Together with [CompTbleGap](CompTbleGap.md), which sets the spacing between points, it maps each table index to a physical position.

This keyword is available from v5 (central-i v5).

## How it works

Every control cycle the controller measures the position relative to this start point, divides by the point spacing from [CompTbleGap](CompTbleGap.md), and uses the result as a fractional index into [CompFiltTble](CompFiltTble.md). A measured position equal to `CompTbleInit` maps to the first table point; positions below `CompTbleInit` fall outside the table domain and no compensation is applied there.

Before the index is computed, the position is shifted by the per-unit contact-point correction from [CompTbleCrrct](CompTbleCrrct.md), so the effective start of the table tracks the contact point of the present unit.

The value is a signed 64-bit position and defaults to 0.

## Examples

Set the table to begin at position 10000 counts:

```
ACompTbleInit[1]=10000
```

Read back the configured start position:

```
ACompTbleInit[1]
```

## See also

- [CompTbleGap](CompTbleGap.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltTble](CompFiltTble.md)
- [CompTbleCrrct](CompTbleCrrct.md)
- [Pos](../../10-motion/01-kinematics-status/Pos.md)
