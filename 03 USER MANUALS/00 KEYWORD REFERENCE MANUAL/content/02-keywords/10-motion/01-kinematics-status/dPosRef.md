---
keyword: dPosRef
summary: Velocity reference, the filtered derivative of the position reference PosRef.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 155
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# dPosRef

Velocity reference, the filtered derivative of the position reference PosRef.

## Overview

`dPosRef` is the velocity reference, computed as the filtered derivative of the position reference [PosRef](PosRef.md). The filter is a first-order low-pass filter defined by [dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md). It is the velocity feed-forward fed into the velocity-loop reference.

`dPosRef` is the *velocity reference* and must not be confused with [VelRef](VelRef.md), the *velocity-loop reference/input*. `VelRef` is the sum of the position-controller output and the scaled velocity reference, whereas `dPosRef` is purely the (filtered) derivative of `PosRef`.

## How it works

Each control cycle, while the motor is on, the controller takes the per-cycle change of the fully post-processed reference (the shaped+filtered position reference, the same signal the position loop uses) and optionally low-pass-filters it:

$$
\Delta = (\text{shaped/filtered reference}) - (\text{previous shaped/filtered reference})
$$

- **No filter** ([dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md) coefficient = 1.0): `dPosRef = Δ` directly.
- **With filter:** a first-order low-pass is applied. To keep accuracy over a wide dynamic range, the filter runs on an internally up-scaled value (scaled ×16) so fractional steps are not lost, then shifts back down. A 1-count residual correction snaps the output to `Δ` at steady state so a ramp command is tracked exactly.

When the motor is off, `dPosRef` (and its scaled filter state) is reset to `0` so the filter starts clean on the next enable. As a special case, for member axes of a CNCA/B or vector motion whose master tells them to skip the calculation, `dPosRef` is left unchanged to avoid spikes at the end of segments ending at zero speed.

`dPosRef` then becomes the velocity feed-forward in [VelRef](VelRef.md): $\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}$, where [VelTrackFact](../../11-control-tuning/04-velocity-control/VelTrackFact.md) scales how much feed-forward is applied.

## Examples

```text
AdPosRef            ; read the current velocity reference
```

## Changes between versions

In **v5 (central-i)** the derivative is taken on the 64-bit reference and the value is 64-bit; the per-cycle-difference computation, the `dPosRefFilt` low-pass and the motor-off reset are the same, and it is still used as the velocity feed-forward in `VelRef`. **v5 is central-i only.**

## See also

- [PosRef](PosRef.md) — position reference, the source of this derivative
- [dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md) — the low-pass filter applied to the derivative
- [VelTrackFact](../../11-control-tuning/04-velocity-control/VelTrackFact.md) — feed-forward gain applied to `dPosRef` in `VelRef`
- [VelRef](VelRef.md) — velocity-loop reference/input (a different signal)
