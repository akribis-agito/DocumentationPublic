---
keyword: VecEncRatio
summary: Per-axis encoder-resolution compensation ratio, scaled by 1/256 (256 = ratio of 1).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 632
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
  - 256
  - 25600
  default: 256
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecEncRatio

Per-axis encoder-resolution compensation ratio, scaled by 1/256 (256 = ratio of 1).

## Overview

`VecEncRatio` is intended to compensate for different encoder resolutions among the axes participating in a coordinated vector move ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), so that the resultant path stays geometrically accurate even when the member axes do not share the same counts-per-unit. It is the single-value form of the same compensation provided by the numerator/denominator pair [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md). It is saved to flash and cannot be modified while in motion.

## How it works

The value is interpreted as a ratio scaled by 1/256: `256` means a ratio of 1 (the default, no scaling), and a larger value gives a proportionally larger ratio — for example `260` means a ratio of 260/256. The range is `256` (ratio of 1) to `25600` (ratio of 100).

> **Use the factor pair instead.** On current firmware the active per-axis vector encoder scaling is applied through the rational pair [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md), which expresses the same ratio as a numerator over a denominator. Configure those two keywords for vector encoder compensation. `VecEncRatio` is retained for compatibility; prefer the factor pair for new configurations and verify behavior against your firmware before relying on `VecEncRatio` alone.

## Examples

```text
AVecEncRatio[1]=256    ; ratio of 1 (default, no scaling)
AVecEncRatio[1]=260    ; ratio of 260/256
```

## See also

- [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) — numerator/denominator form actually applied to the vector path
- [VecMemberAxes](VecMemberAxes.md) — axes forming the vector group
- [VecSpeed](VecSpeed.md) — commanded resultant speed
