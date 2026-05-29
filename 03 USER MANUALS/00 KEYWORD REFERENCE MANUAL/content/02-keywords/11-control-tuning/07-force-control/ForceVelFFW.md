---
keyword: ForceVelFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 580
attributes:
  access: rw
  scope: axis
  flash: true
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
overrides:
  central-i.v5:
    data_type: float32
---
# ForceVelFFW

Velocity feedback compensation gain in the force loop.

## Overview

`ForceVelFFW` is the velocity feedback compensation gain applied to the current reference in force operation mode. It multiplies the velocity feedback and is **subtracted** from the current reference:

$$
\text{ForceVelFFW term} = -\,\text{Vel} \cdot \text{ForceVelFFW} \cdot 0.00000001
$$

where `Vel` is the velocity feedback (the value reported by [Vel](../../10-motion/01-kinematics-status/Vel.md), index 1). The internal scaling is 1E-8.

Value range is `-2147483648` to `2147483647`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

`ForceVelFFW` is applied in both force-control structures selected by [ForcePIVOn](ForcePIVOn.md):

- **Standard force control** (`ForcePIVOn = 0`): the term is combined with the PID output and the current-wise feedforward ([ForceFFW](ForceFFW.md)) before the force output filters, forming the current reference.
- **Force-over-PIV control** (`ForcePIVOn = 1`): the term is combined with the velocity-loop output and the current-wise feedforward to form the current reference.

## How it works

Because the contribution opposes the velocity feedback, it acts as a velocity-proportional term at the current reference. In both structures it enters at the same summing point as the current-wise feedforward [ForceFFW](ForceFFW.md).

## Examples

```text
AForceVelFFW[1]=100     ; set the velocity feedback compensation gain
AForceVelFFW[1]         ; read the velocity feedback compensation gain
```

### Worked example: sign and magnitude of the contribution

With `ForceVelFFW = 100` and a velocity feedback `Vel[1] = 5000` (user velocity units), the term added at the current-reference summing point is:

`-Vel x ForceVelFFW x 1E-8 = -5000 x 100 x 1E-8 = -0.005` (current units)

If the axis is moving in the opposite direction (`Vel[1] = -5000`) the term becomes `+0.005`. Because the term is subtracted, it always opposes the direction of motion, acting like an extra viscous drag in the current command and supplying the steady-state current needed to overcome velocity-proportional load.

## See also

- [ForceFFW](ForceFFW.md) — current-wise force feedforward (added at the same summing point)
- [ForceFFWP](ForceFFWP.md) — position-wise force feedforward (force-over-PIV only)
- [ForcePIVOn](ForcePIVOn.md) — selects the force-control structure
- [Force control](00-overview.md) — force-loop structure overview
