---
keyword: JerkMode
summary: Selects the point-to-point motion profiler order (2nd or 3rd order).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 722
attributes:
  access: rw
  scope: axis
  flash: true
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
overrides:
  central-i.v5:
    units: user
    can_code: 567
---
# JerkMode

Selects the point-to-point motion profiler order (2nd or 3rd order).

## Overview

`JerkMode` defines the order of the point-to-point motion profiler, which determines whether jerk (and snap) limiting is applied to a move. It is only used when [MotionMode](MotionMode.md) = 1 or 2 (point-to-point motion). A second-order profile uses [Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md) and [Jerk](../03-kinematics-configuration/Jerk.md); a third-order profile additionally uses [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md) and [JerkInDec](../03-kinematics-configuration/JerkInDec.md). It cannot be changed while the axis is in motion.

## How it works

`JerkMode` is used to define the point-to-point motion profiler's order, as shown below.

| JerkMode | Motion profiler’s order | Related keywords |
|----|----|----|
| 0 | 2 (Infinite jerk) | Speed, Accel, Decel, Jerk |
| 1 | 3 (Infinite snap) | Speed, Accel, Decel, Jerk, JerkInAcc, JerkInDec |

Each control cycle the profiler reads `JerkMode` and selects its trajectory law accordingly: with `JerkMode = 0` it uses the second-order square-root deceleration law, and with `JerkMode = 1` it runs the full jerk profiler. The controller also **overrides** the order to second-order for the duration of a limit/controlled stop, so an emergency-deceleration stop is taken without jerk limitation regardless of `JerkMode`.

Independently of the profiler order, the [Jerk](../03-kinematics-configuration/Jerk.md) keyword sets a moving-average smoothing tail of `2^Jerk` cycles that the profiler flushes at the end of every move (the profile-smoothing tail reported by [MotionStat](../05-motion-status/MotionStat.md) bit 6).

## Examples

```text
AJerkMode=0          ; second-order profile
AJerkMode=1          ; third-order profile
AJerkMode           ; query current value
```

## See also

- [MotionMode](MotionMode.md) — must be 1 or 2 for `JerkMode` to apply
- [Jerk](../03-kinematics-configuration/Jerk.md) — second-order jerk setting
- [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md) — jerk during acceleration (third-order)
- [JerkInDec](../03-kinematics-configuration/JerkInDec.md) — jerk during deceleration (third-order)
