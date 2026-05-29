---
keyword: VecEmrgDec
summary: Emergency vector deceleration applied to all member axes on a stop or fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 638
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
    default: null
---
# VecEmrgDec

Emergency vector deceleration applied to all member axes on a stop or fault.

## Overview

`VecEmrgDec` sets the emergency deceleration rate, in user units per second squared, applied to all axes participating in vector motion when a member axis reaches a travel limit (a hardware reverse/forward limit switch or a software position limit) during the move. It is typically set higher than the normal [VecDecel](VecDecel.md) to halt the vector move as quickly as possible while keeping the path coordinated. The user-issued [StopVec](StopVec.md) command itself brakes the path at the normal [VecDecel](VecDecel.md); `VecEmrgDec` is reserved for the limit-triggered fault paths. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

A vector move normally decelerates the path velocity at [VecDecel](VecDecel.md). When a limit-triggered emergency stop is raised, the controller sets an internal flag that swaps the deceleration term in the path profiler from `VecDecel` to `VecEmrgDec` for the rest of the move, so the resultant path velocity ramps down to rest at this faster rate while the geometry keeps the member axes coordinated along the path. The braking still acts on the single path velocity, so each member axis decelerates by `VecEmrgDec` scaled by its share of the path.

The emergency rate is selected when a member axis reaches a travel limit during the move: a hardware reverse/forward limit switch ([MotionReason](../05-motion-status/MotionReason.md) = 33) or a software position limit ([MotionReason](../05-motion-status/MotionReason.md) = 34), with 6 / 7 reported for the offending axis itself. A user [StopVec](StopVec.md) does **not** raise this flag — the stop still brakes at [VecDecel](VecDecel.md) (with [MotionReason](../05-motion-status/MotionReason.md) = 29 and the vector-stop bit, [MotionStat](../05-motion-status/MotionStat.md) bit 18 / mask `0x00040000`).

A motor-off or fault on any member axis ends the move immediately rather than ramping at any of these rates.

## Examples

```text
AVecEmrgDec=100000   ; emergency vector deceleration (user units/s^2, default)
AVecEmrgDec         ; read the current value
```

## See also

- [VecDecel](VecDecel.md) — normal (controlled) vector deceleration
- [StopVec](StopVec.md) — command that decelerates using this rate
- [MotionStat](../05-motion-status/MotionStat.md) — vector-stop bit (bit 18)
- [MotionReason](../05-motion-status/MotionReason.md) — stop reason codes 29 / 33 / 34
