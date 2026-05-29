---
keyword: MaxPosErr
summary: Maximum closed-loop position error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 84
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
  - 80000000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPosErr

Maximum closed-loop position error; exceeding it disables the axis.

## Overview

`MaxPosErr` is the maximum allowable absolute position error ([PosErr](../../../10-motion/01-kinematics-status/PosErr.md)) in closed-loop operation. It is the primary "following error" protection: if `|PosErr|` exceeds the active threshold, the axis is disabled in the same control sample and a fault is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md). For the open-loop equivalent used during injection/open-loop, see [MaxPosErrOL](MaxPosErrOL.md).

## How it works

The check runs every control sample in the position loop:

```text
if |PosErr| > active threshold
    turn the axis off and log the fault
```

![Following-error trip threshold: the absolute error rises until it crosses the active limit; on that sample the axis is disabled and a ConFlt code is logged. The open-loop limits are higher to tolerate the larger natural error during injection or open-loop operation.](following-error-trip.svg)

Key points:

- The threshold actually used is switched between `MaxPosErr` (closed loop) and [MaxPosErrOL](MaxPosErrOL.md) (open loop / injection) depending on the loop state. In normal closed-loop operation the closed-loop threshold applies, so a violation records [ConFlt](../../../07-status-and-faults/ConFlt.md) fault code 1020 (position error too high). In open loop the open-loop threshold applies and the same condition instead records fault code 1055 (open-loop position error too high).
- The position error is forced to `0` (so this protection never trips) for an open-loop stepper, and whenever the axis is not in a position-control / force-over-PIV mode. The protection is therefore effective only when a position loop is actually closed.
- On a violation the axis is turned off immediately, and the fault's configured stop behaviour applies.

## Examples

```text
AMaxPosErr[1]=5000    ; max following error (user units)
AMaxPosErr[1]         ; read back the limit
```

### Walk-through: tune and verify a following-error trip

Set the limit close to the largest tracking error the application should ever see, then exercise the worst-case move and confirm the trip behaviour before deploying:

```text
AMaxPosErr[1]=2000    ; chosen well above the expected steady-state |PosErr|
APosErr               ; sample the live error in normal operation; should stay << MaxPosErr
```

Run the worst-case profile (highest `Speed`/`Accel`, heaviest load) and re-sample `APosErr` at several points during the move. If the headroom is too thin, either raise the position gain (so the lag shrinks) or raise `MaxPosErr`. To confirm the trip path itself, command a move into a mechanical obstruction:

```text
AConFlt                       ; expect 1020 (closed-loop position error too high)
AMotionReason                 ; expect 8 (motor disabled)
APosErr                       ; last value before the trip; will be > MaxPosErr
```

The axis is disabled in the same control sample the threshold is crossed, so there is no ramp; if a soft stop is needed instead, leave headroom and rely on a software [FwdPLim](../position-limit-protection/FwdPLim.md)/[RevPLim](../position-limit-protection/RevPLim.md) to brake first.

## See also

- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — the measured position error this limit acts on
- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit (the alternate threshold)
- [MaxVelErr](MaxVelErr.md) — companion velocity-following-error limit
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1020 (closed loop) / 1055 (open loop)
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason 8 (motor disabled) when this trip fires
