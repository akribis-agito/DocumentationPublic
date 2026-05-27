---
keyword: VecMotionStat
summary: Read-only bit-field reporting the current vector-motion state of the axis.
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

Read-only bit-field reporting the current vector-motion state of the axis.

## Overview

`VecMotionStat` is a read-only parameter that reports the current status of vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) for the axis. The bit-field indicates whether the axis is actively executing a vector move, waiting for synchronisation, or idle, which lets a host program monitor progress and detect when a coordinated move has completed or been stopped. It is an axis-related status variable that is not saved to flash.

## Examples

```text
AVecMotionStat      ; read the current vector-motion state bit-field
```

## See also

- [StopVec](StopVec.md) — command that ends vector motion
- [VecPause](VecPause.md) — pause/resume vector motion
- [VecSpeed](VecSpeed.md) — commanded resultant speed
