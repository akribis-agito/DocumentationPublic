---
keyword: EventCorrect
summary: Command that recalculates corrected event-table positions from the current axis position and mapping.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 419
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventCorrect

Command that recalculates corrected event-table positions from the current axis position and mapping.

## Overview

`EventCorrect` is a command that recalculates and corrects the event-table positions based on the current axis position and mapping, writing the result to [EventTableCor](EventTableCor.md). It cannot be executed while the axis is in motion (`ok_in_motion: false`). It is an axis-related command and is not saved to flash. Use it to realign the table-driven event grid after the reference position has shifted.

## Examples

```text
AEventCorrect        ; recompute the corrected event-table positions
```

## See also

- [EventTable](EventTable.md) — source positions being corrected
- [EventTableCor](EventTableCor.md) — holds the corrected positions
- [EventSelect](EventSelect.md) — selects the event-generator mode
