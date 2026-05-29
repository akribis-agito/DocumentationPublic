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

### Deceleration trigger (mode 1)

Unlike the second-order square-root deceleration law, the third-order profiler (`JerkMode = 1`) decides when to start braking by predicting the **distance** needed to bring the axis to rest under the jerk-limited deceleration ramp. Each cycle it computes the deceleration distance for a trapezoidal sub-profile (jerk-up to `Decel`, constant `Decel`, jerk-down to zero, using [JerkInDec](../03-kinematics-configuration/JerkInDec.md)); for short moves that cannot reach the full `Decel`, it falls back to a triangular sub-profile (jerk-up then jerk-down with no constant-deceleration phase). The profiler stays in the acceleration/cruise phase while this predicted distance is still less than the distance remaining to the target, and switches into deceleration on the first cycle where it meets or exceeds the remaining distance.

Because the switch generally falls partway through a control cycle, the profiler refines the exact within-cycle switching instant by linear interpolation of the position-to-target error between the acceleration-phase and deceleration-phase candidates, iterating a few times until the predicted landing position is within about 0.1 count of the target. This is what lets the jerk-limited move stop on target despite the discrete update rate.

### Edge cases

- **Motor off:** the value is held; it is read on the next `Begin`.
- **Out-of-range write:** the parameter system rejects values outside `0`–`1`.
- **Simulation mode (`MotorType` = 5):** the profiler runs identically in simulation.
- **ModRev wrap:** unrelated to `JerkMode`; both profiler orders handle wrap the same way.
- **Active fault:** the axis is disabled; on re-enable and the next `Begin`, the current `JerkMode` is read again.
- **Hardware/software limit stop or controlled-stop-by-input:** `JerkMode` is forced to `0` (second-order) internally for the duration of the stop ramp, regardless of the user setting — these emergency decelerations always use the square-root law. An ordinary [Stop](../04-motion-command/Stop.md) command is **not** in this group: a plain `Stop` decelerates with the configured `JerkMode` and the normal [Decel](../03-kinematics-configuration/Decel.md).
- **Other motion modes:** `JerkMode` is ignored outside PTP (1) and repetitive PTP (2); jog, gear, ECAM, PD, CNC, vector, joystick, FIFO, spline-buffer and slave each use their own trajectory law.
- **Cannot change in motion:** writes are rejected while [MotionStat](../05-motion-status/MotionStat.md) is non-zero.

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
