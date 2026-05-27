---
keyword: VEncFactDen
summary: Denominator of the scaling ratio applied to the virtual encoder source signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 618
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
  - 500000000
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncFactDen

Denominator of the scaling ratio applied to the virtual encoder source signal.

## Overview

`VEncFactDen` is the denominator of the scaling ratio applied to the virtual encoder source. Together with [VEncFact](VEncFact.md) it defines the exact rational scale factor (`VEncFact / VEncFactDen`) used to convert the source variable into the emitted encoder count when the virtual encoder is enabled ([VEncOn](VEncOn.md) = 1). Its range is 1 to 500,000,000 and it must be positive (direction inversion is done via a negative [VEncFact](VEncFact.md)). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

$$Output\ count = Source \times \frac{VEncFact}{VEncFactDen}$$

The firmware keeps a precomputed `1 / VEncFactDen` for the per-cycle tracking calculation (updated by `SpVEncFact` in `SpecialFuncs.c`). The default `VEncFactDen = 65536` (with `VEncFact = 65536`) gives unity scaling and matches the fixed `/65536` factor used by older firmware.

## Examples

```text
AVEncFactDen=65536       ; unity scale when VEncFact=65536
```

## See also

- [VEncFact](VEncFact.md) — numerator of the scaling ratio (set negative to invert direction)
- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source variable that is scaled
