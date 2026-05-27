---
keyword: Vc
summary: Read-only phase C voltage reference for space-vector modulation (PWM-count fraction ×1000).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 15
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
# Vc

Read-only phase C voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Vc` is the phase C voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000 (±1000 = ±100 % of maximum PWM amplitude). Phase C is defined in the hardware reference guide. Together with [Va](Va.md) and [Vb](Vb.md) it forms the three-phase voltage commands sent to the modulator and ultimately the PWM duty.

## How it works

Unlike [Va](Va.md) and [Vb](Vb.md), phase C is not produced by its own current loop — it is derived to complete the phase set:

| Motor group | Source of Vc |
|----|----|
| Three-phase brushless motor | $Vc\ = \ -(Va + Vb)$ so the three phase voltages sum to zero (balanced star). |
| Brush (single-phase) motor | $Vc\ = \ 0$ (only phases A and B are driven, with `Vb = -Va`). |
| Two-phase stepper motor | $Vc\ = \ 0$ before the enhanced-speed-range step (the motor return lines connect to the amplifier C leg). |

After it is formed, `Vc` is subject to the same post-processing as the other phases: the enhanced-speed-range midpoint subtraction (ControlMode bit 0, which can make `Vc` non-zero for steppers), and saturation to the maximum PWM amplitude (firmware `glMaxPWM`) which sets the voltage-saturation bit in [StatReg](../../07-status-and-faults/StatReg.md).

## Examples

```text
AVc                 ; read phase C SVM voltage reference
```

## See also

- [Va](Va.md), [Vb](Vb.md) — phase A and B voltage references that Vc completes
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [ControlMode](ControlMode.md) — control-domain, loop-bypass and enhanced-speed-range options
- [StatReg](../../07-status-and-faults/StatReg.md) — voltage-saturation status set when Vc is clamped
