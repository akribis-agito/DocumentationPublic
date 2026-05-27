---
keyword: StallThPcnt
summary: Stepper stall threshold as a percentage (10–90%, default 50%).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 512
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
  - 10
  - 90
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallThPcnt

Stepper stall threshold as a percentage (10–90%, default 50%).

## Overview

`StallThPcnt` sets the stepper stall-detection threshold as a percentage (valid 10–90%, default 50%). It scales the effective threshold [StallTh](StallTh.md) used to evaluate the stall metric [StallVal](StallVal.md). A lower percentage makes stall detection more sensitive.

> **Documentation pending:** the exact relationship between this percentage and `StallTh` is not yet documented. Contact Agito for details until this section is completed.

## Examples

```text
AStallThPcnt=50      ; stall threshold at 50%
```

## See also

- [StallTh](StallTh.md) — resulting threshold
- [StallCfg](StallCfg.md) — stall-detection mode
