---
keyword: LmFFWLevel
summary: "Percentage level applied to the inductive (L di/dt) voltage feedforward contribution."
availability:
  standalone: []
  central-i:
  - v5
can_code: 846
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
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# LmFFWLevel

Percentage level applied to the inductive (L di/dt) voltage feedforward contribution.

> Available from central-i v5.

## Overview

`LmFFWLevel` scales the inductive term of the voltage feedforward. To change the current in a winding the controller must apply a voltage proportional to the inductance and the rate of change of current (the L·di/dt term). The controller computes that voltage from the measured motor inductance [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) and the commanded change in current; `LmFFWLevel` is a percentage that sets how much of the computed voltage is applied. This term anticipates the voltage needed during fast current transitions (for example at the start of a move), so the current loop tracks rising and falling current references with less lag.

The inductive term contributes to both the quadrature- and direct-axis feedforward outputs [VqFFW](VqFFW.md) and [VdFFW](VdFFW.md), and it also determines the speed-dependent d-q cross-coupling term in those outputs. It is only applied when voltage feedforward is enabled by [VoltageFFWOn](VoltageFFWOn.md).

## How it works

`LmFFWLevel` is a percentage (in %). The inductive feedforward voltage is the modelled L·di/dt voltage (from [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) and the per-cycle change in reference current) multiplied by `LmFFWLevel`/100:

- `0` — no inductive feedforward (default);
- `100` — full modelled inductive voltage applied;
- values up to the maximum allow over- or under-compensation of the modelled term.

For three-phase motors the controller uses the per-phase inductance: if the stored [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) is a line-to-line value it is halved internally to the phase value before the term is computed. The same `LmFFWLevel` also scales the speed-dependent cross-coupling between the d and q axes.

The valid range is 0 to 200 (%) and the default is 0. `LmFFWLevel` is a flash-backed parameter and may be set with the motor on or in motion; the change takes effect on the next control cycle. With either `LmFFWLevel` or [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) at its minimum, the inductive term is zero.

## Examples

```text
ALmFFWLevel=100      ; apply the full modelled inductive voltage
ALmFFWLevel          ; read back the configured level
ALmFFWLevel=0        ; disable the inductive feedforward term
```

## See also

- [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) — measured motor inductance this level scales
- [RmFFWLevel](RmFFWLevel.md) — level of the resistive (R·i) feedforward term
- [BEMFFFWLevel](BEMFFFWLevel.md) — level of the back-EMF feedforward term
- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — feedforward outputs that carry the inductive term
- [VoltageFFWOn](VoltageFFWOn.md) — master enable for voltage feedforward
