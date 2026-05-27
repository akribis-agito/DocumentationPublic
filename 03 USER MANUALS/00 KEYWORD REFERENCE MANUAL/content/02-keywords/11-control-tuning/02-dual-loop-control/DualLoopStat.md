---
keyword: DualLoopStat
availability:
  standalone: []
  central-i:
  - v5
can_code: 727
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualLoopStat

Read-only status of the active dual-loop control structure.

## Overview

`DualLoopStat` reports which control structure is currently active. It reflects the run-time result of [DualLoopOn](DualLoopOn.md), [DualEncSwapOn](DualEncSwapOn.md), [DualEncMode](DualEncMode.md) and [DualEncRange](DualEncRange.md) — including range-limited switching, which can change the active structure during motion — so it may differ from the configured `DualLoopOn` value.

| `DualLoopStat` | Description |
|---|---|
| 0 | Default control is active (both loops on the main encoder). |
| 1 | Pseudo dual-loop control is active (position loop sourced from the auxiliary encoder, scaled to load units). |
| 2 | Dual-loop control is active (position loop on main/load encoder, velocity loop on motor feedback). |

## How it works

With dual-loop disabled, `DualLoopStat` reads `0`. With dual-loop enabled and pseudo dual-loop off, it reads `2`. With pseudo dual-loop on ([DualEncSwapOn](DualEncSwapOn.md) = 1) it reads `1`.

When range-limited switching is configured ([DualEncMode](DualEncMode.md) = 1), the controller switches between pseudo dual-loop and full dual-loop according to whether the motor feedback is inside the [DualEncRange](DualEncRange.md) window: inside the range `DualLoopStat` becomes `2`, outside it becomes `1`. Reading `DualLoopStat` therefore shows the structure in effect at that instant.

## Examples

```text
ADualLoopStat        ; read the active dual-loop control structure
```

## See also

- [DualLoopOn](DualLoopOn.md) — configure dual-loop control
- [DualEncSwapOn](DualEncSwapOn.md) — pseudo dual-loop switch
- [DualEncMode](DualEncMode.md) / [DualEncRange](DualEncRange.md) — range-limited switching that this status reflects
