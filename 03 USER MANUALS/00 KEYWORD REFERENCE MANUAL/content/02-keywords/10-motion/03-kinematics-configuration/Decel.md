---
keyword: Decel
summary: Deceleration rate for point-to-point motion, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 137
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# Decel

Deceleration rate for point-to-point motion, in user units per second squared.

## Overview

`Decel` defines how quickly the axis ramps down from the commanded [Speed](Speed.md) to rest at the end of a move, and is the rate used by a controlled [Stop](../04-motion-command/Stop.md). It is the counterpart to [Accel](Accel.md) on the deceleration side and is one of the kinematic limits the motion profiler respects. For abrupt stops on fault or abort, the separate [EmrgDec](EmrgDec.md) rate is used instead. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
Decel=200000        ; deceleration (user units/s^2)
Decel?              ; query current deceleration
```

## See also

- [Accel](Accel.md) — acceleration rate at the start of a move
- [Speed](Speed.md) — target velocity that deceleration ramps down from
- [EmrgDec](EmrgDec.md) — emergency deceleration for stop/fault
