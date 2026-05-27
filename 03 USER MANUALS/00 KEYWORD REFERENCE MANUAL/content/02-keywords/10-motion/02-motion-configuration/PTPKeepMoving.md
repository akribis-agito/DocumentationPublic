---
keyword: PTPKeepMoving
summary: Lets a new Begin blend into the existing move instead of stopping first.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 625
attributes:
  access: rw
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
# PTPKeepMoving

Lets a new `Begin` blend into the existing move instead of stopping first.

## Overview

`PTPKeepMoving` controls what happens when a new [Begin](../04-motion-command/Begin.md) command is issued before the previous point-to-point move has completed. When set to `1`, the axis blends smoothly into the new target ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) without first stopping, which is useful for on-the-fly retargeting. When `0`, a new `Begin` is only accepted after the current move finishes. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## Examples

```text
APTPKeepMoving=1     ; blend into a new target without stopping
APTPKeepMoving=0     ; require the move to complete first
APTPKeepMoving      ; query state
```

## See also

- [Begin](../04-motion-command/Begin.md) — starts (or retargets) the move
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — absolute target position
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — relative target position
