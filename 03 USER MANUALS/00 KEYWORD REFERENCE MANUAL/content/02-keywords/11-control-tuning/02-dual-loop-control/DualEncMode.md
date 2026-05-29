---
keyword: DualEncMode
availability:
  standalone: []
  central-i:
  - v5
can_code: 725
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# DualEncMode

Activates range-limited dual-loop control.

## Overview

`DualEncMode` selects whether pseudo dual-loop is used everywhere, or only outside a defined position range. It is only used when [DualLoopOn](DualLoopOn.md) = 1 and [DualEncSwapOn](DualEncSwapOn.md) = 1.

| `DualEncMode` | Behaviour |
|---|---|
| 0 | Pseudo dual-loop control is always used, regardless of position. |
| 1 | True dual-loop control is used while the motor feedback is inside the range defined by [DualEncRange](DualEncRange.md); pseudo dual-loop control is used outside that range. |

## How it works

When `DualEncMode = 1`, each control cycle the controller compares the motor (auxiliary) feedback [AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md) against the lower and upper bounds in [DualEncRange](DualEncRange.md):

- **Inside the range** — true dual-loop is active: the position loop closes on the load feedback. [DualLoopStat](DualLoopStat.md) reads `2`.
- **Outside the range** — pseudo dual-loop is active: the position loop is sourced from the auxiliary encoder scaled to load units (see [DualEncSwapOn](DualEncSwapOn.md)). [DualLoopStat](DualLoopStat.md) reads `1`.

A position offset is maintained across the switch so the transition does not produce a position step.

`DualEncMode` is not retained through a power cycle: it reverts to its default `0` (pseudo dual-loop everywhere) at power-up, so range-limited switching must be re-armed each session. It can be changed with the motor on, but not while the axis is in motion. In contrast, [DualEncRange](DualEncRange.md) is retained and can be adjusted even during motion.

![True dual-loop runs while AuxPos lies between DualEncRange[1] and DualEncRange[2]; pseudo dual-loop runs outside that window](dual-enc-range-switch.svg)

## Examples

```text
ADualEncMode=1       ; use true dual-loop only within DualEncRange
ADualEncRange[1]=-100000
ADualEncRange[2]=100000
```

## See also

- [DualEncRange](DualEncRange.md) — the motor-feedback range that bounds true dual-loop
- [DualEncSwapOn](DualEncSwapOn.md) — pseudo dual-loop switch (required = 1)
- [DualLoopOn](DualLoopOn.md) — enable dual-loop control (required = 1)
- [DualLoopStat](DualLoopStat.md) — reports which structure is active at the current position
