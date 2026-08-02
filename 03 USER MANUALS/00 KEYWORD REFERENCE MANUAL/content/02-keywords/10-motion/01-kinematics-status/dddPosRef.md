---
keyword: dddPosRef
summary: Jerk reference, the third derivative of the position reference PosRef.
availability:
  standalone: []
  central-i:
  - v5
can_code: 858
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
# dddPosRef

Jerk reference, the third derivative of the position reference PosRef.

## Overview

`dddPosRef` is the jerk reference of the axis — the rate of change of the acceleration reference [ddPosRef](ddPosRef.md). It is the last member of the reference derivative chain [PosRef](PosRef.md) → [dPosRef](dPosRef.md) → [ddPosRef](ddPosRef.md) → `dddPosRef`, and it exists to drive the optional jerk feed-forward term.

Unlike the velocity and acceleration references, `dddPosRef` is only *applied* when jerk feed-forward is explicitly enabled. It is computed and readable regardless.

## How it works

`dddPosRef` is produced by the same two-mode mechanism as [ddPosRef](ddPosRef.md), reported by the read-only keyword `FFWMode`:

- **Trajectory mode** (`FFWMode` = 1) — the jerk is taken directly from the profiler's equations, cycle-aligned with the position, velocity and acceleration references and free of sampling delay.
- **Derivative mode** (`FFWMode` = 0) — the jerk is the **first difference of the acceleration reference**, which makes it the third difference of the position reference:

$$
\text{dddPosRef} = \left( \text{ddPosRef}_k - \text{ddPosRef}_{k-1} \right) \times 2^{n}
$$

where $n$ is the sample-rate exponent (`SAMPLE_FREQUENCY_TWO_POWER`, 14 at the standard 16 kHz control rate, 15 at 32 kHz, 16 at 64 kHz).

The mode-selection conditions are described under [ddPosRef](ddPosRef.md) — trajectory mode requires a smooth profile with input shaping, the profiler jerk limit and the position-reference filter all off.

Because derivative mode differentiates the position reference three times, `dddPosRef` is the noisiest signal in the chain: any step or quantisation in the reference is amplified by each successive difference. This is why the applied term is both gated and saturated.

## How it is used

The jerk feed-forward term is applied only when `JerkFFWOn` = 1:

$$
\text{FFW}_{\text{jerk}} = \text{clamp}\left( \text{dddPosRef} \times \text{JerkFFW} \times k,\; \pm\,\text{JerkFFWLim} \right)
$$

where $k$ is the fixed internal gain scaling. `JerkFFWLim` is a symmetric saturation on the resulting term — not on `dddPosRef` itself, which is reported unclamped. With `JerkFFWOn` = 0 the term is not computed and contributes nothing, while `dddPosRef` continues to be updated and can still be read or recorded.

Recording `dddPosRef` with the feed-forward disabled is the normal way to judge whether the jerk reference is clean enough to be worth applying, and to choose `JerkFFWLim`.

### Edge cases

- **Motor off:** the previous-cycle acceleration store that derivative mode differences is reset to `0`, so the first cycle after enabling does not produce a spurious jerk spike from differencing across the disabled interval.
- **Profiler stopped:** the trajectory-mode jerk source is cleared to `0` when the profiler finishes or is stopped.
- **`JerkFFWOn` = 0:** `dddPosRef` is still produced; only the feed-forward term is suppressed.
- **Out-of-range write:** `dddPosRef` is read-only.

## Examples

```text
AdddPosRef          ; read the current jerk reference
AJerkFFWOn=1        ; enable the jerk feed-forward term
AJerkFFWLim=1000    ; saturate the applied term
```

## See also

- [ddPosRef](ddPosRef.md) — acceleration reference, the signal this differentiates
- [dPosRef](dPosRef.md) — velocity reference, the first derivative
- [PosRef](PosRef.md) — position reference, the source of the derivative chain
