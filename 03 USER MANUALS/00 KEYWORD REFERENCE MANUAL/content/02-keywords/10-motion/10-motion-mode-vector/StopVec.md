---
keyword: StopVec
summary: Command that stops coordinated vector motion, decelerating all member axes with VecEmrgDec.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 645
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopVec

Command that stops coordinated vector motion, decelerating all member axes with VecEmrgDec.

## Overview

`StopVec` is a command that stops coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). All participating axes (selected by [VecMemberAxes](VecMemberAxes.md)) decelerate together using the emergency deceleration rate [VecEmrgDec](VecEmrgDec.md) and come to rest, keeping the vector path coordinated as it stops. It is an axis-related command function that can be issued at any time, including during motion. `StopVec` is the way to end a vector move before it reaches its programmed endpoint.

## How it works

`StopVec` may be issued on any member axis. The controller finds the group that axis belongs to and, if the group is actively moving or paused, applies the stop to **all** member axes together so the path stays coordinated as it brakes:

1. It records the stop reason on every member axis: [MotionReason](../05-motion-status/MotionReason.md) = 29 ("ended due to StopVec command").
2. It sets the vector-stop request bit on every member axis: the [MotionStat](../05-motion-status/MotionStat.md) vector-stop bit (bit 18, mask `0x00040000`).
3. It switches the group's internal state to "stopping", which makes the path-velocity profiler ramp the path speed down to rest at the emergency rate [VecEmrgDec](VecEmrgDec.md) (rather than the normal [VecDecel](VecDecel.md)).

Because the deceleration is applied to the single path velocity and the geometry still splits it across the axes, the move follows its programmed path while slowing — it does not deviate. When the path velocity reaches zero the in-motion status bits of all member axes are cleared and the move ends. Issuing `StopVec` when the group is not in motion has no effect.

![StopVec timeline showing the vector-stop bit being set, MotionReason latching to 29, and the path braking at VecEmrgDec](stopvec-timeline.svg)

A motor-off or fault on a member axis, or a member axis reaching a software position limit, stops the group by the same mechanism but with different reason codes (see [MotionReason](../05-motion-status/MotionReason.md) codes 30-34). Use [VecPause](VecPause.md) instead if you want to halt the move and later resume it from where it stopped.

## Examples

```text
AStopVec             ; stop the active vector motion (invoke as a command)
```

## See also

- [VecEmrgDec](VecEmrgDec.md) — deceleration rate used to stop
- [VecMotionStat](VecMotionStat.md) — reports the resulting motion state
- [VecPause](VecPause.md) — temporarily pause (vs. stop) vector motion
