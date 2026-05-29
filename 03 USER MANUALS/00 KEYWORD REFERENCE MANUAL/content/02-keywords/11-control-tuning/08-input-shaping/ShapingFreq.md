---
keyword: ShapingFreq
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 152
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 32768000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingFreq

Resonance frequencies suppressed by the input shaper.

## Overview

`ShapingFreq` stores the resonance frequencies of the vibration modes that the input shaper suppresses. Up to two frequencies are supported: `ShapingFreq[1]` and `ShapingFreq[2]`, each paired with the corresponding damping ratio in [ShapingDamp](ShapingDamp.md). The shaper is active only when input shaping is enabled by [ShapingOn](ShapingOn.md). `ShapingFreq` is saved to flash and cannot be changed while the axis is in motion or the motor is on.

The first frequency must be non-zero for the shaper to act. The second frequency is optional; leaving `ShapingFreq[2] = 0` uses a single resonance.

### Units, scaling and range

Frequencies are stored scaled by 65536 — the stored value equals the frequency in Hz multiplied by 65536:

$$
\text{ShapingFreq} = f_{\text{Hz}} \cdot 65536
$$

| | Value |
|---|---|
| Unit | Hz × 65536 |
| Range | 0 to 32768000 (0 to 500 Hz) |
| Default | 0 (shaper inactive) |

The lowest usable frequency depends on the length of the shaper's history buffer, which differs by product. If a configured frequency is out of range, the shaper is disabled for the axis.

## How it works

For each resonance the controller computes the half-period spacing from the frequency (the impulses are placed at 0, half the period and one full period, where the period is 1/`f`) and the impulse amplitudes from the damping ratio in [ShapingDamp](ShapingDamp.md). The amplitudes for one resonance are:

$$
A_0 = \frac{1}{1 + 2K + K^2}, \quad A_1 = \frac{2K}{1 + 2K + K^2}, \quad A_2 = \frac{K^2}{1 + 2K + K^2}
$$

$$
K = e^{\,-\zeta \pi / \sqrt{1 - \zeta^{2}}}
$$

where ζ is the damping ratio from [ShapingDamp](ShapingDamp.md). The amplitudes sum to 1. With two frequencies defined, the two three-impulse sequences are convolved into a nine-impulse sequence; the history buffer must be long enough to hold the combined span, otherwise the shaper is disabled.

## Examples

```text
AShapingFreq[1]=3276800   ; first resonance at 50 Hz (50 x 65536)
AShapingFreq[2]=0         ; no second resonance
AShapingDamp[1]=3277      ; damping ratio 0.05
AShapingOn=1              ; enable input shaping
```

## See also

- [ShapingOn](ShapingOn.md) — enable/disable input shaping
- [ShapingDamp](ShapingDamp.md) — damping ratio paired with each frequency
