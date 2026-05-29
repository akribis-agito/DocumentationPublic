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

The width behavior is decided first by the value at the begin entry — the entry at the [EventTableBeg](EventTableBeg.md) index — which sets the mode for the whole event session:

| Begin-entry value | Behavior for the whole active range |
|-------------------|-------------------------------------|
| 0 | **Toggle mode** for the entire session: each event changes the output state instead of producing a fixed-duration pulse. Per-entry widths are not applied. |
| -1 (default) | The global [EventPulseWid](EventPulseWid.md) is used for **every** event; per-entry widths are ignored. |
| Positive | **Per-entry widths** are used, with carry-forward (see below). |

When the begin entry is positive, each entry's width is resolved as follows:

| Entry value | Width used for that entry |
|-------------|---------------------------|
| Positive | That value, as the pulse duration (units per [EventPulseRes](EventPulseRes.md)). It also becomes the carried-forward width for later `-1` entries. |
| -1 | The most recent positive per-entry width seen earlier in the active range; if none has been seen yet, the global [EventPulseWid](EventPulseWid.md). |
| 0 | A zero-width pulse for that entry. A `0` on a non-begin entry does **not** toggle — toggle mode is enabled only when the begin entry itself is `0`. |

The valid range for each entry is -1 to 10000000; -1 is the only negative value (it defers to the global width). Output polarity is taken from the sign of the width actually in use for the entry: a per-entry width is always non-negative, so inversion happens only when an entry defers (via `-1`) to a negative global [EventPulseWid](EventPulseWid.md). A positive per-entry width never inverts, even if the global is negative.

Set the begin entry ([EventTableBeg](EventTableBeg.md) index) to `-1` if you want the whole table to follow the global width by default, or to `0` to put the whole session in toggle mode.

## Examples

```text
; Per-entry widths (begin entry positive): set the begin entry to a width
AEventTableWid[1]=50     ; begin entry: 50-unit pulse; enables per-entry mode
AEventTableWid[2]=100    ; second entry uses a 100-unit pulse
AEventTableWid[3]=0      ; third entry produces a zero-width pulse (does NOT toggle)
AEventTableWid[2]        ; query the second entry's pulse width

; Global width for the whole range: set the begin entry to -1
AEventTableWid[1]=-1     ; whole active range uses the global EventPulseWid;
                         ; per-entry values on other entries are ignored

; Toggle mode for the whole session: set the begin entry to 0
AEventTableWid[1]=0      ; every event toggles the output instead of pulsing
```

## See also

- [EventPulseWid](EventPulseWid.md) — global pulse width used when an entry is -1
- [EventTableSel](EventTableSel.md) — per-entry selection
- [EventTable](EventTable.md) — table of event positions
