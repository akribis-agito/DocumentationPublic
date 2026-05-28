---
keyword: MaxVelErr
summary: Maximum closed-loop velocity error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 85
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
  - 0
  - 1300000000
  default: 32768
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MaxVelErr

Maximum closed-loop velocity error; exceeding it disables the axis.

## Overview

`MaxVelErr` is the maximum allowable absolute velocity error ([VelErr](../../../10-motion/01-kinematics-status/VelErr.md)) in closed-loop operation. If `|VelErr|` exceeds the active threshold, the axis is disabled in the same control sample and a fault is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md). For the open-loop equivalent used during injection/open-loop, see [MaxVelErrOL](MaxVelErrOL.md).

## How it works

The check runs every control sample in the velocity loop:

```text
if (mode is position-control, velocity-control, or force-over-PIV)
   and |VelErr| > active threshold
    turn the axis off and log the fault   (skipped for velocity-command amplifiers)
```

![Following-error trip threshold: the absolute error rises until it crosses the active limit; on that sample the axis is disabled and a ConFlt code is logged. The open-loop limits are higher to tolerate the larger natural error during injection or open-loop operation.](following-error-trip.svg)

Key points:

- The threshold actually used is switched between `MaxVelErr` (closed loop) and [MaxVelErrOL](MaxVelErrOL.md) (open loop / injection) depending on the loop state. In closed loop, a violation records [ConFlt](../../../07-status-and-faults/ConFlt.md) fault code 1021 (velocity error too high); in open loop, it records fault code 1056 (open-loop velocity error too high).
- The protection is active **only** in Position-control, Velocity-control, or force-over-PIV operation. In other modes the velocity error is forced to `0`, so the check cannot trip.
- It is **bypassed for velocity-command (analog) amplifiers**, because the drive closes its own velocity loop.
- On a violation the axis is turned off immediately.

## Examples

```text
AMaxVelErr[1]=100000   ; max velocity error (user units/s)
AMaxVelErr[1]          ; read back the limit
```

## See also

- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — the measured velocity error this limit acts on
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit (the alternate threshold)
- [MaxPosErr](MaxPosErr.md) — companion position-following-error limit
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1021 (closed loop) / 1056 (open loop)
