---
keyword: VelGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 102
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
---
# VelGain

Proportional gain of the velocity loop — the factor that multiplies the velocity error.

## Overview

`VelGain` is the proportional gain of the inner (velocity) loop in the PIV cascade. Each control cycle it multiplies the velocity error [VelErr](../../10-motion/01-kinematics-status/VelErr.md) to form the proportional part of the velocity-PI output. That output (proportional plus the [VelKi](VelKi.md) integral, after the velocity filters) becomes the motor current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) that drives the current loop.

`VelGain` is an array, so it can take part in gain scheduling. Without gain scheduling the first element `VelGain[1]` is used for control. See [ScheduleMode](../01-general-keywords/ScheduleMode.md).

In gantry mode the gantry-specific velocity gain is used in place of `VelGain` for the gantried axes.

## How it works

The velocity controller acts on [VelErr](../../10-motion/01-kinematics-status/VelErr.md) (the velocity reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md) minus the velocity feedback). The proportional term and the integral are summed and scaled internally to produce the velocity-PI output:

$$
\text{proportional} = \text{VelErr} \cdot \text{VelGain}
$$

$$
\text{VelPIOutput} = \big( \text{proportional} + \text{integral} \big) \cdot k_{\text{scale}}
$$

The integral is the running accumulation of `proportional × VelKi` (see [VelKi](VelKi.md)). `VelPIOutput` then passes through the velocity filters ([VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md)) and, in position mode, has the acceleration and velocity feed-forwards added to form the current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).

- **What it multiplies:** the velocity error [VelErr](../../10-motion/01-kinematics-status/VelErr.md).
- **Where it sums:** its product is added to the velocity integral; the sum (after internal scaling and the velocity filters) becomes [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).
- **Scaling / units:** applied as a multiplier (scaling factor 1.0); the combined PI result is brought to current-command units by a fixed internal scaling.

### Scaling, range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 1000000 | 0 to 1000000000 |
| Default | 0 | 0 |

## Examples

```text
AVelGain[1]=1200    ; set the velocity-loop proportional gain (first scheduling element)
AVelGain[1]         ; read the velocity-loop proportional gain
```

### Worked example: proportional contribution at a velocity error

With `VelGain = 1200` and a velocity error `VelErr = 50` (in velocity-loop units), the proportional term entering the PI sum is:

`proportional = VelErr x VelGain = 50 x 1200 = 60000`

This product enters the PI sum (together with the integral) and is then converted to current-command units by the fixed internal scaling before passing through the velocity filters and feedforwards.

### Walk-through: configure the PI velocity loop and verify saturation via StatReg

This recipe sets up the inner velocity loop alongside the outer position loop, then uses the status word to confirm whether the controller is driving the loop into a limit.

1. **Set the proportional gain** (first scheduling element used when no scheduling is active):

   ```text
   AVelGain[1]=1200
   ```

2. **Add an integral term** for steady-state velocity error rejection. The integral is anti-wound automatically when the output saturates (see [VelKi](VelKi.md)):

   ```text
   AVelKi[1]=80
   ```

3. **Clear any integrator history** carried over from earlier tests, so the loop starts from a known state (axis must be stationary):

   ```text
   AClearIntegral
   ```

4. **Command a move and observe [StatReg](../../07-status-and-faults/StatReg.md)**. Three saturation bits matter here:

   ```text
   AStatReg                      ; read whole status word
   (AStatReg & 0x200000) >> 21   ; current saturation (bit 21) - current command hit PeakCL/ContCL
   (AStatReg & 0x400000) >> 22   ; voltage saturation (bit 22) - phase voltage hit MaxPWM
   (AStatReg & 0x800000) >> 23   ; velocity saturation (bit 23) - VelRef hit MaxVel
   ```

   If bit 23 reads `1`, the position-loop output (or the velocity feed-forward) is asking for more speed than [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) allows, so the velocity loop is being driven from a clamped reference. If bit 21 reads `1`, the velocity-PI output is being clamped at the current limit and the velocity-loop integrator is being held by the anti-windup gate inside [VelKi](VelKi.md) until saturation clears.

5. **If a notch is needed** to clean the velocity-PI output before it forms the current command, define one in [VelFiltDef](VelFiltDef.md), enable it in [VelFiltOn](VelFiltOn.md), then run [CalcFilters](../01-general-keywords/CalcFilters.md) so the new coefficients take effect.

## Changes between versions

In **v5 (central-i)** `VelGain` is a floating-point value with a wider range (`0` to `1000000000`); the proportional×error → PI → current-command path is otherwise the same. **v5 is central-i only.**

## See also

- [VelErr](../../10-motion/01-kinematics-status/VelErr.md) — velocity error that `VelGain` multiplies
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference
- [VelKi](VelKi.md) — velocity integral gain summed with the `VelGain` term
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — zeroes the velocity-loop integrator
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — current command produced from the velocity-PI output
- [VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md) — velocity-loop filters on the PI output
- [PosGain](../03-position-control/PosGain.md) — proportional gain of the outer (position) loop
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21 (current sat) / bit 22 (voltage sat) / bit 23 (velocity sat)
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
