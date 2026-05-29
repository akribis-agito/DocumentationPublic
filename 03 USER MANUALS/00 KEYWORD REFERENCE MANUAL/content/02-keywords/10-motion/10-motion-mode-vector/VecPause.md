---
keyword: VecPause
summary: Pauses (1) or resumes (0) vector motion by ramping the resultant speed to/from zero.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 640
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
# VecPause

Pauses (1) or resumes (0) vector motion by ramping the resultant speed to/from zero.

## Overview

`VecPause` temporarily holds a coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) without ending the move. A value of `1` pauses the motion by forcing the commanded resultant speed to 0, so the group decelerates along the path until it stops. A value of `0` continues the motion normally; if previously paused, the group accelerates back up to [VecSpeed](VecSpeed.md) and continues along the same path. Unlike [StopVec](StopVec.md), which terminates the move, `VecPause` lets the same move resume from exactly where it left off.

It is not saved to flash and takes its default value `0` at power-up.

## How it works

Set `VecPause` on the **group master** (the lowest-numbered member axis — see [VecMemberAxes](VecMemberAxes.md)), since the master runs the single path profiler for the whole group. Each control cycle the profiler checks the flag: while it is `1`, the resultant target speed is held at zero and the group reports [VecMotionStat](VecMotionStat.md) = 2 (paused); when it returns to `0`, the target speed is restored to [VecSpeed](VecSpeed.md) and [VecMotionStat](VecMotionStat.md) goes back to 1 (in motion). The acceleration and deceleration along the path follow the configured vector acceleration/deceleration ramps, so the pause and resume are smooth rather than instantaneous.

A pause does not change the target, so all member axes continue to their original endpoints when resumed. If the group is stopped (for example by [StopVec](StopVec.md)) the controller clears `VecPause` back to `0` automatically, because the move is no longer holdable.

## Examples

```text
AVecPause=1          ; on group-master axis A: pause vector motion (decelerate along the path to a stop)
AVecPause=0          ; resume vector motion (accelerate back to VecSpeed)
```

## See also

- [StopVec](StopVec.md) — terminate (rather than pause) vector motion
- [VecSpeed](VecSpeed.md) — speed resumed to after a pause
- [VecMotionStat](VecMotionStat.md) — reports value 2 while paused
- [VecMemberAxes](VecMemberAxes.md) — defines the group and its master axis
