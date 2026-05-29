---
keyword: MasterFilt
summary: First-order low-pass filter coefficient for the scaled master-position delta (direct gear motion).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 161
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
  - 1
  - 64
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFilt

First-order low-pass filter coefficient for the scaled master-position delta (direct gear motion).

## Overview

`MasterFilt` is the coefficient of a first-order low-pass filter applied to the geared reference in **direct** gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5`). It smooths how the follower tracks the master, suppressing steps caused by a coarse or pulsed master signal combined with a high gear ratio. Indirect gear motion (`= 6`) does not use it — there the PTP profiler smooths the motion instead.

## How it works

### The filter

In direct gear motion the geared displacement since `Begin`, $u_{k} = \text{MasterPos} - \text{MasterPosInitial}$, is passed through a first-order low-pass filter before being added to the reference latched at `Begin` to form `PosRef`. The filter coefficient is `MasterFilt / 64`:

$$
y_{k} = \frac{\text{MasterFilt}}{64} \cdot u_{k} + \left( 1 - \frac{\text{MasterFilt}}{64} \right) \cdot y_{k - 1}
$$

where $t = k \cdot T_{s}$ and $T_{s}$ is the control sampling time (typically 61 µs).

### Choosing the value

`MasterFilt` ranges `1 … 64`. The two extremes bracket the behaviour:

- `MasterFilt = 64` ⇒ coefficient 1, i.e. **no filtering** (the follower tracks the master with no lag). This is the value required for the drift-free axis-to-axis gearbox (see [GearMaster](GearMaster.md)).
- small `MasterFilt` ⇒ heavy smoothing and more tracking lag.

By backward-Euler estimation, `MasterFilt` can be chosen from a target cut-off frequency $f_{c}$ (Hz). The default `MasterFilt = 3` corresponds to roughly a 128 Hz cut-off:

$$
\text{MasterFilt} = 64 \cdot \left( \frac{2\pi \cdot f_{c} \cdot T_{s}}{1 + 2\pi \cdot f_{c} \cdot T_{s}} \right)
$$

For example, at the typical 61 µs sample time, picking `MasterFilt = 16` (coefficient 16/64 = 0.25) gives a first-order pole at roughly `f_c = 0.25 / (2π × 61 µs) ≈ 650 Hz`, a moderate smoothing that still tracks fast master changes. Reducing it to `MasterFilt = 3` drops the cut-off back to ~128 Hz, giving a visibly slower follower for the same master step but rejecting more high-frequency noise on the master signal.

## Examples

```text
AMasterFilt=3        ; default (~128 Hz cut-off)
AMasterFilt=64       ; no filtering (1:1 lag-free tracking)
AMasterFilt          ; read current value
```

## See also

- [MasterPos](MasterPos.md) — the geared displacement whose change is filtered
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — gear ratio applied before this filter
- [GearMaster](GearMaster.md) — selects the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — `MasterFilt` applies in direct gear motion (`= 5`)
