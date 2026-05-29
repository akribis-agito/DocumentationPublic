---
keyword: VoltageFFWOn
summary: Master enable for voltage feedforward in the current/voltage loop.
availability:
  standalone: []
  central-i:
  - v5
can_code: 852
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VoltageFFWOn

Master enable for voltage feedforward in the current/voltage loop.

> Available from central-i v5.

## Overview

`VoltageFFWOn` switches voltage feedforward on or off for the axis. Voltage feedforward is a model-based term that estimates the motor terminal voltage required to drive the commanded current, from the motor's electrical model (resistance, inductance and back-EMF), and adds it ahead of the current PI controllers. By supplying most of the needed voltage in advance, it reduces the work the current loop has to do to track its reference, which improves current tracking at high speed and under fast current changes.

When `VoltageFFWOn = 0` (default) no feedforward voltage is added to the current-loop output. When `VoltageFFWOn = 1` the computed feedforward is added to the loop voltage command.

The feedforward outputs themselves, [VqFFW](VqFFW.md) and [VdFFW](VdFFW.md), are always computed and can be read regardless of this switch; `VoltageFFWOn` only controls whether they are actually summed into the voltage command.

## How it works

Each control cycle the controller computes the feedforward voltage from three physical contributions of the motor model:

- a resistive term, the voltage to push the commanded current through the winding resistance (R·i), scaled by [RmFFWLevel](RmFFWLevel.md);
- an inductive term, the voltage to change the current at the commanded rate (L·di/dt), scaled by [LmFFWLevel](LmFFWLevel.md);
- a back-EMF term, the speed-proportional voltage the moving motor generates, from [BEMFConst](BEMFConst.md) scaled by [BEMFFFWLevel](BEMFFFWLevel.md).

These are assembled into the quadrature- and direct-axis feedforward outputs [VqFFW](VqFFW.md) and [VdFFW](VdFFW.md). With `VoltageFFWOn = 1`, those outputs are added to the q-axis and d-axis PI outputs [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) and [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) before the combined voltage vector is limited against the PWM magnitude and transformed to the phase voltages. For brush motors the q-axis feedforward is added on the single phase voltage command in the same way.

| Value | Meaning |
|-------|---------|
| 0 | Voltage feedforward disabled (default). The feedforward outputs are still computed and readable but not applied. |
| 1 | Voltage feedforward enabled. The computed feedforward is added to the current-loop voltage command. |

`VoltageFFWOn` is a flash-backed parameter and cannot be changed while the axis is in motion (it can be changed with the motor on but stationary).

## Examples

```text
AVoltageFFWOn=1      ; enable voltage feedforward
AVoltageFFWOn        ; read back the enable state
AVoltageFFWOn=0      ; disable voltage feedforward
```

## See also

- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — the computed q-axis and d-axis feedforward voltage outputs
- [RmFFWLevel](RmFFWLevel.md) — level of the resistive (R·i) feedforward term
- [LmFFWLevel](LmFFWLevel.md) — level of the inductive (L·di/dt) feedforward term
- [BEMFConst](BEMFConst.md) / [BEMFFFWLevel](BEMFFFWLevel.md) — back-EMF constant and its feedforward level
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) / [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — current PI outputs the feedforward is added to
