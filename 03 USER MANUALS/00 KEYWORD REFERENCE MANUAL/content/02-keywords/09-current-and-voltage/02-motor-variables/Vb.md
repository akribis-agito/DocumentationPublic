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
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    data_type: float32
    range: null
    scaling: 1.526
---
# Vb

Read-only phase B voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Vb` is the phase B voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000 (±1000 = ±100 % of maximum PWM amplitude). Phase B is defined in the hardware reference guide. Together with [Va](Va.md) and [Vc](Vc.md) it forms the three-phase voltage commands sent to the modulator and ultimately the PWM duty.

## How it works

`Vb` is produced in the same way as [Va](Va.md), shifted to phase B:

| Case | Source of Vb |
|----|----|
| Brushless, vector (dq0) control ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4, [ControlMode](ControlMode.md) bit 1 = 0, bit 2 = 0) | Inverse transform of the dq0 voltage outputs: $\text{Vb}\ = \ \text{Vq} \cdot \sin(\theta - 120^\circ) + \text{Vd} \cdot \cos(\theta - 120^\circ)$, with [Vd](Vd.md)/[Vq](Vq.md) from the dq current loops. |
| Brushless, abc (phase) control ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4, [ControlMode](ControlMode.md) bit 1 = 1, bit 2 = 0) | Output of the phase B current PI loop on [IbErr](IbErr.md) ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) integral + proportional, scaled by [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)). [Vq](Vq.md) and [Vd](Vd.md) are forced to 0. |
| Stepper motor ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 6 or 7) | Output of the phase B current PI loop on [IbErr](IbErr.md), with [IbRef](IbRef.md) generated as $\text{CurrRef} \cdot \cos(\text{stepper electrical angle})$. The stepper path is always per-phase (abc-domain) and ignores [ControlMode](ControlMode.md) bits 1 and 2. |
| Brush / voice-coil motor ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 1 or 2, [ControlMode](ControlMode.md) bit 2 = 0) | $\text{Vb}\ = \ -\text{Va}$ (the brush path drives a single H-bridge across phases A and B). |
| Brushless current loop bypassed ([ControlMode](ControlMode.md) bit 2 = 1) | $\text{Vb}\ = \ \text{IbRef}$. (Brush sets [IbRef](IbRef.md) = 0 in this case; stepper ignores this bit.) |

The same post-processing as [Va](Va.md) then applies: brushless $\text{Vc} = -(\text{Va} + \text{Vb})$ and brush/stepper $\text{Vc} = 0$, the enhanced-speed-range midpoint subtraction ([ControlMode](ControlMode.md) bit 0, brushless and stepper only), and saturation to the maximum PWM amplitude ([MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md)) which sets the voltage-saturation bit ([StatReg](../../07-status-and-faults/StatReg.md) bit 22).

Vb lags Va by 120° of electrical angle, and Vc lags Vb by a further 120°:

![Three balanced phase voltages 120 degrees apart across one electrical cycle](three-phase-waveforms.svg)

### Edge cases

- **Motor off.** When [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) is 0 the current loop is reset and `Vb` is forced to 0.
- **Force / position / current operation modes.** The current loop runs identically in all modes; only the source of [CurrRef](CurrRef.md) differs.
- **Open-loop voltage mode.** When the open-loop voltage command is active ([OpenLoopVolt](../../08-axis-operation/01-general-keywords/OpenLoopVolt.md) / [OpenLoopCurr](../../08-axis-operation/01-general-keywords/OpenLoopCurr.md)), `Vb` reflects that command path rather than the closed loop.
- **Simulation.** In simulation `Vb` follows the same formulas.
- **External current-command amplifier ([AmpType](../../02-motor-and-amplifier/AmpType.md) = current-command).** The current loop runs in the drive, not the controller.

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
