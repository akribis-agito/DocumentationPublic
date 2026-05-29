---
keyword: ForceKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 578
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
# ForceKi

Integral gain of the force-loop PID controller.

## Overview

`ForceKi` is the integral (I) term of the standard-form PID controller in the force control loop. It applies to both force-control structures (standard and force-over-PIV selected by [ForcePIVOn](ForcePIVOn.md)) with a fixed internal scaling of 1E-3.

Each control cycle the integrator accumulates the gained force error scaled by `ForceKi`:

$$
integrator = integrator + gained\ error \times ForceKi \times 0.001
$$

where the *gained error* is the force error after the [ForceGain](ForceGain.md) stage. The integrator value is the I contribution to the PID output.

Value range is `0` to `2147483647`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

## How it works

The accumulation includes an anti-windup mechanism: the increment added each cycle is multiplied by the loop clamping flags, so while a downstream loop (velocity and current in standard mode, or the position/velocity cascade and current in force-over-PIV mode) is saturated at a limit, the integrator stops accumulating in the direction that would deepen the saturation. This prevents the integral term from winding up while the output is held at a limit.

## Examples

```text
AForceKi[1]=50          ; set the force-loop integral gain
AForceKi[1]             ; read the force-loop integral gain
```

## See also

- [ForceGain](ForceGain.md) — force-loop proportional gain (provides the gained error this term accumulates)
- [ForceKd](ForceKd.md) — force-loop derivative gain
- [ForcePIVOn](ForcePIVOn.md) — selects the force-control structure (changes which downstream limits clamp this integrator)
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — error driven toward zero by the loop
- [StatReg](../../07-status-and-faults/StatReg.md) — saturation bits show when downstream loops are clamped (anti-windup engaged)
- [Force control](00-overview.md) — force-loop structure overview
