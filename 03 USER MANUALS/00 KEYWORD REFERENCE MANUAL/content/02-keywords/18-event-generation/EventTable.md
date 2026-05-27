---
keyword: EventTable
summary: Array of absolute positions at which event output pulses are generated.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`EventTable` is an array of absolute positions at which event output pulses are generated in the table-driven event mode ([EventType](EventType.md) = 2). Each element defines a position trigger point in user units; entries must be ordered from low to high. The active range of the table is bounded by [EventTableBeg](EventTableBeg.md) (first index used) and [EventTableEnd](EventTableEnd.md) (last index used). It is an axis-related array parameter and is not saved to flash.

The number of usable entries is model-dependent (100 on most models, more on larger models). Because event-table indexing is 1-based, entries are stored from index 1 upward; index 0 is not used as a table position.

## How it works

When you arm table-driven events with [EventOn](EventOn.md) = 1, the controller loads the entry at [EventTableBeg](EventTableBeg.md) as the first compare position and copies its per-entry selection from [EventTableSel](EventTableSel.md). As the axis moves, a position comparator watches the feedback position and produces an output pulse when the position reaches the active compare value. Immediately after each pulse the controller advances one index, loads the next table entry as the new compare position, and applies that entry's selection and pulse width. Generation stops once the index passes [EventTableEnd](EventTableEnd.md).

The position source the comparator watches is chosen by [EventTableSrc](EventTableSrc.md): the raw entries in `EventTable`, or the corrected entries in [EventTableCor](EventTableCor.md) (produced by [EventCorrect](EventCorrect.md) when an encoder error map is active). When a pure-software comparison is used, the feedback is already corrected, so the raw table is read directly and the source selection has no effect.

Each comparison also tracks the expected travel direction from the sign of the step between successive entries, so a table whose positions rise and then fall still triggers correctly as the axis reverses.

## Examples

```text
AEventTable[1]=1000      ; first table position (user units)
AEventTable[2]=3000      ; second table position
AEventTable[1]           ; query the first table entry
```

A minimal table-driven setup that fires three pulses:

```text
AEventType=2             ; table mode
AEventTableBeg=1         ; use entries 1..3
AEventTableEnd=3
AEventTable[1]=1000
AEventTable[2]=3000
AEventTable[3]=6000
AEventPulseWid=50        ; 50 us output pulse at each entry
AEventOn=1               ; arm (set while below the first entry)
```

## See also

- [EventTableCor](EventTableCor.md) — corrected positions after EventCorrect
- [EventTableSel](EventTableSel.md) — per-entry selection
- [EventTableSrc](EventTableSrc.md) — position source for table evaluation
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
