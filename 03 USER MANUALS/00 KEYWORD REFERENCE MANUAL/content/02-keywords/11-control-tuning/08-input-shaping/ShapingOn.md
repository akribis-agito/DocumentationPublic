---
keyword: ShapingOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 151
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingOn

Enables or disables input shaping on the axis.

## Overview

`ShapingOn` enables input shaping (command filtering) on the axis. When enabled, the position reference is convolved with an impulse sequence so that the energy at one or two resonant frequencies cancels, suppressing residual vibration as the axis settles. The resonance frequencies and their damping ratios are set by [ShapingFreq](ShapingFreq.md) and [ShapingDamp](ShapingDamp.md).

| `ShapingOn` | Behaviour |
|---|---|
| 0 | Input shaping disabled (default). |
| 1 | Input shaping enabled — the reference is shaped by the impulse sequence built from [ShapingFreq](ShapingFreq.md) and [ShapingDamp](ShapingDamp.md). |

`ShapingOn` is saved to flash and cannot be changed while the axis is in motion or the motor is on. Input shaping is applied only in position or velocity operation mode (not in current or force mode), and it cannot be combined with modulo (continuous-rotation) mode on the main encoder.

## How it works

The shaper is a finite-impulse-response (FIR) operation on the post-profiler position reference. For a single resonance it applies three impulses, spaced at 0, half the resonance period and one full period:

$$
shaped_k = A_0 \cdot ref_k + A_1 \cdot ref_{k-N} + A_2 \cdot ref_{k-2N}
$$

where the half-period spacing `N` corresponds to one half-cycle of the resonance frequency. The impulse amplitudes are derived from the damping ratio (see [ShapingFreq](ShapingFreq.md) and [ShapingDamp](ShapingDamp.md)) and always sum to 1, so a steady reference passes through unchanged and only the dynamic transient is reshaped. With two resonance frequencies defined, the two three-impulse sequences are convolved into a nine-impulse sequence.

The shaper's history buffer is initialised to the current reference when the motor is enabled, so motion starts cleanly.

## Examples

```text
AShapingFreq[1]=3276800   ; resonance at 50 Hz (value = Hz x 65536)
AShapingDamp[1]=3277      ; damping ratio 0.05
AShapingOn=1              ; enable input shaping
```

### Worked example: impulse timing and amplitudes for a 50 Hz / 0.05 damping mode

For `ShapingFreq[1]` = 50 Hz and `ShapingDamp[1]` = 0.05 (ζ = 0.05):

- Period T = 1 / 50 Hz = 20 ms
- Impulse positions: 0 ms, T/2 = 10 ms, T = 20 ms
- K = exp(-0.05 x π / √(1 - 0.05²)) ≈ 0.855
- 1 + 2K + K² ≈ 3.441
- A₀ ≈ 1 / 3.441 ≈ 0.291
- A₁ ≈ 2 x 0.855 / 3.441 ≈ 0.497
- A₂ ≈ 0.855² / 3.441 ≈ 0.213
- Sum: A₀ + A₁ + A₂ ≈ 1.001 (rounding); exactly 1 in the controller's fixed-point form.

The shaper therefore adds the original reference (weight 0.291), the same reference delayed by 10 ms (weight 0.497) and again delayed by 20 ms (weight 0.213). A step from 0 to a setpoint reaches the setpoint after 20 ms, but the residual oscillation at 50 Hz is cancelled.

## See also

- [ShapingFreq](ShapingFreq.md) — resonance frequency / frequencies to suppress
- [ShapingDamp](ShapingDamp.md) — damping ratio of each resonance
