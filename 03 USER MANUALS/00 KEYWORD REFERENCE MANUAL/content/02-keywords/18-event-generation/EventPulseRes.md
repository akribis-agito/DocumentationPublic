---
keyword: EventPulseRes
summary: 'Selects the time unit used to interpret the event pulse width: microseconds or nanoseconds.'
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 517
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
# EventPulseRes

Selects the time unit used to interpret the event pulse width: microseconds or nanoseconds.

## Overview

`EventPulseRes` selects the time unit in which the event output pulse width is expressed. The values in [EventPulseWid](EventPulseWid.md) and the per-entry [EventTableWid](EventTableWid.md) are interpreted as microseconds or as nanoseconds according to this setting, letting you specify either ordinary millisecond-class pulses or very short nanosecond-class pulses. It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

| Value | Width unit for EventPulseWid / EventTableWid |
|-------|----------------------------------------------|
| 0 (default) | Microseconds. |
| 1 | Nanoseconds. |

The controller converts the requested width into the pulse generator's internal timebase when events are armed. To preserve precision across the full range, it automatically selects a coarse or fine internal time step depending on the requested duration, so both very short and longer pulses are timed accurately. Changing `EventPulseRes` rescales how a given numeric width is interpreted, so review [EventPulseWid](EventPulseWid.md) and any [EventTableWid](EventTableWid.md) entries after changing it.

The exact resolution and maximum depend on the hardware. On central-i remote drives with incremental or SIN-COS feedback the pulse is timed by a hardware counter with a resolution of about **20 ns** for widths up to roughly **163.8 us**, and a coarser **5.12 us** step for longer widths, with a longest producible pulse of approximately **1.34 seconds**. On stand-alone products the resolution and maximum differ (a shorter maximum applies). In all cases the controller picks the fine or coarse internal step automatically from the requested duration, so `EventPulseRes` only selects the *unit* you type the width in (microseconds or nanoseconds); it does not change the achievable resolution, which depends on how long the pulse is. Requesting a width below the finest step rounds to the nearest achievable step, and 0 selects toggle mode rather than a zero-length pulse.

## Examples

```text
AEventPulseRes=0     ; widths are in microseconds (default)
AEventPulseRes=1     ; widths are in nanoseconds
AEventPulseRes       ; query the current setting
```

## See also

- [EventPulseWid](EventPulseWid.md) — duration of each event pulse
- [EventSelect](EventSelect.md) — selects which output line the event pulse drives
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
