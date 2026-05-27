---
keyword: StallCnst
summary: Tuning constants for stepper stall detection (3-element array).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 515
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallCnst

Tuning constants for stepper stall detection.

## Overview

`StallCnst` is an array of constants that tune the stepper stall-detection algorithm selected by [StallCfg](StallCfg.md).

> **Documentation pending:** the meaning of each element is not yet documented. Contact Agito for details until this section is completed.

## See also

- [StallCfg](StallCfg.md) — stall-detection mode
- [StallThPcnt](StallThPcnt.md) — stall threshold percentage
