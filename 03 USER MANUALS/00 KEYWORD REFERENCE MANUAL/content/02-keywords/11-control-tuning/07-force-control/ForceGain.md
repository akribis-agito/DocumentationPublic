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
gained\ error = ForceErr \times ForceGain \times scaling
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

## See also

- [ForceKi](ForceKi.md) — force-loop integral gain
- [ForceKd](ForceKd.md) — force-loop derivative gain
- [ForcePIVOn](ForcePIVOn.md) — selects the force-control structure (sets the ForceGain scaling)
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — error signal multiplied by ForceGain
- [Force control](00-overview.md) — force-loop structure overview
