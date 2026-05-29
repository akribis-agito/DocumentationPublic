---
keyword: ForceGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 577
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceGain

Proportional gain of the force-loop PID controller.

## Overview

`ForceGain` is the proportional (P) term of the standard-form PID controller in the force control loop. Each control cycle it multiplies the force error [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) (the filtered reference [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) minus the [Force](../../08-axis-operation/04-force-operation-mode/Force.md) feedback) after an internal scaling factor that depends on the force-control structure selected by [ForcePIVOn](ForcePIVOn.md):

| ForcePIVOn | Force-control structure | Internal scaling |
|------------|-------------------------|------------------|
| 0          | Standard force control  | 1E-6             |
| 1          | Force-over-PIV control  | 1E-3             |

The scaled product is the gained error:

$$
\text{gained error} = \text{ForceErr} \cdot \text{ForceGain} \cdot \text{scaling}
$$

This gained error is the P contribution of the PID output, and it is also the signal that the integral ([ForceKi](ForceKi.md)) and derivative ([ForceKd](ForceKd.md)) terms act on.

Value range is `0` to `2147483647`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

## How it works

In **standard force control** (`ForcePIVOn = 0`) the PID output (P + I + D) plus the feedforward terms is passed through the force output filters to form the current reference. Here `ForceGain` is scaled by 1E-6.

In **force-over-PIV control** (`ForcePIVOn = 1`) the PID output plus the position-wise feedforward ([ForceFFWP](ForceFFWP.md)) is scaled by the controller sampling time and added to the entry position to form the position reference fed to the inner position/velocity cascade. Here `ForceGain` is scaled by 1E-3.

## Examples

```text
AForceGain[1]=120       ; set the force-loop proportional gain
AForceGain[1]           ; read the force-loop proportional gain
```

### Walk-through: configure a force-over-PIV PID

Force-over-PIV control (`ForcePIVOn = 1`) wraps the force PID around the existing position+velocity cascade. The three force-loop gains share the same gained-error signal and must be set together. The example below assumes a tuned PIV cascade and adds the force loop.

1. **Select the force-over-PIV structure** (motor off, axis stationary):

   ```text
   AForcePIVOn[1]=1
   ```

2. **Set the three PID terms** of the outer force loop:

   ```text
   AForceGain[1]=120        ; P term (scaled by 1e-3 in force-over-PIV)
   AForceKi[1]=50           ; I term (scaled by 1e-3)
   AForceKd[1]=200          ; D term (scaled by 1e-3)
   ```

3. **Add position-wise feedforward** so the force loop does not have to chase the steady weight of the load:

   ```text
   AForceFFWP[1]=...
   ```

4. **Enter force operation mode** and command a force setpoint. The force PID output plus the feedforward becomes a position reference scaled by the controller sampling time, added to the entry position, then driven by the inner position/velocity loops. Saturation feedback into the integrator anti-windup comes from the inner-loop limits (see [ForceKi](ForceKi.md)).

> **Note on scaling.** Switching [ForcePIVOn](ForcePIVOn.md) between 0 and 1 changes the internal scaling of `ForceGain` (1E-6 vs 1E-3), so the same numeric value gives a 1000-fold different effective gain - re-tune after switching structures.

## See also

- [ForceKi](ForceKi.md) — force-loop integral gain (uses the same gained error)
- [ForceKd](ForceKd.md) — force-loop derivative gain (uses the same gained error)
- [ForcePIVOn](ForcePIVOn.md) — selects the force-control structure (sets the ForceGain scaling)
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — error signal multiplied by ForceGain
- [ForceFFW](ForceFFW.md) / [ForceFFWP](ForceFFWP.md) / [ForceVelFFW](ForceVelFFW.md) — feedforward terms summed at the loop output
- [Force control](00-overview.md) — force-loop structure overview
