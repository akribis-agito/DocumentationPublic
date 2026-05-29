---
keyword: ForceKd
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 588
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
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceKd

Derivative gain of the force-loop PID controller.

## Overview

`ForceKd` is the derivative (D) term of the standard-form PID controller in the force control loop — the force loop is a full PID (P + I + D) in force operation mode. It applies to both force-control structures (standard and force-over-PIV selected by [ForcePIVOn](ForcePIVOn.md)) with a fixed internal scaling of 1E-3.

Each control cycle the derivative term acts on the change in the gained force error between this cycle and the previous one:

$$
D = ForceKd \times (gained\ error - gained\ error_{prev}) \times 0.001
$$

where the *gained error* is the force error after the [ForceGain](ForceGain.md) stage and the subscript *prev* denotes its value on the previous cycle. This is the D contribution to the PID output.

Value range is `0` to `2000000000`; the default is `0`. The keyword is stored in flash and may be changed while the motor is on and in motion.

## Examples

```text
AForceKd[1]=200         ; set the force-loop derivative gain
AForceKd[1]             ; read the force-loop derivative gain
```

## See also

- [ForceGain](ForceGain.md) — force-loop proportional gain (provides the gained error differenced here)
- [ForceKi](ForceKi.md) — force-loop integral gain
- [ForcePIVOn](ForcePIVOn.md) — selects the force-control structure
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — error driven toward zero by the loop
- [ForceRefFilt](ForceRefFilt.md) — first-order low-pass on the reference (shapes what the D term sees)
- [Force control](00-overview.md) — force-loop structure overview
