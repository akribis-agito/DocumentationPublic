---
keyword: Va
summary: Read-only phase A voltage reference for space-vector modulation (PWM-count fraction ×1000).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 13
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
# Va

Read-only phase A voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Va` is the phase A voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000 (so ±1000 corresponds to ±100 % of the maximum PWM amplitude). Phase A is defined in the hardware reference guide. Together with [Vb](Vb.md) and [Vc](Vc.md) it forms the three-phase voltage commands sent to the modulator and ultimately the PWM duty.

## How it works

How `Va` is produced depends on the motor group and the [ControlMode](ControlMode.md) bits:

| Case | Source of Va |
|----|----|
| Brushless, vector (dq0) control ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4, [ControlMode](ControlMode.md) bit 1 = 0, bit 2 = 0) | Inverse transform of the dq0 voltage outputs: $\text{Va}\ = \ \text{Vq} \cdot \sin(\theta) + \text{Vd} \cdot \cos(\theta)$, where $\theta$ is the commutation angle and [Vd](Vd.md)/[Vq](Vq.md) come from the dq current loops. |
| Brushless, abc (phase) control ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4, [ControlMode](ControlMode.md) bit 1 = 1, bit 2 = 0) | Output of the phase A current PI loop on [IaErr](IaErr.md): integral term ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) plus proportional term, scaled by the loop gain ([CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)). [Vq](Vq.md) and [Vd](Vd.md) are forced to 0. |
| Stepper motor ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 6 or 7) | Output of the phase A current PI loop on [IaErr](IaErr.md), with [IaRef](IaRef.md) generated as $\text{CurrRef} \cdot \sin(\text{stepper electrical angle})$. The stepper path is always per-phase (abc-domain) and ignores [ControlMode](ControlMode.md) bits 1 and 2. |
| Brush / voice-coil motor ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 1 or 2, [ControlMode](ControlMode.md) bit 2 = 0) | Output of the phase A current PI loop on [IaErr](IaErr.md). [ControlMode](ControlMode.md) bit 1 is not used. |
| Brushless or brush, current loop bypassed ([ControlMode](ControlMode.md) bit 2 = 1) | $\text{Va}\ = \ \text{IaRef}$ — the phase current reference is used directly as the voltage command. (Stepper motors ignore this bit.) |

After `Va` is formed:

- **Phase completion.** For brushless motors $\text{Vc} = -(\text{Va} + \text{Vb})$ so the three phase voltages sum to zero. For brush motors $\text{Vb} = -\text{Va}$ and $\text{Vc} = 0$. For stepper motors $\text{Vb}$ comes from its own phase-B PI loop and $\text{Vc} = 0$ (the motor return lines connect to the amplifier C leg).
- **Enhanced speed range.** If [ControlMode](ControlMode.md) bit 0 is set (default), the midpoint of the phase voltages is subtracted from all phases (a common-mode / third-harmonic-style injection), which raises the usable line-to-line voltage. This step runs for brushless and stepper motors; brush motors skip it.
- **Saturation.** Each phase is clamped to the maximum PWM amplitude ([MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md)); in brushless vector mode the [Vq](Vq.md)/[Vd](Vd.md) vector is scaled before the inverse transform so the sinusoidal relationship is preserved. Saturation sets the voltage-saturation bit ([StatReg](../../07-status-and-faults/StatReg.md) bit 22).

**Scaling.** `Va` is reported with the SVM scaling: a value of 1000 equals the full PWM count for the platform, so the internal PWM command is $\text{Va} \cdot (\text{PWM count per }1000)$. The factor depends on the hardware/PWM clock period.

The full reference-to-voltage chain (shared by all phase variables) is:

![abc/dq current-loop signal path](current-loop-signal-path.svg)

The three phase commands are three sinusoids 120° apart in the electrical angle θ, so Vc is fully determined by Va and Vb:

![Three balanced phase voltages 120 degrees apart across one electrical cycle](three-phase-waveforms.svg)

### Edge cases

- **Motor off.** When [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) is 0 the current loop is reset and `Va` is forced to 0.
- **Force / position / current operation modes.** The current loop runs identically in all modes; only the source of [CurrRef](CurrRef.md) differs.
- **Open-loop voltage mode.** When the open-loop voltage command is active ([OpenLoopVolt](../../08-axis-operation/01-general-keywords/OpenLoopVolt.md) / [OpenLoopCurr](../../08-axis-operation/01-general-keywords/OpenLoopCurr.md)), `Va` reflects that command path rather than the closed loop.
- **Simulation.** In simulation `Va` follows the same formulas, since the entire loop runs on the simulated phase currents.
- **External current-command amplifier ([AmpType](../../02-motor-and-amplifier/AmpType.md) = current-command).** The current loop runs in the drive instead of the controller, and `Va` here does not represent the drive's phase A voltage.

## Examples

```text
AVa                 ; read phase A SVM voltage reference
```

## See also

- [Vb](Vb.md), [Vc](Vc.md) — phase B and C voltage references
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [IaRef](IaRef.md) — phase A current reference (equals Va when the loop is bypassed)
- [IaErr](IaErr.md) — phase A current error driving Va when the abc loop runs
- [ControlMode](ControlMode.md) — control-domain, loop-bypass and enhanced-speed-range options
- [StatReg](../../07-status-and-faults/StatReg.md) — voltage-saturation status set when Va is clamped
