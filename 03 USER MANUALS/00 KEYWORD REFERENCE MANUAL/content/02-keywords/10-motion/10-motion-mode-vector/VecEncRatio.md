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

`VecEncRatio` is used to compensate for different encoder resolutions among the axes participating in a vector move: each axis is scaled according to its resolution so the coordinated path stays accurate. It is an alternative to the numerator/denominator pair [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md). It is saved to flash and cannot be modified while in motion.

## How it works

The actual ratio inside the controller is scaled by 1/256. So `VecEncRatio = 256` means a ratio of 1, and a value of `260` means a ratio of 260/256. The range is `256` (ratio of 1) to `25600` (ratio of 100).

> **Documentation pending:** Detailed usage guidance was marked TBD during implementation. The implementation is intended to avoid accumulated position errors and to reach the final target position accurately; confirm against current firmware before relying on specific behavior.

## Examples

```text
VecEncRatio=256     ; ratio of 1 (default)
VecEncRatio=260     ; ratio of 260/256
```

## See also

- [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) — numerator/denominator form of the ratio
- [VecSpeed](VecSpeed.md) — commanded resultant speed
