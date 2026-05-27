---
keyword: EventTableSrc
summary: Selects the position source used to evaluate event table triggers.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 313
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
# EventTableSrc

Selects the position source used to evaluate event table triggers.

## Overview

`EventTableSrc` selects the position source used to evaluate [EventTable](EventTable.md) triggers (for example, the command position versus the actual position). The choice determines which feedback the comparator watches when generating table-driven events. It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
AEventTableSrc=0     ; select the position source (default)
AEventTableSrc=1     ; select the alternate position source
AEventTableSrc      ; query the current source
```

## See also

- [EventTable](EventTable.md) — table of event positions
- [EventSelect](EventSelect.md) — selects the event-generator mode
- [EventTableBeg](EventTableBeg.md) — first active table index
