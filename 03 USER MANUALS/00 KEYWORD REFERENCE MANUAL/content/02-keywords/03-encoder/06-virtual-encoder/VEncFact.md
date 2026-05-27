---
keyword: VEncFact
summary: Numerator of the scaling ratio applied to the virtual encoder source signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`VEncFact` is the numerator of the scaling ratio applied to the virtual encoder source signal. The effective scale factor is `VEncFact / VEncFactDen`, which maps the virtual encoder position from the source units to the desired output resolution. It is used with [VEncFactDen](VEncFactDen.md) (the denominator) when the virtual encoder is enabled ([VEncOn](VEncOn.md) = 1). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

$$Scale\ factor = \frac{VEncFact}{VEncFactDen}$$

## Examples

```text
AVEncFact=65536          ; unity scale when VEncFactDen=65536
```

## See also

- [VEncFactDen](VEncFactDen.md) — denominator of the scaling ratio
- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source signal that is scaled
