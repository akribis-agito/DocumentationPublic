---
keyword: VelErr
summary: Velocity error (reference minus feedback), used for control and protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 19
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VelErr

Velocity error (reference minus feedback), used for control and protection.

## Overview

`VelErr` reports the error between the velocity reference and the velocity feedback, in main user units per second. It is the velocity-loop counterpart of the position error [PosErr](PosErr.md) and is the signal the velocity PI controller (and its high-velocity-error protection) act on.

`VelErr` is only reported when the axis is enabled and in a position or velocity operation mode (or force-over-PIV) and not open-loop; otherwise the firmware forces it to `0`.

## How it works

`VelErr` is computed each control cycle as the (saturated) velocity reference minus the velocity-loop feedback `Vel[1]`, in `AG300_CTL01ControlLoops.c:663`:

1. Under individual (non-gantry) mode:

$$
VelErr = VelRef - Vel\lbrack 1\rbrack
$$

2. Under gantry mode:

$$
VelErr = VelRef - GantryVel
$$

Because the subtrahend is [Vel](Vel.md)`[1]`, what `VelErr` measures against changes with the loop configuration: `Vel[1]` is the main-encoder velocity normally, the (scaled) auxiliary velocity under dual-loop, an analog tacho under analog-tacho dual-loop, or the gantry velocity in gantry mode.

### When it is forced to zero

`VelErr` is set to `0` (`AG300_CTL01ControlLoops.c:666`–`668`, `2600`) for stepper open-loop motors (`MotorType` = 6) and whenever the [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) is neither position nor velocity control and force-over-PIV is off. Note the firmware still **computes** `VelErr` even in current operation mode (it is a true error used to preload the velocity-PI integral so the current command does not jump when switching back to position/velocity control).

### High velocity-error protection

After computing `VelErr` the firmware checks `labs(VelErr) > glMaxVelErrInternal` (the internal scaled form of [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.md)) while in position/velocity/force-PIV mode; on exceedance it disables the axis and logs `CON_FLT_HIGH_VEL_ERR` (or the open-loop variant). This check is skipped for analog-velocity-command amplifiers (`AG300_CTL01ControlLoops.c:670`–`683`). Otherwise `VelErr` drives the velocity PI (gain × error, accumulated into the velocity integral) — `:694`–`711`.

## Examples

```text
AVelErr             ; read the current velocity error
```

## Changes between versions

In **v5 (central-i)** `VelErr` is 64-bit (`gllVelErr = gllVelRef − gllVel[1]`, `develop:CommonC/AG300_CTL01ControlLoops.c:691`) and is compared against a scaled 64-bit `MaxVelErr`; the zeroing conditions and the PI usage are otherwise the same. `VelErr` is reported as a 32-bit value in v5 (no range override). **v5 is central-i only.**

## See also

- [VelRef](VelRef.md) — velocity-loop reference (the minuend)
- [Vel](Vel.md) — feedback velocity array (`Vel[1]` is the subtrahend in non-gantry mode)
- [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md) — feedback used in gantry mode
- [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.md) — error threshold that disables the axis
- [PosErr](PosErr.md) — position error counterpart
