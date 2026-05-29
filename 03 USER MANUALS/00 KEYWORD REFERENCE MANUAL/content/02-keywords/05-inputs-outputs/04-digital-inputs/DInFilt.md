---
keyword: DInFilt
summary: Software debounce filter for all digital inputs on an axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 213
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
  - 15
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# DInFilt

Software debounce filter for all digital inputs on an axis.

## Overview

`DInFilt` sets a debounce filter: a raw digital input must hold the same value for `DInFilt` consecutive samples before the change is asserted; otherwise the input keeps its previous state. For example, `DInFilt = 3` requires three consecutive readings of "1" before a "1" is asserted. It is the first stage of the [digital-input signal path](00-overview.md), and runs in hardware at the raw sampling rate (much faster than the per-cycle [DInPort](DInPort-DInPortHigh.md) update).

`DInFilt` is a single value that applies to **all** digital inputs of the axis/module (e.g. `CDInFilt` applies to all inputs of axis/module C). Debouncing improves noise immunity at the cost of reducing the effective sampling rate by the filter factor.

## How it works

Writing `DInFilt` pushes the value down to the hardware: it masks the value to its low 4 bits (`& 0xF`, giving the 0–15 range) and writes it into the hardware filter register. The register packs the filter setting for several axes — 4 bits each — into one word:

```text
filter reg = (DInFilt[C] & 0xF) << 8 | (DInFilt[B] & 0xF) << 4 | (DInFilt[A] & 0xF);
```

So the debounce is performed in hardware, not in the control-loop software. A value of `0` disables debouncing.

## Examples

```text
ADInFilt=3           ; require 3 consecutive matching samples
ADInFilt              ; read back the filter setting
```

### Edge cases

- **Out of range** — values are masked to the low 4 bits (`0`–`15`); writes outside this range are clipped, not rejected.
- **Zero value** — disables debouncing; the raw hardware reading is used directly.
- **Whole-axis scope** — the value applies to **all** inputs on the axis/module; you cannot debounce one input independently of another.
- **Edge detection lag** — debouncing delays both rising and falling edges by up to `DInFilt` raw sample periods; for time-critical inputs (e.g. high-rate begin-motion triggers) prefer the lowest filter that still rejects noise.
- **Motor on/off** — runs in hardware regardless of `MotorOn`.
- **Save** — flash-saveable; reloaded into the hardware register at boot.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — resulting input states (filter is the first stage)
- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — logic inversion (applied after this filter)
