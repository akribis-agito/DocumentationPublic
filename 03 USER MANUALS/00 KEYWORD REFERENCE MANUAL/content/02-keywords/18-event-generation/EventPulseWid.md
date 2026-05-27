---
keyword: EventPulseWid
summary: Duration of the event output pulse in microseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 179
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
  - -10000000
  - 10000000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventPulseWid

Duration of the event output pulse in microseconds.

## Overview

`EventPulseWid` sets the duration of the event output pulse, determining how long the output signal stays active after each event trigger. The width is expressed in microseconds by default, or in nanoseconds if [EventPulseRes](EventPulseRes.md) = 1. With small [EventGap](EventGap.md) values at high velocity, a large pulse width can cause successive pulses to overlap. Per-entry overrides for table-driven events are set with [EventTableWid](EventTableWid.md). It is an axis-related parameter saved to flash and can be changed at any time.

## How it works

The sign and magnitude of the value control the output:

| Value | Output behavior |
|-------|-----------------|
| Positive | A pulse of that duration with normal polarity (output drives active, then returns to idle). |
| 0 | Toggle mode: the output changes state at each event instead of producing a fixed-duration pulse. |
| Negative | A pulse of that magnitude (duration) with inverted polarity. |

When events are armed, the controller converts the width into the pulse generator's internal timebase, automatically choosing a coarse or fine internal time step so that both short and long pulses are timed accurately. Because the pulse has a fixed duration in time (not in position), the *distance* the axis travels during the pulse grows with velocity. The diagram shows how successive pulses can overlap when the time the axis takes to cross [EventGap](EventGap.md) is shorter than the pulse width:

<svg xmlns="http://www.w3.org/2000/svg" width="460" height="170" font-family="sans-serif" font-size="12">
  <text x="10" y="20">Output, gap time &gt; pulse width (clean pulses):</text>
  <line x1="20" y1="55" x2="440" y2="55" stroke="#888"/>
  <path d="M40 55 V35 H70 V55 H180 V35 H210 V55 H320 V35 H350 V55" fill="none" stroke="#1565c0" stroke-width="2"/>
  <text x="40" y="70" fill="#555">event</text>
  <text x="180" y="70" fill="#555">event</text>
  <text x="320" y="70" fill="#555">event</text>
  <text x="10" y="115">Output, gap time &lt; pulse width (overlap, merged):</text>
  <line x1="20" y1="150" x2="440" y2="150" stroke="#888"/>
  <path d="M40 150 V130 H300 V150" fill="none" stroke="#c62828" stroke-width="2"/>
  <text x="40" y="165" fill="#555">events run together</text>
</svg>

## Examples

```text
AEventPulseWid=50    ; 50 us output pulse (default unit)
AEventPulseWid=-50   ; 50 us pulse, inverted polarity
AEventPulseWid=0     ; toggle the output at each event instead of pulsing
AEventPulseWid       ; query the current pulse width
```

## See also

- [EventPulseRes](EventPulseRes.md) — pulse-generator position resolution
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
- [EventGap](EventGap.md) — small gaps with wide pulses can overlap
