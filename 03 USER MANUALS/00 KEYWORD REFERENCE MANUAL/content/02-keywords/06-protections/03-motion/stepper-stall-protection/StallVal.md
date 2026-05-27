---
keyword: StallVal
summary: Read-only current value of the stepper stall-detection metric.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 511
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# StallVal

Read-only current value of the stepper stall-detection metric.

## Overview

`StallVal` is the read-only, live value of the stepper stall-detection metric — the quantity compared against the threshold ([StallTh](StallTh.md)) to decide [StallStat](StallStat.md).

> **Documentation pending:** the exact quantity `StallVal` represents is not yet documented. Contact Agito for details until this section is completed.

## See also

- [StallTh](StallTh.md) — threshold this value is compared against
- [StallStat](StallStat.md) — resulting stall flag
