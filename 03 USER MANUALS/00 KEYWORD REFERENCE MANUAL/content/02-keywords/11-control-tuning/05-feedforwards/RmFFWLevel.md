---
keyword: RmFFWLevel
summary: Percentage level applied to the resistive (R i) voltage feedforward contribution.
availability:
  standalone: []
  central-i:
  - v5
can_code: 845
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 200.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RmFFWLevel

Percentage level applied to the resistive (R i) voltage feedforward contribution.

> Available from central-i v5.

## Overview

`RmFFWLevel` scales the resistive term of the voltage feedforward. To drive a steady current through the motor winding the controller must apply a voltage equal to the current times the winding resistance (the R·i term). The controller computes that voltage from the measured motor resistance [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) and the commanded current; `RmFFWLevel` is a percentage that sets how much of the computed voltage is applied. This term supplies the steady-state voltage needed to hold a current, so the current loop does not have to build it up through its integrator.

The resistive term contributes to both the quadrature- and direct-axis feedforward outputs [VqFFW](VqFFW.md) and [VdFFW](VdFFW.md), and it is only applied when voltage feedforward is enabled by [VoltageFFWOn](VoltageFFWOn.md).

## How it works

`RmFFWLevel` is a percentage (in %). The resistive feedforward voltage is the modelled R·i voltage (from [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) and the reference current) multiplied by `RmFFWLevel`/100:

- `0` — no resistive feedforward (default);
- `100` — full modelled resistive voltage applied;
- values up to the maximum allow over- or under-compensation of the modelled term.

For three-phase motors the controller uses the per-phase resistance: if the stored [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) is a line-to-line value it is halved internally to the phase value before the term is computed.

The valid range is 0 to 200 (%) and the default is 0. `RmFFWLevel` is a flash-backed parameter and may be set with the motor on or in motion; the change takes effect on the next control cycle. With either `RmFFWLevel` or [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) at its minimum, the resistive term is zero.

## Examples

```text
ARmFFWLevel=100      ; apply the full modelled resistive voltage
ARmFFWLevel          ; read back the configured level
ARmFFWLevel=0        ; disable the resistive feedforward term
```

## See also

- [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) — measured motor resistance this level scales
- [LmFFWLevel](LmFFWLevel.md) — level of the inductive (L di/dt) feedforward term
- [BEMFFFWLevel](BEMFFFWLevel.md) — level of the back-EMF feedforward term
- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — feedforward outputs that carry the resistive term
- [VoltageFFWOn](VoltageFFWOn.md) — master enable for voltage feedforward
