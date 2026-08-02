---
keyword: DTCompGain
summary: Dead-time compensation gain; 0 disables the feature.
availability:
  standalone: []
  central-i:
  - v5
can_code: 869
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 10
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# DTCompGain

Dead-time compensation gain; 0 disables the feature.

## Overview

A power bridge must never let both transistors in a leg conduct at once, so the drive inserts a short blanking interval — the *dead time* — on every switching edge. During it neither device conducts and the phase receives no voltage. The loss is a fixed number of volt-seconds per PWM period, so it costs a roughly constant amount of current regardless of how much you asked for, and therefore hurts proportionally most at low current.

`DTCompGain` scales a compensating voltage added in the direction of each commanded phase current. `0` makes the compensation an exact no-op.

## How it works

Each control cycle the drive adds a voltage of magnitude proportional to `DTCompGain` to each phase, signed by that phase's commanded current. Within a band of ±[DTCompLvl](DTCompLvl.md) around zero current the sign is interpolated linearly rather than switched, so the compensation does not chatter as the current crosses zero.

> **Important:** `DTCompGain` is a **per-drive calibration**, not a universal setting. The correct value depends on the blanking time of the drive you are using, and the blanking time differs across the range — an AGD155 has four times the dead band of an AGD301. The default of 1.0 is not the optimum for either.

> **Worked example:** `DTCompGain = 0` adds no voltage at all, so the drive behaves as one without the compensation. A gain of 1.0 adds the drive's nominal dead-band correction, and higher values scale it proportionally.
>
> The consequence worth knowing is that the error curve has a **minimum, not a plateau**: below the optimum the compensation under-corrects and some of the stolen volt-seconds remain, and above it the drive over-corrects and the error grows again symmetrically. Too high is as wrong as too low, so the value has to be found by measurement — and the optimum does **not** scale linearly with the dead band, so it cannot be calculated from one drive's value for another.

> **Note:** for the measurement procedure and the values measured per drive, see the *Current-Loop Compensation* application note.

### Finding the right value

1. Command a square-wave current with [InjectType](../../13-injection/InjectType.md) set to square injection at the current reference.
2. Record the tracking error between [CurrRef](../02-motor-variables/CurrRef.md) and the measured current.
3. Raise `DTCompGain` in steps and keep the value that minimises that error.

> **Note:** the error curve has a clear minimum. Past the optimum the drive **over**-compensates and the error grows again, symmetrically — a value that is too high is as wrong as one that is too low.

### Edge cases

- **Closed versus open loop:** a closed current loop's integrator eventually rebuilds most of the missing volt-seconds by itself, so the steady-state current comes out close to correct either way. What dead time costs a closed loop is transient accuracy around each zero crossing. In voltage-mode or open-loop operation the loss appears directly in the delivered current.
- **Low current:** this is where the feature earns its place. At small commands the fixed volt-second loss is a large fraction of the demand.
- **Range:** writes outside `0…10` are clamped.

## Examples

```text
ADTCompGain=5.2      ; calibrated for a 2.0 us dead band (AGD155)
ADTCompGain=2.0      ; calibrated for a 0.5 us dead band (AGD301)
ADTCompGain=0        ; feature disabled (default)
```

## See also

- [DTCompLvl](DTCompLvl.md) — zero-crossing interpolation band
- [CurrRef](../02-motor-variables/CurrRef.md) — the reference the compensation helps the loop follow
