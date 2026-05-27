---
keyword: Vb
summary: Read-only phase B voltage reference for space-vector modulation (PWM-count fraction ×1000).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 14
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# Vb

Read-only phase B voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Vb` is the phase B voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000 (±1000 = ±100 % of maximum PWM amplitude). Phase B is defined in the hardware reference guide. Together with [Va](Va.md) and [Vc](Vc.md) it forms the three-phase voltage commands sent to the modulator and ultimately the PWM duty.

## How it works

`Vb` is produced in the same way as [Va](Va.md), shifted to phase B:

| Case | Source of Vb |
|----|----|
| Brushless, vector (dq0) control (ControlMode bit 1 = 0) | Inverse transform of the dq0 voltage outputs: $Vb\ = \ Vq \cdot \sin(\theta - 120^\circ) + Vd \cdot \cos(\theta - 120^\circ)$, with [Vd](Vd.md)/[Vq](Vq.md) from the dq current loops. |
| Brushless or stepper, abc (phase) control (ControlMode bit 1 = 1) | Output of the phase B current PI loop on [IbErr](IbErr.md) ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) integral + proportional, scaled by [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)). |
| Brush (single-phase) motor | $Vb\ = \ -Va$ (phase B mirrors phase A). |
| Current loop bypassed (ControlMode bit 2 = 1) | $Vb\ = \ IbRef$. |

The same post-processing as [Va](Va.md) then applies: brushless `Vc = -(Va + Vb)`, the enhanced-speed-range midpoint subtraction (ControlMode bit 0), and saturation to the maximum PWM amplitude which sets the voltage-saturation bit ([StatReg](../../07-status-and-faults/StatReg.md) bit 22).

## Examples

```text
AVb                 ; read phase B SVM voltage reference
```

## See also

- [Va](Va.md), [Vc](Vc.md) — phase A and C voltage references
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [IbRef](IbRef.md), [IbErr](IbErr.md) — phase B current reference and error feeding Vb
- [ControlMode](ControlMode.md) — control-domain and loop-bypass options
- [StatReg](../../07-status-and-faults/StatReg.md) — voltage-saturation status set when Vb is clamped
