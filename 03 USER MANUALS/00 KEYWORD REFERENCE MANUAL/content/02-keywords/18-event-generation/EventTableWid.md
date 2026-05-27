---
keyword: EventTableWid
summary: Per-entry pulse width array; -1 uses the global EventPulseWid.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`EventTableWid` is an array that specifies the pulse width for each [EventTable](EventTable.md) entry individually, overriding the global [EventPulseWid](EventPulseWid.md) for selected entries. The width units follow [EventPulseRes](EventPulseRes.md) (microseconds or nanoseconds), the same as `EventPulseWid`. It is an axis-related array parameter and is not saved to flash.

## How it works

For each table entry the controller chooses the output pulse width as follows:

| Entry value | Width used for that entry |
|-------------|---------------------------|
| -1 (default) | The global [EventPulseWid](EventPulseWid.md). |
| 0 | Toggle mode: the output changes state at the entry instead of producing a fixed-duration pulse. |
| Positive | That value, as the pulse duration (units per [EventPulseRes](EventPulseRes.md)). |
| Negative | That magnitude as the duration, with inverted output polarity. |

When an entry is `-1`, the controller does not always fall back to the global width: it carries forward the most recent positive per-entry width seen earlier in the active range, and uses the global [EventPulseWid](EventPulseWid.md) only if no positive per-entry width has been encountered yet. Set the first active entry ([EventTableBeg](EventTableBeg.md)) to `-1` if you want the whole table to follow the global width by default.

## Examples

```text
AEventTableWid[1]=-1     ; first entry uses the global EventPulseWid
AEventTableWid[2]=100    ; second entry uses a 100 us pulse
AEventTableWid[3]=0      ; third entry toggles the output instead of pulsing
AEventTableWid[2]        ; query the second entry's pulse width
```

## See also

- [EventPulseWid](EventPulseWid.md) — global pulse width used when an entry is -1
- [EventTableSel](EventTableSel.md) — per-entry selection
- [EventTable](EventTable.md) — table of event positions
