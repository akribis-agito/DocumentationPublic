---
keyword: StallTh
summary: Read-only stepper stall-detection threshold.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 516
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
# StallTh

Read-only stepper stall-detection threshold.

## Overview

`StallTh` is the read-only threshold used by stepper stall detection — the value [StallVal](StallVal.md) is compared against to set [StallStat](StallStat.md). It is influenced by [StallThPcnt](StallThPcnt.md).

> **Documentation pending:** how `StallTh` is derived is not yet documented. Contact Agito for details until this section is completed.

## See also

- [StallThPcnt](StallThPcnt.md) — threshold percentage input
- [StallVal](StallVal.md) — metric compared against this threshold
