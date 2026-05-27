---
keyword: EventPulseWid
summary: Duration of the event output pulse in microseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`EventPulseWid` sets the duration of the event output pulse, in microseconds, determining how long the output signal stays active after each event trigger. With small [EventGap](EventGap.md) values at high velocity, a large pulse width can cause successive pulses to overlap. Per-entry overrides for table-driven events are set with [EventTableWid](EventTableWid.md). It is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
EventPulseWid=50    ; 50 us output pulse (default)
EventPulseWid?      ; query the current pulse width
```

## See also

- [EventPulseRes](EventPulseRes.md) — pulse-generator position resolution
- [EventTableWid](EventTableWid.md) — per-entry pulse width override
- [EventGap](EventGap.md) — small gaps with wide pulses can overlap
