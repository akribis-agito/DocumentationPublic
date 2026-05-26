---
keyword: StallStat
summary: Read-only stepper stall status flag (0 = no stall, 1 = stalled).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 514
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallStat

Read-only stepper stall status flag (0 = no stall, 1 = stalled).

## Overview

`StallStat` is a read-only flag reporting the stepper stall-detection result: `0` = no stall detected, `1` = stall detected. It is the status output of the stall-protection group configured by [StallCfg](StallCfg.md).

> **Documentation pending:** the precise detection conditions are not yet documented. Contact Agito for details until this section is completed.

## See also

- [StallCfg](StallCfg.md) — stall-detection mode
- [StallVal](StallVal.md) / [StallTh](StallTh.md) — stall metric and threshold
