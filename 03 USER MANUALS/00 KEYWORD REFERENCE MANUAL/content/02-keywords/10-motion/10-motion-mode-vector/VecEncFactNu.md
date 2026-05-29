---
summary: Numerator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).
keyword: VecEncFactNu
availability:
  standalone: []
  central-i:
  - v5
can_code: 712
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecEncFactNu

Numerator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).

## Overview

`VecEncFactNu` is the numerator of the per-axis encoder scaling ratio applied to the coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). The effective scale for the axis is `VecEncFactNu / VecEncFactDn`, mapping vector path units to the axis encoder counts so that axes with different encoder resolutions can take part in the same coordinated move while the resultant path stays accurate. It is an axis-related parameter saved to flash, paired with the denominator [VecEncFactDn](VecEncFactDn.md), and cannot be changed while the axis is in motion. This is the numerator/denominator form of the same compensation offered by the single-value keyword [VecEncRatio](VecEncRatio.md).

## How it works

Set the pair so that `VecEncFactNu / VecEncFactDn` equals the resolution ratio needed for the axis. When numerator and denominator are equal (the default `1` / `1`), the ratio is 1 and no scaling is applied. Both keywords accept whole numbers in the range `1`-`2000`, so a wide range of rational ratios can be expressed (for example `3` / `2` for a 1.5:1 resolution difference). Configure the pair on each member axis before starting the move, since it cannot be changed in motion.

> On current firmware the vector path interpolation does not apply this ratio. `VecEncFactNu` / [VecEncFactDn](VecEncFactDn.md) are stored per axis, but the vector move computes each member axis purely from the path geometry; verify behavior against your firmware before relying on vector encoder-resolution compensation.

## Examples

```text
AVecEncFactNu=1        ; numerator = 1 on axis A (default)
AVecEncFactNu=3        ; with VecEncFactDn = 2 gives a 3/2 (1.5:1) scaling ratio
AVecEncFactNu          ; read the current numerator on axis A
```

## See also

- [VecEncFactDn](VecEncFactDn.md) — denominator of the scaling ratio
- [VecEncRatio](VecEncRatio.md) — single-value encoder-resolution compensation
- [VecMemberAxes](VecMemberAxes.md) — axes forming the vector group
- [VecSpeed](VecSpeed.md) — commanded resultant speed
