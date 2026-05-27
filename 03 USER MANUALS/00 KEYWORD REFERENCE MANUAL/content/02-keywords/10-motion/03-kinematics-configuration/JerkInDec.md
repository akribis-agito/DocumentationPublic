---
keyword: JerkInDec
summary: Jerk applied during the deceleration phase of a third-order (infinite-snap) profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 721
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
  - 100
  - 1000000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# JerkInDec

Jerk applied during the deceleration phase of a third-order (infinite-snap) profile.

## Overview

`JerkInDec` sets the jerk applied during the deceleration phase of a third-order (infinite-snap) motion profile, used when [JerkMode](../02-motion-configuration/JerkMode.md) = 1. It controls the rate at which deceleration itself ramps up and down during the deceleration segment, smoothing the [Decel](Decel.md) ramp. Its acceleration-phase counterpart is [JerkInAcc](JerkInAcc.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

> **Documentation pending:** `JerkInDec` was not found in the firmware parameter table during review; confirm availability and parameter attributes before use.

## Examples

```text
AJerkInDec=2000000   ; jerk during deceleration phase
AJerkInDec          ; query current value
```

## See also

- [JerkInAcc](JerkInAcc.md) — jerk during the acceleration phase
- [Jerk](Jerk.md) — second-order jerk setting
- [JerkMode](../02-motion-configuration/JerkMode.md) — selects the profiler order
