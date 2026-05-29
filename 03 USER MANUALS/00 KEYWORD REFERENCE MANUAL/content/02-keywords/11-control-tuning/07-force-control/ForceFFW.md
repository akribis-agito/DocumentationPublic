---
keyword: ForceFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 589
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
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceFFW

Current-wise force feedforward gain.

## Overview

`ForceFFW` is the current-wise force feedforward gain. It multiplies the filtered force reference [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) and contributes directly to the current reference, in parallel with the force PID output:

$$
\text{ForceFFW term} = \text{ForceRef} \cdot \text{ForceFFW} \cdot 0.001
$$

The internal scaling is 1E-3. Value range is `0` to `1000000`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

`ForceFFW` is applied in both force-control structures selected by [ForcePIVOn](ForcePIVOn.md):

- **Standard force control** (`ForcePIVOn = 0`): the feedforward term is added to the PID output before the force output filters, forming the current reference.
- **Force-over-PIV control** (`ForcePIVOn = 1`): the feedforward term is added to the velocity-loop output to form the current reference, alongside the velocity compensation term ([ForceVelFFW](ForceVelFFW.md)).

## How it works

Because this term is proportional to the (filtered) commanded force rather than to the error, it supplies a current contribution that tracks the force command without waiting for the loop to build error, leaving the PID to act on the residual.

## Examples

```text
AForceFFW[1]=1000       ; set the current-wise force feedforward gain
AForceFFW[1]            ; read the current-wise force feedforward gain
```

### Worked example: contribution at a steady force command

With `ForceFFW = 1000` and a (filtered) force reference `ForceRef = 50` (force units), the current contribution from this feedforward path is:

`ForceFFW term = 50 x 1000 x 0.001 = 50` (current units)

The PID then only has to act on the residual error between the actual force and the command, leaving the steady-state component to the feedforward.

## See also

- [ForceFFWP](ForceFFWP.md) — position-wise force feedforward (force-over-PIV only)
- [ForceVelFFW](ForceVelFFW.md) — velocity feedback compensation at the current reference
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — filtered reference multiplied by this gain
- [Force control](00-overview.md) — force-loop structure overview
