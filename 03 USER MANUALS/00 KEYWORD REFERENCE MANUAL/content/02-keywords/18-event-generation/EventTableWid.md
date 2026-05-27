---
keyword: EventTableWid
summary: Per-entry pulse width array; -1 uses the global EventPulseWid.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 497
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 10000000
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableWid

Per-entry pulse width array; -1 uses the global EventPulseWid.

## Overview

`EventTableWid` is an array that specifies the pulse width for each [EventTable](EventTable.md) entry individually, overriding the global [EventPulseWid](EventPulseWid.md) for selected entries. A value of `-1` (the default) makes that entry use the global pulse width. It is an axis-related array parameter and is not saved to flash.

## Examples

```text
AEventTableWid[1]=-1     ; first entry uses the global EventPulseWid
AEventTableWid[2]=100    ; second entry uses a 100 us pulse
AEventTableWid[2]       ; query the second entry's pulse width
```

## See also

- [EventPulseWid](EventPulseWid.md) — global pulse width used when an entry is -1
- [EventTableSel](EventTableSel.md) — per-entry selection
- [EventTable](EventTable.md) — table of event positions
