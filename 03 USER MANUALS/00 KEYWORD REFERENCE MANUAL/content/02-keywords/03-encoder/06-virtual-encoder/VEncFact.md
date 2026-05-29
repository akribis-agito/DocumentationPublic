---
keyword: VEncFact
summary: Numerator of the scaling ratio applied to the virtual encoder source signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 617
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
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncFact

Numerator of the scaling ratio applied to the virtual encoder source signal.

## Overview

`VEncFact` is the numerator of the scaling ratio applied to the virtual encoder source. The effective scale factor is `VEncFact / VEncFactDen`, mapping the source variable's units onto the emitted encoder count, so the output resolution can be set independently of the source resolution. It is used with [VEncFactDen](VEncFactDen.md) (the denominator) when the virtual encoder is enabled ([VEncOn](VEncOn.md) = 1). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion. `VEncFact` may be **negative** (range −16,777,215 to 16,777,215) to invert the output direction relative to the source.

## How it works

The emitted encoder count tracks the source value scaled by this rational factor:

$$\text{Output count} = \text{Source} \cdot \frac{\text{VEncFact}}{\text{VEncFactDen}}$$

Internally the firmware first multiplies the source by `VEncFact` into a 64-bit "output plane", then a tracking controller drives the emitted count so that `count × VEncFactDen` follows `source × VEncFact`. The default `VEncFact = VEncFactDen = 65536` gives unity scaling and preserves backward compatibility with older firmware that used a fixed `/65536` factor.

## Examples

```text
AVEncFact=65536          ; unity scale when VEncFactDen=65536
AVEncFact=-65536         ; unity scale, inverted output direction
```

## See also

- [VEncFactDen](VEncFactDen.md) — denominator of the scaling ratio
- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source variable that is scaled
