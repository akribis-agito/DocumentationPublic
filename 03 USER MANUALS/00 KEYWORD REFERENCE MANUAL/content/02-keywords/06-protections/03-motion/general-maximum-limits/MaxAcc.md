---
keyword: MaxAcc
summary: Maximum allowable acceleration/deceleration, checked before a motion starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 81
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    access: rw
    data_type: float32
    ok_in_motion: true
    ok_motor_on: true
    units: user
    range:
    - 100.0
    - 686700000000.0
    default: 10000000
    implemented: final
---
# MaxAcc

Maximum allowable acceleration/deceleration, checked before a motion starts.

## Overview

`MaxAcc` is intended as the maximum allowable acceleration/deceleration. Its behaviour differs sharply between firmware variants.

## How it works

On **standalone / v4**, `MaxAcc` is **not implemented as an enforced limit**. The keyword table marks it `implemented: partial` with access flags of `0` (not user-writable); the stored value is never read by the profiler, control loops, or command validation. In other words, setting it has no effect on this variant. Per-axis acceleration limiting for coordinated (CNC) motion is handled by a separate CNC mechanism, not by this keyword.

> Honest note: the frontmatter for this keyword reflects this — `implemented: partial` and `access: 0` on standalone/v4. Do not rely on `MaxAcc` to clamp or reject motions on these variants.

## Changes between versions

On **central-i v5**, `MaxAcc` becomes a writable, enforced limit that is checked when a motion starts. If the commanded acceleration or deceleration of the motion would exceed `MaxAcc`, the controller refuses to begin the move and reports a start-of-motion error (mirroring how [MaxVel](MaxVel.md) gates the commanded Speed). This start-of-motion check applies to point-to-point and jog-style profiled moves; it does not apply to indirect modes (gear, pulse-and-direction, eCam, joystick, CNC), where the acceleration/deceleration is driven by external inputs or a master and is not governed by `MaxAcc`. There is no runtime acceleration clamp or trip — `MaxAcc` only gates the start of a move.

## Examples

```text
AMaxAcc[1]=2000000    ; central-i v5: max accel/decel (user units). No effect on standalone/v4.
AMaxAcc[1]            ; read back
```

## See also

- [MaxVel](MaxVel.md) — velocity limit (saturation + overspeed trip)
