---
summary: Numerator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).
---
# VecEncFactNu

Numerator of the per-axis vector-to-encoder scaling ratio (VecEncFactNu / VecEncFactDn).

## Overview

`VecEncFactNu` is the numerator of the encoder scaling ratio applied to the vector motion position reference for this axis. The effective scale is `VecEncFactNu / VecEncFactDn`, mapping vector position units to the axis encoder counts so that axes with different encoder resolutions can take part in the same coordinated vector move. It is an axis-related parameter, paired with the denominator [VecEncFactDn](VecEncFactDn.md). This serves the same compensation purpose as the integer-ratio keyword [VecEncRatio](VecEncRatio.md).

> **Note:** `VecEncFactNu` was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and parameter attributes before use.

> **Documentation pending:** Frontmatter attributes (access, range, default, etc.) are unconfirmed pending firmware verification.

## See also

- [VecEncFactDn](VecEncFactDn.md) — denominator of the scaling ratio
- [VecEncRatio](VecEncRatio.md) — single-value encoder-resolution compensation
- [VecSpeed](VecSpeed.md) — commanded resultant speed
