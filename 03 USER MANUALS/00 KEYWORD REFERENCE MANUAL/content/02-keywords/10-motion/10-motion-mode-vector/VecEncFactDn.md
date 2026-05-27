---
summary: Denominator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).
keyword: VecEncFactDn
availability:
  standalone: []
  central-i:
  - v5
can_code: 713
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
# VecEncFactDn

Denominator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).

## Overview

`VecEncFactDn` is the denominator of the encoder scaling ratio applied to the vector motion position reference for this axis. Together with [VecEncFactNu](VecEncFactNu.md) it defines the rational scale `VecEncFactNu / VecEncFactDn` mapping vector position units to axis encoder counts, so that axes with different encoder resolutions can take part in the same coordinated vector move. It is an axis-related parameter. This serves the same compensation purpose as the integer-ratio keyword [VecEncRatio](VecEncRatio.md).

> **Note:** `VecEncFactDn` was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and parameter attributes before use.

> **Documentation pending:** Frontmatter attributes (access, range, default, etc.) are unconfirmed pending firmware verification.

## See also

- [VecEncFactNu](VecEncFactNu.md) — numerator of the scaling ratio
- [VecEncRatio](VecEncRatio.md) — single-value encoder-resolution compensation
- [VecSpeed](VecSpeed.md) — commanded resultant speed
