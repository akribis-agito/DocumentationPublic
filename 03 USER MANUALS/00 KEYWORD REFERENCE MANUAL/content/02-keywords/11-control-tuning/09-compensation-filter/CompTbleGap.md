---
keyword: CompTbleGap
summary: "Position spacing, in encoder counts, between adjacent compensation-table points."
availability:
  standalone: []
  central-i:
  - v5
can_code: 837
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# CompTbleGap

Position spacing, in encoder counts, between adjacent compensation-table points.

## Overview

The compensation table points are evenly spaced along the position axis. `CompTbleGap` sets that spacing, in main-encoder counts, between one table point and the next. Together with [CompTbleInit](CompTbleInit.md), which sets the position of the first point, it defines the position of every point in [CompFiltTble](CompFiltTble.md).

This keyword is available from v5 (central-i v5).

## How it works

To find the table position for the current axis position, the controller takes the distance from the start point set by [CompTbleInit](CompTbleInit.md) and divides it by `CompTbleGap`. The integer part selects the table segment and the fractional part is used to linearly interpolate between the two neighbouring entries of [CompFiltTble](CompFiltTble.md).

A smaller gap places points closer together and gives finer position resolution over a shorter span; a larger gap covers a wider span with the same number of points. The reciprocal of the gap is precomputed when the value changes, so updates take effect without disabling the filter.

The value ranges from 1 to 2147483647 and defaults to 1.

## Examples

Space the table points 500 counts apart:

```
ACompTbleGap[1]=500
```

Read back the configured spacing:

```
ACompTbleGap[1]
```

## See also

- [CompTbleInit](CompTbleInit.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltTble](CompFiltTble.md)
- [00-overview](00-overview.md)
