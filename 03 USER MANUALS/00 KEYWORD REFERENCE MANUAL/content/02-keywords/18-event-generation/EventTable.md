---
keyword: EventTable
summary: Array of absolute positions at which event output pulses are generated.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 316
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
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
# EventTable

Array of absolute positions at which event output pulses are generated.

## Overview

`EventTable` is an array of positions at which event output pulses are generated in the table-driven event mode (see [EventType](EventType.md)). Each element defines an absolute position trigger point in user units; entries should be ordered from low to high. The active range of the table is bounded by [EventTableBeg](EventTableBeg.md) and [EventTableEnd](EventTableEnd.md), and corrected positions are produced by [EventCorrect](EventCorrect.md) into [EventTableCor](EventTableCor.md). It is an axis-related array parameter and is not saved to flash.

## Examples

```text
EventTable[1]=1000      ; first table position (user units)
EventTable[2]=3000      ; second table position
EventTable[1]?          ; query the first table entry
```

## See also

- [EventTableCor](EventTableCor.md) — corrected positions after EventCorrect
- [EventTableSel](EventTableSel.md) — per-entry selection
- [EventTableSrc](EventTableSrc.md) — position source for table evaluation
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
