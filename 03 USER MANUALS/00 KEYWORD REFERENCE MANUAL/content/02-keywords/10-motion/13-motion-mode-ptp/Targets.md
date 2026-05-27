---
keyword: Targets
summary: Array of target positions (user units) for multi-target point-to-point motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 376
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# Targets

Array of target positions (user units) for multi-target point-to-point motion.

## Overview

`Targets` stores a sequence of target positions, in user units, for multi-target point-to-point motion. The controller moves through the array entries in order when executing a multi-segment PTP move, allowing several destinations to be queued instead of a single [AbsTrgt](AbsTrgt.md) or [RelTrgt](RelTrgt.md). It is saved to flash and can be changed at any time.

## Examples

```text
ATargets[1]=10000    ; first target position
ATargets[2]=20000    ; second target position
```

## See also

- [AbsTrgt](AbsTrgt.md) — single absolute target position
- [RelTrgt](RelTrgt.md) — single relative target distance
- [Begin](../04-motion-command/Begin.md) — start the PTP move
