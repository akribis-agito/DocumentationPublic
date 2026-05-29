---
keyword: PosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 714
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosKi

Integral gain of the position loop (central-i v5) — accumulates the scaled position-controller output to add an integral term to the velocity command.

## Overview

`PosKi` is the integral gain of the outer (position) loop. It turns the position controller into a PI controller: where [PosGain](PosGain.md) alone provides a proportional command, `PosKi` accumulates that proportional output over time and adds the accumulated value to the velocity-loop reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md). This allows the position loop to drive steady-state position error toward zero.

`PosKi` is available on **central-i v5 only**. It is an array, so it can take part in gain scheduling; without scheduling the first element `PosKi[1]` is used. See [ScheduleMode](../01-general-keywords/ScheduleMode.md).

## How it works

Each control cycle the (filtered) position error is multiplied by [PosGain](PosGain.md) to form the proportional term. `PosKi` then multiplies that proportional term and the result is added into a running position integral. The proportional term plus the position integral, together with the velocity feed-forward, form the velocity-loop reference:

$$
\text{VelRef} = \left( \text{PosErr} \cdot \text{PosGain} \right) + \int \left( \text{PosErr} \cdot \text{PosGain} \cdot \text{PosKi} \right) \, dt + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

- **What it multiplies:** the position-controller proportional output. The (optionally filtered, see [PosFiltOn](PosFiltOn.md) index 2) position error is multiplied by [PosGain](PosGain.md) to form the proportional term, which `PosKi` then integrates — so `PosKi` multiplies that product (`PosErr_filt × PosGain`) before it enters the integral accumulator.
- **Where it sums:** the accumulated integral is added to the proportional term and the velocity feed-forward to build [VelRef](../../10-motion/01-kinematics-status/VelRef.md).
- **Anti-windup:** the integral saturation value is controlled internally. The position integral increment is gated by all three cascade anti-windup conditions. It is held for a cycle if the velocity reference is clamped at [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) with the position error pushing further into the clamp ([StatReg](../../07-status-and-faults/StatReg.md) bit 23), and also if either downstream loop saturates — the velocity loop at the current limit (bit 21) or the current loop at the voltage limit (bit 22). Any of these freezes the position integrator so it cannot wind up behind a saturated downstream stage.
- **Default:** `0` (position integral disabled, so the position loop is purely proportional).

## Examples

```text
APosKi[1]=2.5       ; enable a position-loop integral term (first scheduling element)
APosKi[1]           ; read the position-loop integral gain
```

### Walk-through: add a position integral and observe the steady-state effect

This scenario adds the v5 position integral on top of an already-tuned proportional position loop and uses the velocity-saturation status bit to confirm the loop is not running into [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md).

1. **Confirm the proportional position loop is in place**:

   ```text
   APosGain[1]                  ; should be non-zero
   ```

2. **Add the integral term** (held in set 1 when scheduling is off):

   ```text
   APosKi[1]=2.5
   ```

3. **Command a steady-state hold** (axis stationary at a target). With `PosGain` alone, any constant residual force (gravity, friction bias) would leave a small `PosErr`; with `PosKi > 0` the accumulator builds until the `PosGain*PosErr + integral` sum is large enough to balance it, driving the steady-state error toward zero.

4. **Check [StatReg](../../07-status-and-faults/StatReg.md) bit 23** while the integrator is rising:

   ```text
   (AStatReg & 0x800000) >> 23   ; velocity saturation
   ```

   If bit 23 reads `1`, the position-loop PI output is asking for more than `MaxVel`, the velocity reference is being clamped and the integrator anti-windup is engaged for that cycle. If it stays `0`, the integral is building up freely.

> **Note.** [ClearIntegral](../01-general-keywords/ClearIntegral.md) only zeroes the *velocity*-loop integrator; the position-loop integrator carries through that command. To restart the position integral cleanly, disable the motor and re-enable, or temporarily set `PosKi = 0`.

## See also

- [PosGain](PosGain.md) — proportional gain whose output `PosKi` integrates
- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — position error at the input of the position loop
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference that the position PI output forms
- [VelKi](../04-velocity-control/VelKi.md) — integral gain of the inner (velocity) loop
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — clears the velocity-loop integrator (does **not** affect the position integrator)
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 23 (velocity saturation) shows when the PI output is clamped
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
