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
- **Enhanced speed range.** If [ControlMode](ControlMode.md) bit 0 is set (default), the midpoint of the phase voltages is subtracted from all phases (a common-mode / third-harmonic-style injection), which raises the usable line-to-line voltage. For brushless motors the subtracted midpoint is the average of the largest and smallest of the three phase voltages, $\tfrac{1}{2}\big(\max(\text{Va},\text{Vb},\text{Vc}) + \min(\text{Va},\text{Vb},\text{Vc})\big)$; for two-phase steppers (where Vc starts at 0) it is $\tfrac{1}{2}(\text{Va} + \text{Vb})$. This step runs for brushless and stepper motors; brush motors skip it.
- **Saturation.** The voltage is limited to the maximum PWM amplitude ([MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md)), which is expressed in the same per-1000 units as `Va` and defaults to 90 % of the full count (900 keyword units). `MaxPWM` can never reach the full ±1000, because a share of the half-period is reserved for the PWM dead band, so even at full command `Va` is held strictly below 1000. In normal brushless vector (dq0) control the limiting is done on the [Vq](Vq.md)/[Vd](Vd.md) vector *before* the inverse transform (both axes scaled by the same factor), so the sinusoidal phase relationship is preserved. The direct per-phase clamp of `Va` (and `Vb`, `Vc`) to ±`MaxPWM` is applied only in the bypass modes — abc-domain control ([ControlMode](ControlMode.md) bit 1 = 1) or current-loop bypass ([ControlMode](ControlMode.md) bit 2 = 1) — where there is no vector to scale; clamping the phases independently in those modes can distort the phase relationship between `Va`, `Vb` and `Vc`. Either path sets the voltage-saturation bit ([StatReg](../../07-status-and-faults/StatReg.md) bit 22).

**Scaling.** `Va` is reported with the SVM scaling: a value of 1000 equals the full PWM count for the platform, so the internal PWM command is $\text{Va} \cdot (\text{PWM count per }1000)$. The factor depends on the hardware/PWM clock period. Concretely, the per-1000 PWM count equals the reported scaling factor × 1000: on a central-i system `Va` = 1000 commands the full half-period count of 1526 PWM clocks (scaling 1.526), and on a standalone controller it commands that build's full count — 1144 or 4577 PWM clocks depending on the PWM/sampling-rate build (scaling 1.144 or 4.577, the value shown in this page's scaling). Thus the internal PWM compare value is simply `Va` × scaling, and `Va` = ±1000 is ±100 % of the PWM half-period (full modulation depth before [MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md) is applied).

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
