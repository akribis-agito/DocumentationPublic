---
keyword: VecMotionStat
summary: Read-only enumerated value reporting the current vector-motion state (0 not in motion, 1 in motion, 2 paused, 3 stopping).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 641
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecMotionStat

Read-only enumerated value reporting the current vector-motion state of the axis.

## Overview

`VecMotionStat` is a read-only parameter that reports the current state of the coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). It lets a host program follow the progress of a vector move and detect when it has paused, started stopping, or finished. It is an axis-related status variable that is not saved to flash.

`VecMotionStat` is maintained on the **group master** (the lowest-numbered member axis — see [VecMemberAxes](VecMemberAxes.md)). The master runs the single path profiler that drives all members, so read `VecMotionStat` on the master to monitor the whole group.

## How it works

Although the keyword can hold any 32-bit value, in practice it reports one of four enumerated states (it is a single value, not a bit mask):

| Value | State | Meaning |
|----|----|----|
| 0 | Not in motion | No vector move is running on this group (idle, or the move has finished, been stopped, or been aborted). |
| 1 | In motion | A vector move is actively running along the path. |
| 2 | Paused | The move is held by [VecPause](VecPause.md) = 1; the resultant speed has been ramped to zero but the move has not ended. |
| 3 | Stopping | A stop has been requested (for example by [StopVec](StopVec.md), a `Stop`, or a controlled stop); the resultant speed is ramping to zero, after which the value returns to 0. |

Typical progression of a normal move: `0` → `1` → (briefly `3` while ramping to zero on stop) → `0`. A paused move shows `1` → `2` → `1` when resumed.

## Examples

```text
AVecMotionStat       ; read the current vector-group state (read on the master axis)
```

To wait for a vector move to complete, poll `VecMotionStat` on the master axis until it reads `0`.

## See also

- [VecPause](VecPause.md) — sets the group into the paused state (value 2) and back
- [StopVec](StopVec.md) — requests the stopping state (value 3), then back to 0
- [VecMemberAxes](VecMemberAxes.md) — defines the group and its master axis
- [VecSpeed](VecSpeed.md) — commanded resultant speed
