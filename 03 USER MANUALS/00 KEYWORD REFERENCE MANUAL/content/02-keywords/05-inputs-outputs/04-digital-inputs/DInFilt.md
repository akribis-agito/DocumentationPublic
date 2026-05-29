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

`DInFilt` sets a debounce filter: a raw digital input must hold the same new value for `DInFilt` consecutive samples before the change is asserted; if the input falls back to its old level at any point during that interval the count restarts, so a glitch shorter than the filter window never propagates. For example, `DInFilt = 3` requires three consecutive readings of "1" before a "1" is asserted. It is the first stage of the [digital-input signal path](00-overview.md), and runs in hardware: the input is sampled far faster than the control loop (tens of nanoseconds per sample), and the debounced result is reflected in [DInPort](DInPort-DInPortHigh.md) once per control cycle.

`DInFilt` is a single per-axis value (e.g. `CDInFilt` sets the filter for axis/module C). Debouncing improves noise immunity at the cost of delaying accepted edges by the filter length. See [How it works](#how-it-works) for which input path the present firmware actually filters.

## How it works

Writing `DInFilt` pushes the value down to the hardware: it masks the value to its low 4 bits (`& 0xF`, giving the 0–15 range) and writes it into the hardware filter register. That register holds one 4-bit filter setting per axis (A, B, C) packed into a single word, so each axis carries its own debounce length. The debounce is performed in hardware, not in the control-loop software, and a value of `0` disables it (the raw reading passes straight through).

In the present firmware, `DInFilt` is wired to the **pulse/direction capture** input path (the step/direction signals counted into [DInPort](DInPort-DInPortHigh.md)-related position capture), where contact bounce or line noise would otherwise be miscounted as extra steps. The hardware also contains a separate, wider per-port debounce filter for the general isolated/open-collector and differential digital inputs (home, limit, and similar), but present firmware leaves that filter at its minimum (effectively unfiltered) setting. As a result, raising `DInFilt` reliably cleans up the pulse/direction capture path; do not assume it will, on its own, debounce a switch wired to a general-purpose digital input.

### Hardware behavior

The debouncer samples the input on a fixed hardware tick (about 40 ns for the pulse/direction path). On each tick it compares the freshly sampled level against the level it is currently presenting; while they differ it counts ticks, and only when the count reaches the `DInFilt` threshold does it accept the new level and reset the counter. Any return to the previously accepted level during that window resets the counter to zero immediately. So the accept delay is approximately `DInFilt + 1` ticks (the threshold plus the input-synchronization tick), and a disturbance shorter than that window is rejected outright rather than averaged.

For the pulse/direction path (≈40 ns tick), the resulting minimum accept delay is approximately:

| `DInFilt` | Approximate accept delay |
|-----------|--------------------------|
| 0         | pass-through (no debounce) |
| 3         | ≈ 160 ns |
| 8         | ≈ 360 ns |
| 15 (max)  | ≈ 640 ns |

These figures assume the standard pulse/direction sampling tick; the exact value is product-specific.

## Examples

```text
ADInFilt=3           ; require 3 consecutive matching samples
ADInFilt              ; read back the filter setting
```

### Edge cases

- **Out of range** — values are masked to the low 4 bits (`0`–`15`); writes outside this range are clipped, not rejected.
- **Zero value** — disables debouncing; the raw hardware reading is used directly.
- **Per-axis scope** — one filter length per axis/module; you cannot debounce one input independently of another on the same axis. In present firmware the setting acts on the pulse/direction capture path (see [How it works](#how-it-works)).
- **Edge detection lag** — debouncing delays both rising and falling edges by up to `DInFilt` raw sample periods; for time-critical inputs (e.g. high-rate begin-motion triggers) prefer the lowest filter that still rejects noise.
- **Motor on/off** — runs in hardware regardless of `MotorOn`.
- **Save** — flash-saveable; reloaded into the hardware register at boot.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — resulting input states (filter is the first stage)
- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — logic inversion (applied after this filter)
