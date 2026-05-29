---
keyword: CompTbleCrrct
summary: Per-unit contact-point correction that shifts the compensation table along the position axis.
availability:
  standalone: []
  central-i:
  - v5
can_code: 840
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CompTbleCrrct

Per-unit contact-point correction that shifts the compensation table along the position axis.

## Overview

A compensation table is usually characterised once on a reference unit, but individual physical units can make contact at slightly different positions. `CompTbleCrrct` lets the controller shift the whole table so that it lines up with the contact point of the present unit, without re-measuring the force values in [CompFiltTble](CompFiltTble.md).

This keyword is available from v5 (central-i v5).

## How it works

The keyword holds two contact-point positions, in main-encoder counts. Each control cycle the controller adds the difference between them to the measured position before the table lookup, which is equivalent to shifting the table by the same amount. The shift applied is the contact point recorded when the table was created minus the actual contact point of this unit.

The array is 1-indexed: index 1 and index 2 are the usable elements (index 0 is reserved internally and is not accessible).

| Index | Element |
|----|----|
| 1 | Contact-point position recorded when the table was created |
| 2 | Actual contact-point position for the present unit |

Both elements default to 0, which produces no shift.

## Examples

Record the reference contact point and the present unit's contact point:

```
ACompTbleCrrct[1]=10000
ACompTbleCrrct[2]=10120
```

Read back the present unit's contact point:

```
ACompTbleCrrct[2]
```

## See also

- [CompTbleInit](CompTbleInit.md)
- [CompFiltTble](CompFiltTble.md)
- [CompFiltOn](CompFiltOn.md)
- [Pos](../../10-motion/01-kinematics-status/Pos.md)
