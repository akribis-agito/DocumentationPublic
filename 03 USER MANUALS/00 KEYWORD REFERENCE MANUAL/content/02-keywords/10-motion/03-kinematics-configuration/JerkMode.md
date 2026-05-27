---
summary: Selects the point-to-point motion profiler order; see JerkMode in motion configuration.
---
# JerkMode

Selects the point-to-point motion profiler order; see `JerkMode` in motion configuration.

## Overview

`JerkMode` selects the order of the motion profiler for point-to-point moves. The full description and table of values is maintained with the primary entry, [JerkMode](../02-motion-configuration/JerkMode.md), in the motion-configuration section.

The value chooses which profiler runs each control cycle:

| `JerkMode` | Profiler | Jerk parameter used |
|------------|----------|----------------------|
| 0 | Second-order trapezoid + moving-average smoothing | [Jerk](Jerk.md) (boxcar window 2^Jerk cycles) |
| 1 | Third-order structured (double-S) profiler | [JerkInAcc](JerkInAcc.md) / [JerkInDec](JerkInDec.md) |

Note that an emergency, limit-switch or controlled-stop halt overrides this selection: the controller forces the second-order (mode 0) behavior for that stop and brakes with [EmrgDec](EmrgDec.md) regardless of the configured `JerkMode`. `JerkMode` cannot be changed while the axis is in motion.

## See also

- [JerkMode](../02-motion-configuration/JerkMode.md) — primary entry with the full value table
- [Jerk](Jerk.md) — second-order jerk setting (mode 0)
- [JerkInAcc](JerkInAcc.md) — jerk during the acceleration phase (mode 1)
- [JerkInDec](JerkInDec.md) — jerk during the deceleration phase (mode 1)
- [EmrgDec](EmrgDec.md) — emergency stops force mode 0 regardless of this setting
