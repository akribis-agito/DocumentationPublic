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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# VecEncRatio

Per-axis encoder-resolution compensation ratio, scaled by 1/256 (256 = ratio of 1).

## Overview

`VecEncRatio` is intended to compensate for different encoder resolutions among the axes participating in a coordinated vector move ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), so that the resultant path stays geometrically accurate even when the member axes do not share the same counts-per-unit. It is the single-value form of the same compensation provided by the numerator/denominator pair [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md). It is saved to flash and cannot be modified while in motion.

## How it works

The value is interpreted as a ratio scaled by 1/256: `256` means a ratio of 1 (the default, no scaling), and a larger value gives a proportionally larger ratio — for example `260` means a ratio of 260/256. The range is `256` (ratio of 1) to `25600` (ratio of 100).

> On current firmware this ratio is stored per axis but is not applied to the vector path: the vector move computes each member axis purely from the path geometry, so `VecEncRatio` does not currently affect the resultant motion. Later firmware replaces it with the rational pair [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md), which expresses the same ratio as a numerator over a denominator; that pair is likewise stored (and an internal multiplier is computed from it) but is not yet applied to the path either. Verify behavior against your firmware before relying on vector encoder-resolution compensation.

## Examples

```text
AVecEncRatio=256       ; ratio of 1 on axis A (default, no scaling)
AVecEncRatio=260       ; ratio of 260/256
```

## See also

- [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) — numerator/denominator form of the same ratio
- [VecMemberAxes](VecMemberAxes.md) — axes forming the vector group
- [VecSpeed](VecSpeed.md) — commanded resultant speed
