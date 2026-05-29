---
keyword: CompFiltTble
summary: "Compensation table holding the expected force at each evenly spaced table position."
availability:
  standalone: []
  central-i:
  - v5
can_code: 836
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 64
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# CompFiltTble

Compensation table holding the expected force at each evenly spaced table position.

## Overview

`CompFiltTble` is the data array of the compensation filter. Each element holds the force that the controller should expect when the axis is at the corresponding table position. When the filter is enabled with [CompFiltOn](CompFiltOn.md), this table is read every control cycle to predict a force from the current position, which the complementary filter then blends with the measured force (see [00-overview](00-overview.md)).

This keyword is available from v5 (central-i v5).

## How it works

The table is a one-dimensional array indexed by table point. The positions of the points are not stored in the table; they are defined separately by [CompTbleInit](CompTbleInit.md) (the position of the first point) and [CompTbleGap](CompTbleGap.md) (the position spacing between points). Element index 1 corresponds to the first point, index 2 to the next point one gap further along, and so on.

During operation the controller converts the current position into a fractional table index, then linearly interpolates between the two neighbouring table entries to obtain the expected force. Only entries from index 1 up to the index set by [CompTbleEnd](CompTbleEnd.md) take part in the lookup.

The array is 1-indexed: index 1 is the first usable point and the highest usable index is 63. (Index 0 is reserved internally and is not accessible.)

| Index | Element |
|----|----|
| 1 | Expected force at the first table position |
| 2 | Expected force one gap further along |
| ... | ... |
| 63 | Expected force at the last available table position |

## Examples

Write the expected force into the first three table points:

```
ACompFiltTble[1]=0.0
ACompFiltTble[2]=1.5
ACompFiltTble[3]=3.1
```

Read back the second table point:

```
ACompFiltTble[2]
```

## See also

- [CompTbleInit](CompTbleInit.md)
- [CompTbleGap](CompTbleGap.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltOn](CompFiltOn.md)
- [00-overview](00-overview.md)
