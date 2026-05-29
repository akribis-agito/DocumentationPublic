---
keyword: CompFiltOn
summary: Enables the compensation filter that blends measured force with a position-predicted force.
availability:
  standalone: []
  central-i:
  - v5
can_code: 834
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
# CompFiltOn

Enables the compensation filter that blends measured force with a position-predicted force.

## Overview

`CompFiltOn` turns the compensation filter on or off for the axis. When enabled, the controller no longer uses the raw analog force-feedback value directly. Instead it predicts an expected force from the current position using the compensation table, then merges the measured force and the predicted force with a complementary filter (see [00-overview](00-overview.md)). The result becomes the force value used by force control.

This keyword is available from v5 (central-i v5).

## How it works

| Value | Meaning |
|----|----|
| 0 | Compensation filter off; force control uses the measured force directly (default) |
| 1 | Compensation filter on; measured force and table-predicted force are blended |

When the keyword is set to 1, the filter only acts while the axis position lies inside the table domain defined by [CompTbleInit](CompTbleInit.md), [CompTbleGap](CompTbleGap.md) and [CompTbleEnd](CompTbleEnd.md). Outside that range the measured force is used unchanged, and the filter's internal state is reset so that the next entry into the table range starts cleanly.

The cut-off of the complementary filter is set by [CompFiltFreq](CompFiltFreq.md), the expected-force values by [CompFiltTble](CompFiltTble.md), and the per-unit position offset by [CompTbleCrrct](CompTbleCrrct.md).

## Examples

Enable the compensation filter on an axis:

```
ACompFiltOn[1]=1
```

Read back the current state:

```
ACompFiltOn[1]
```

Disable it again:

```
ACompFiltOn[1]=0
```

## See also

- [CompFiltFreq](CompFiltFreq.md)
- [CompFiltTble](CompFiltTble.md)
- [CompTbleInit](CompTbleInit.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompTbleGap](CompTbleGap.md)
- [CompTbleCrrct](CompTbleCrrct.md)
- [Force](../../08-axis-operation/04-force-operation-mode/Force.md)
