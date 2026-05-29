---
keyword: ShapingDamp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 153
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
  - 1
  - 65535
  default: 32768
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingDamp

Damping ratio of each resonance suppressed by the input shaper.

## Overview

`ShapingDamp` stores the damping ratio of each resonance mode defined in [ShapingFreq](ShapingFreq.md). Element `ShapingDamp[1]` pairs with `ShapingFreq[1]` and `ShapingDamp[2]` with `ShapingFreq[2]`. The damping ratio sets the relative amplitudes of the shaper's impulses; the frequency sets their timing. The shaper is active only when input shaping is enabled by [ShapingOn](ShapingOn.md). `ShapingDamp` is saved to flash and cannot be changed while the axis is in motion or the motor is on.

### Units, scaling and range

The damping ratio is stored scaled by 65536 — the stored value equals the damping ratio multiplied by 65536:

$$
\text{ShapingDamp} = \zeta \cdot 65536
$$

| | Value |
|---|---|
| Unit | damping ratio × 65536 |
| Range | 1 to 65535 (ζ just above 0 to just below 1) |
| Default | 32768 (ζ = 0.5) |

The damping ratio must be a positive fraction below 1.

## How it works

The damping ratio ζ is converted into the shaper amplitude term:

$$
K = e^{\,-\zeta \pi / \sqrt{1 - \zeta^{2}}}
$$

and the three impulse amplitudes for the corresponding resonance are formed from $K$:

$$
A_0 = \frac{1}{1 + 2K + K^2}, \quad A_1 = \frac{2K}{1 + 2K + K^2}, \quad A_2 = \frac{K^2}{1 + 2K + K^2}
$$

The amplitudes always sum to 1, so a steady reference is unaffected. With two resonances defined, the two amplitude sets are convolved together (see [ShapingFreq](ShapingFreq.md)).

## Examples

```text
AShapingFreq[1]=3276800   ; resonance at 50 Hz (50 x 65536)
AShapingDamp[1]=6554      ; damping ratio 0.10 (0.10 x 65536)
AShapingOn=1              ; enable input shaping
```

## See also

- [ShapingOn](ShapingOn.md) — enable/disable input shaping
- [ShapingFreq](ShapingFreq.md) — resonance frequency paired with each damping ratio
