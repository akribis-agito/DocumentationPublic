---
keyword: JerkInAcc
summary: Jerk applied during the acceleration phase of a third-order (infinite-snap) profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 720
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
overrides:
  central-i.v5:
    data_type: float32
    units: user
    range: null
    default: null
    can_code: 565
---
# JerkInAcc

Jerk applied during the acceleration phase of a third-order (infinite-snap) profile.

## Overview

`JerkInAcc` sets the jerk applied during the acceleration phase of a third-order (infinite-snap) motion profile, used when [JerkMode](../02-motion-configuration/JerkMode.md) = 1. It controls the rate at which acceleration itself ramps up and down during the acceleration segment, smoothing the [Accel](Accel.md) ramp. Its deceleration-phase counterpart is [JerkInDec](JerkInDec.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

> **Documentation pending:** `JerkInAcc` was not found in the firmware parameter table during review; confirm availability and parameter attributes before use.

## Examples

```text
AJerkInAcc=2000000   ; jerk during acceleration phase
AJerkInAcc          ; query current value
```

## See also

- [JerkInDec](JerkInDec.md) — jerk during the deceleration phase
- [Jerk](Jerk.md) — second-order jerk setting
- [JerkMode](../02-motion-configuration/JerkMode.md) — selects the profiler order
