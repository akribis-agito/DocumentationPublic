---
keyword: FricBrstlStf
summary: LuGre bristle stiffness (σ0), used by FricMethod 4 (renamed from FricSigma0).
availability:
  standalone: []
  central-i:
  - v5
can_code: 935
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1000000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricBrstlStf

LuGre bristle stiffness (σ0), used by FricMethod 4 (renamed from FricSigma0).

## Overview

`FricBrstlStf` is the LuGre model's bristle stiffness, σ0. Available on AGM800 and AGM800-EC (central-i v5). It replaces `FricSigma0` from 5.3.0-rc4 (same CAN code). Only method 4 (LuGre) uses it.

## How it works

LuGre treats the contact as many small bristles that bend before they slip. With bristle deflection $z$ and velocity feedback $v$:

$$
\frac{dz}{dt} = v - \frac{\sigma_0\,|v|\,z}{g(v)}, \qquad
I = \sigma_0 z + \sigma_1 \frac{dz}{dt} + \sigma_2 v
$$

where $g(v)$ is the Stribeck curve from [FricIPos](FricIPos.md)/[FricINeg](FricINeg.md), [FricIStatPos](FricIStatPos.md)/[FricIStatNeg](FricIStatNeg.md) and [FricVStribPos](FricVStribPos.md)/[FricVStribNeg](FricVStribNeg.md), σ0 is [FricBrstlStf](FricBrstlStf.md), σ1 is [FricBrstlDmp](FricBrstlDmp.md) and σ2 is [FricViscous](FricViscous.md).

A stiffer bristle (larger value) makes the model react faster to small motions near a reversal. Values saved under 5.3.0-rc4 are not converted. After upgrading from rc4, re-enter the friction settings.

## Examples

```text
AFricBrstlStf=50      ; bristle stiffness, mA per count
```

## See also

- [FricMethod](FricMethod.md)
- [Friction feedforward](00-overview.md)
