---
keyword: CompTbleEnd
summary: Highest compensation-table index that is in use, bounding the table domain.
availability:
  standalone: []
  central-i:
  - v5
can_code: 839
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
  - 2
  - 63
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# CompTbleEnd

Highest compensation-table index that is in use, bounding the table domain.

## Overview

The compensation table in [CompFiltTble](CompFiltTble.md) can hold up to 63 points, but a given setup may only populate some of them. `CompTbleEnd` tells the controller the last table index that is in use, so positions beyond the populated region are treated as outside the table domain and receive no compensation.

This keyword is available from v5 (central-i v5).

## How it works

Each control cycle the controller turns the current position into a fractional table index. Compensation is applied only while that index is at least 1 and less than `CompTbleEnd`. Because the lookup interpolates between the point at the computed index and the next point one position higher, the point stored at index `CompTbleEnd` serves as the upper end-point of the last interpolation segment; the active position domain therefore ends at the position of that point.

The value ranges from 2 to 63 and defaults to 2. With the default of 2, only the segment between table points 1 and 2 is active.

## Examples

Use table points 1 through 10 (nine interpolation segments):

```
ACompTbleEnd[1]=10
```

Read back the configured end index:

```
ACompTbleEnd[1]
```

## See also

- [CompTbleInit](CompTbleInit.md)
- [CompTbleGap](CompTbleGap.md)
- [CompFiltTble](CompFiltTble.md)
- [CompFiltOn](CompFiltOn.md)
