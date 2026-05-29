---
keyword: VdFFW
summary: Read-only direct-axis voltage feedforward output added to the d-axis voltage command.
availability:
  standalone: []
  central-i:
  - v5
can_code: 851
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range: null
  default: 0
  scaling: 1.526
  implemented: final
overrides: {}
---
# VdFFW

Read-only direct-axis voltage feedforward output added to the d-axis voltage command.

> Available from central-i v5.

## Overview

`VdFFW` is the direct-axis (d-axis) voltage feedforward output. It is the model-based voltage the controller estimates is needed on the d axis to drive the commanded d-axis current, computed every control cycle from the motor's electrical model. When voltage feedforward is enabled by [VoltageFFWOn](VoltageFFWOn.md), `VdFFW` is added to the d-axis current PI output [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) before the voltage vector is limited and transformed to phase voltages. It is the d-axis counterpart of [VqFFW](VqFFW.md).

`VdFFW` is read-only and reported in the same internal PWM-percent units as [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md). It is computed whether or not feedforward is enabled; only its addition into the loop is gated by [VoltageFFWOn](VoltageFFWOn.md).

## How it works

Each control cycle `VdFFW` is the sum of the motor-model voltage terms evaluated on the d-axis current reference [IdRef](../../../02-keywords/09-current-and-voltage/02-motor-variables/IdRef.md):

$$
\text{VdFFW} = R_{\text{ffw}}\,i_{d,\text{ref}} + L_{\text{ffw}}\,f_s\,(i_{d,\text{ref}} - i_{d,\text{ref,prev}}) - X_{\text{ffw}}\,i_{q,\text{ref}}\,\omega
$$

where the terms are, in order:

| Term | Physical role | Set by |
|------|---------------|--------|
| $R_{\text{ffw}}\,i_{d,\text{ref}}$ | Resistive drop: voltage to push the commanded d-axis current through the winding resistance | [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) scaled by [RmFFWLevel](RmFFWLevel.md) |
| $L_{\text{ffw}}\,f_s\,(i_{d,\text{ref}} - i_{d,\text{ref,prev}})$ | Inductive term (L·di/dt): voltage to change the d-axis current at the commanded rate, using the change in reference current over one control period ($f_s$ is the control sample rate) | [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) scaled by [LmFFWLevel](LmFFWLevel.md) |
| $-X_{\text{ffw}}\,i_{q,\text{ref}}\,\omega$ | Cross-coupling: the speed-dependent coupling from the q-axis current into the d axis (derived from the inductance term), with opposite sign to the q-axis cross term | [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) / [LmFFWLevel](LmFFWLevel.md) |

The d-axis feedforward has no back-EMF term: the speed-proportional back-EMF voltage acts on the q axis only and appears in [VqFFW](VqFFW.md).

If [VoltageFFWOn](VoltageFFWOn.md) is non-zero, `VdFFW` is then added to the d-axis PI output [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md). The resulting d-axis and q-axis voltages are limited together as a vector against the maximum PWM magnitude and transformed to the phase voltages (see [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) for the saturation and inverse-Park detail). The d-axis feedforward is not applied to brush motors, which control on a single axis only.

`VdFFW` is reset to 0 when the current loop is reset. The level scalings ([RmFFWLevel](RmFFWLevel.md), [LmFFWLevel](LmFFWLevel.md)) default to 0, so with default settings every term is zero and `VdFFW` reads 0.

## Examples

```text
AVdFFW               ; read the d-axis voltage feedforward output
```

## See also

- [VqFFW](VqFFW.md) — quadrature-axis voltage feedforward output (carries the back-EMF term)
- [VoltageFFWOn](VoltageFFWOn.md) — master enable that gates whether VdFFW is applied
- [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — d-axis PI output that VdFFW is added to
- [IdRef](../../../02-keywords/09-current-and-voltage/02-motor-variables/IdRef.md) — d-axis current reference the resistive and inductive terms use
- [RmFFWLevel](RmFFWLevel.md) / [LmFFWLevel](LmFFWLevel.md) — level scalings of the resistive and inductive terms
