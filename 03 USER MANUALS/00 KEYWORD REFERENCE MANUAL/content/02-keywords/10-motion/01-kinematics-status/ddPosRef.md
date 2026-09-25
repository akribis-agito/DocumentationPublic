---
keyword: ddPosRef
summary: Acceleration reference, the second derivative of the position reference PosRef.
availability:
  standalone: []
  central-i:
  - v5
can_code: 857
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-08-02'
doc_revision: '2026.07'
---
# ddPosRef

Acceleration reference, the second derivative of the position reference PosRef.

## Overview

`ddPosRef` is the acceleration reference of the axis. It is the signal the controller feeds forward through the acceleration feed-forward gain `AccFFW`, and it is the second member of the reference derivative chain [PosRef](PosRef.md) → [dPosRef](dPosRef.md) → `ddPosRef` → [dddPosRef](dddPosRef.md).

`ddPosRef` is a *reference*, derived from the commanded trajectory. It is not a measurement of the axis: there is no acceleration feedback signal, and `ddPosRef` is unaffected by what the motor actually does.

## How it works

Every control cycle the controller produces `ddPosRef` by one of two methods, chosen automatically. Which one is in use is reported by the read-only keyword `FFWMode`:

- **Trajectory mode** (`FFWMode` = 1) — the acceleration is taken **directly from the profiler's own equations**, alongside the velocity and jerk references. Because all four quantities come from the same evaluation of the trajectory, they are cycle-aligned with the position reference and carry no sampling delay.
- **Derivative mode** (`FFWMode` = 0) — the acceleration is computed as the **second difference** of the fully post-processed position reference, the shaped and filtered signal the position loop itself uses:

$$
\text{ddPosRef} = \left( P_k - 2P_{k-1} + P_{k-2} \right) \times 2^{n}
$$

where $P$ is the shaped+filtered position reference and $n$ is the sample-rate exponent (`SAMPLE_FREQUENCY_TWO_POWER`, 14 at the standard 16 kHz control rate, 15 at 32 kHz, 16 at 64 kHz).

### Which mode is selected

Trajectory mode is used only when the trajectory is smooth enough to be differentiated analytically, which the controller takes to mean **all** of the following hold:

- the profiler is running a smooth profile,
- input shaping is off (`ShapingOn` = 0),
- the profiler jerk limit is unset (`Jerk` = 0), and
- the position-reference filter is off (`PosFiltOn` = 0).

If any of those is not met, the reference has been through post-processing the profiler equations do not describe, and the controller falls back to derivative mode. Enabling input shaping or a position filter on a running axis therefore changes how `ddPosRef` is produced, which is visible as a change in `FFWMode`.

## How it is used

`ddPosRef` is multiplied by the acceleration feed-forward gain to form the acceleration feed-forward term added to the current command:

$$
\text{FFW}_{\text{acc}} = \text{ddPosRef} \times \text{AccFFW} \times k
$$

where $k$ is the fixed internal gain scaling. When both `VelFFW` and `AccFFW` are zero and jerk feed-forward is disabled, the controller skips the feed-forward multiplies entirely as an ISR-budget optimisation; `ddPosRef` itself is still produced and still readable.

### Edge cases

- **Motor off:** the previous-cycle acceleration store used by derivative mode is reset to `0`, so the first cycle after enabling starts from a clean difference rather than differencing across the disabled interval.
- **Profiler stopped:** the trajectory-mode acceleration source is cleared to `0` when the profiler finishes or is stopped, so a completed move does not leave a stale acceleration reference behind.
- **Mode switch mid-move:** `FFWMode` is evaluated every cycle. A switch between trajectory and derivative mode changes the source of `ddPosRef` on the same cycle.
- **Out-of-range write:** `ddPosRef` is read-only.

## Examples

```text
AddPosRef           ; read the current acceleration reference
AFFWMode            ; is it coming from the profiler (1) or a derivative (0)?
```

## See also

- [PosRef](PosRef.md) — position reference, the source of the derivative chain
- [dPosRef](dPosRef.md) — velocity reference, the first derivative
- [dddPosRef](dddPosRef.md) — jerk reference, the third derivative
- [AccFFW](../../11-control-tuning/05-feedforwards/AccFFW.md) — the gain applied to `ddPosRef`
