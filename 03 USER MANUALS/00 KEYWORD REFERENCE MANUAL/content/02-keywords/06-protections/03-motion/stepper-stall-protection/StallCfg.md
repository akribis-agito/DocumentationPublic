---
keyword: StallCfg
summary: Configures the stepper stall-detection mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 513
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallCfg

Configures the stepper stall-detection mode.

## Overview

`StallCfg` selects the stepper stall-detection mode (one of three settings, range 0–2). It is part of the stepper stall-protection group together with [StallThPcnt](StallThPcnt.md), [StallCnst](StallCnst.md), and the read-only status keywords [StallStat](StallStat.md), [StallVal](StallVal.md), and [StallTh](StallTh.md).

> **Documentation pending:** the meaning of each mode value is not yet documented. Contact Agito for details until this section is completed.

## See also

- [StallStat](StallStat.md) — stall status
- [StallThPcnt](StallThPcnt.md) — stall threshold (percent)
- [StallCnst](StallCnst.md) — stall-detection constants
