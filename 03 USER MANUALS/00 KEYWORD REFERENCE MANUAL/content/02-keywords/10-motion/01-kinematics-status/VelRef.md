---
keyword: VelRef
summary: Velocity-loop reference/input (position-controller output plus velocity reference).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 25
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# VelRef

Velocity-loop reference/input (position-controller output plus velocity reference).

## Overview

`VelRef` is the velocity-loop reference/input, in main user units per second. It is generally the sum of the position-controller output and the (scaled) velocity feed-forward, and it is the input to the velocity loop.

`VelRef` must not be confused with the velocity reference [dPosRef](dPosRef.md): `dPosRef` is the filtered derivative of the position reference, whereas `VelRef` also includes the position-controller output. The velocity error [VelErr](VelErr.md) is computed from `VelRef`. Its frontmatter range is narrower than ±2³¹ because it is hard-limited to ±[MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) (see below).

## How it works

`VelRef` is built only while the motor is on, commutation is done, the axis is not in simulation and the amplifier is not a position-drive. The construction proceeds in stages.

### 1. Position-controller output + velocity feed-forward

The base value is the position gain acting on [PosErr](PosErr.md) plus a velocity feed-forward term derived from [dPosRef](dPosRef.md):

$$
VelRef = PosErr \times PosGain + \frac{dPosRef \times VelTrackFact}{1024}
$$

In gantry mode the gantry position gain is used instead of [PosGain](../../11-control-tuning/03-position-control/PosGain.md). The product is computed in 64-bit and then clamped into the 32-bit range before being stored.

### 2. Dual-loop and operation-mode overrides

| Stage | Effect |
|-------|--------|
| Dual-loop on ([DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1) | `VelRef` is scaled by a command gain derived from [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) |
| Velocity operation mode | `VelRef` is replaced by the filtered analog velocity command |
| FIFO position tracking (e.g. EtherCAT CSP), in motion | A user position-tracking offset is added |

### 3. Injection

If [InjectPoint](../../13-injection/InjectPoint.md) targets the velocity reference, a test signal ([InjectType](../../13-injection/InjectType.md)) is either substituted for or added to `VelRef`:

| Inject type | Action on `VelRef` |
|-------------|--------------------|
| Sine direct | Replaces `VelRef` with an interpolated sine |
| Sine add | Adds the sine to the position-loop output |
| Square direct / add | Replaces / adds a square wave |
| PRBS direct / add | Replaces / adds a pseudo-random binary sequence (used for system identification) |

### 4. Saturation to MaxVel

Finally `VelRef` is hard-limited to ±[MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md). On saturation the velocity-saturation bit of [StatReg](../../07-status-and-faults/StatReg.md) (bit 23) is set, along with the general "any saturation" flag. This clamp is why `VelRef` reports within ±1.3e9 rather than the full 32-bit range.

## Examples

```text
AVelRef             ; read the velocity-loop reference
```

## Changes between versions

In **v5 (central-i)** `VelRef` is a 64-bit value limited to ±`MaxVel`, and the position-controller output that feeds it includes an optional **position-integral** term ([PosKi](../../11-control-tuning/03-position-control/PosKi.md)) and a position-error filter in addition to the proportional gain — so v5 `VelRef` is a PI(+filter)+FFW output, whereas v4 is P+FFW. The dual-loop, operation-mode, FIFO-offset, injection and `MaxVel`-saturation stages are unchanged. **v5 is central-i only.**

## See also

- [dPosRef](dPosRef.md) — velocity feed-forward source (a different signal)
- [VelErr](VelErr.md) — velocity error (`VelRef − Vel[1]`)
- [Vel](Vel.md) — feedback velocity array
- [PosErr](PosErr.md) / [PosGain](../../11-control-tuning/03-position-control/PosGain.md) — position-controller inputs
- [VelTrackFact](../../11-control-tuning/04-velocity-control/VelTrackFact.md) — velocity feed-forward gain
- [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) — saturation limit
- [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — dual-loop command scaling
