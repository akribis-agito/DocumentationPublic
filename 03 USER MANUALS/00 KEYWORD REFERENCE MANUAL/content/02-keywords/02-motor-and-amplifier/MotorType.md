---
keyword: MotorType
summary: Defines the type of motor connected to the axis, governing how currents and voltages are computed and protected.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 50
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorType

Defines the type of motor connected to the axis, governing how currents and voltages are computed and protected.

## Overview

`MotorType` defines the type of motor connected to the built-in or external amplifier. It determines how currents and voltages are calculated and applied to the motor, and how the motor is protected against overcurrent.

> [!warning]
> Selecting the wrong `MotorType` may result in severe damage. Set it correctly before enabling the motor.

`MotorType` interacts with several other configuration keywords. For brushless motors it works with [PolePrs](PolePrs.md) and [EncRes](../03-encoder/01-general-settings/EncRes.md) (commutation and feedback); for stepper motors it works with [StepBits](StepBits.md), [StepInMotCurr](StepInMotCurr.md), and [StepInPosCurr](StepInPosCurr.md). Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion. See the product manual to find out which terminals to use for each motor type.

> [!note]
> The frontmatter range is 0–7. Value 8 (closed-loop stepper, brushless) is reserved for internal use (the firmware marks it "not supported yet") and is documented here for completeness only.

## How it works

Internally, `MotorType` collapses to one of three **motor-class flags** that the real-time control loop tests on every cycle (so it does not have to re-check the specific type): *brush* (covers DC brush, voice coil, and simulation), *brushless* (linear, rotary, and the reserved brushless-stepper), and *stepper* (open- and closed-loop). The class flag selects which current/voltage-generation path runs in the control loop, and it also sets the commutation requirement: brushless types are marked "commutation required" (the [StatReg](../07-status-and-faults/StatReg.md) commutation bit is cleared until auto-phasing completes), while brush and stepper types are marked "commutation done / not needed" immediately.

Changing `MotorType` while it is a brushless type re-arms commutation — the commutation bit is cleared and the axis must re-phase before it can be enabled. (Changing [EncRes](../03-encoder/01-general-settings/EncRes.md), [PolePrs](PolePrs.md), [AmpType](AmpType.md), or the encoder/current direction does the same.)

| MotorType | Class | Description |
|---|---|---|
| 0 Unknown | — | Default value of a new controller. No voltage outputs are applied. |
| 1 DC brush | brush | Requires only two motor output terminals and needs no commutation (physically commutated). |
| 2 Voice coil | brush | Has 1 magnet pole pair and 1 actuator coil. Requires only two motor output terminals and needs no commutation. Operation is identical to a DC brush motor. |
| 3 Linear DC brushless | brushless | 3-phase (3 sets of actuator coils 120 electrical degrees apart), requiring 3 motor output terminals. Commutation determines current/voltage outputs via Park/inverse-Park transformation. The axis is treated as linear; [EncRes](../03-encoder/01-general-settings/EncRes.md) is the encoder count per pole pair (magnetic period), and [PolePrs](PolePrs.md) must be 1. |
| 4 Rotary DC brushless | brushless | 3-phase (3 sets of actuator coils 120 electrical degrees apart), requiring 3 motor output terminals. Commutation determines current/voltage outputs via inverse-Park transformation. The axis is treated as rotary; [EncRes](../03-encoder/01-general-settings/EncRes.md) is the encoder count per revolution, and [PolePrs](PolePrs.md) defines the pole pairs per revolution. |
| 5 Simulation | brush | Used for simulation during development. Generates simulated motion profiles, inputs, and outputs without a physical motor; the commutation/current loop is bypassed and the feedback is forced to follow the reference. |
| 6 Stepper in open loop | stepper | See "Open-loop stepper" below. |
| 7 Stepper in closed loop | stepper | See "Closed-loop stepper" below. |
| 8 Stepper in closed loop (brushless) | brushless | Reserved option for internal use (not supported). |

> [!note]
> When [AmpType](AmpType.md) selects an **external amplifier** that closes its own current loop (any mode except the built-in PWM amplifier or the linear-adapter), the controller marks the motor as "driven externally" and skips its internal current loop regardless of `MotorType` — the controller then only outputs the command (analog current, analog velocity, or pulse-direction) and lets the external amplifier handle commutation and current control.

### Commutation (brushless types 3, 4)

For brushless motors the electrical angle is derived from the feedback. The controller pre-computes one electrical cycle as

$$Counts\ per\ electrical\ cycle = \frac{EncRes}{PolePrs}$$

and a feedback position is converted to electrical radians by multiplying its position-within-cycle by $2\pi / (EncRes/PolePrs)$. The three phase voltages (Va, Vb, Vc) are then produced from the q/d current references through the inverse-Park transformation using this angle. A wrong [PolePrs](PolePrs.md) or [EncRes](../03-encoder/01-general-settings/EncRes.md) therefore mis-scales the electrical angle and commutation will not work.

### Open-loop stepper (MotorType = 6)

A 2-phase stepper motor, requiring 3 pins (phase A, phase B, and the joined phase A/B return). One electrical cycle (one full-step excitation sequence) contains 4 full steps. Manufacturers normally specify resolution as physical angle per full step. On the Agito controller the number of steps per electrical cycle is defined by [StepBits](StepBits.md) (minimum 2, i.e. 4 full steps).

The number of position counts (for [PosRef](../10-motion/01-kinematics-status/PosRef.md), [AbsTrgt](../10-motion/13-motion-mode-ptp/AbsTrgt.md), etc.) per electrical cycle is $2^{StepBits}$.

The physical resolution is

$$Resolution\ \left\lbrack \frac{physical\ deg}{count} \right\rbrack = \ \frac{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}{2^{StepBits}}$$

and the number of counts per revolution is

$$Counts\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \bullet 2^{StepBits}}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}$$

In open-loop stepper control, no position feedback is used ([Pos](../10-motion/01-kinematics-status/Pos.md) = 0 and [PosErr](../10-motion/01-kinematics-status/PosErr.md) = 0). The user commands motion by changing the position reference ([PosRef](../10-motion/01-kinematics-status/PosRef.md)), which is used to determine the stepping currents for phases A and B and to track the stepper location.

The stepping currents are generated each control cycle from the position-within-electrical-cycle. The firmware masks `PosRef` to the cycle (`PosRef & (2^StepBits − 1)`), converts that to an electrical angle θ = position × 2π/2^StepBits, and sets the two phase-current references from a sine/cosine lookup scaled by the active stepping current ([StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md), held in the current reference):

$$IaRef = I \cdot \sin\theta \qquad IbRef = I \cdot \cos\theta$$

A 2-phase current loop then closes on Ia and Ib, producing phase voltages Va and Vb with **Vc = 0** (phase A/B returns are tied to the amplifier's C phase). The q/d (Park) components are unused for steppers and reported as zero.

### Closed-loop stepper (MotorType = 7)

Same 2-phase stepper hardware as above (3 pins; 4 full steps per electrical cycle; steps per electrical cycle defined by [StepBits](StepBits.md), minimum 2).

The number of steps per electrical cycle is $2^{StepBits}$ [step count].

The physical resolution is

$$Resolution\ \left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack = \ \frac{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}{2^{StepBits}}$$

and the number of steps per revolution is

$$Steps\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \bullet 2^{StepBits}}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$

In closed-loop stepper control, encoder feedback is used and position is defined in encoder counts (not step counts). Both the pole pairs per revolution ([PolePrs](PolePrs.md)) and the encoder count per revolution ([EncRes](../03-encoder/01-general-settings/EncRes.md)) must be provided. Only the position closed loop is used: [VelRef](../10-motion/01-kinematics-status/VelRef.md) is the sum of the position-loop output and the position derivative.

The controller pre-computes a *steps-per-count* factor

$$Steps\ per\ count = \frac{PolePrs \cdot 2^{StepBits}}{EncRes}$$

and each cycle converts `VelRef` (in count/s) to a step-count increment per sample, accumulates it into the stepper electrical-cycle position (wrapping within one electrical cycle), and then runs the **same** phase-current generation as open-loop stepper (mask to `2^StepBits − 1`, sine/cosine lookup scaled by the stepping current, then the Ia/Ib current loop with Vc = 0). A `MaxVel` that allows more than one electrical cycle of travel per control cycle is masked off, so set [MaxVel](../06-protections/03-motion/general-maximum-limits/MaxVel.md) sensibly.

## Examples

```text
AMotorType=4         ; rotary DC brushless motor
AMotorType=6         ; open-loop stepper motor
AMotorType          ; query the configured motor type
```

## See also

- [PolePrs](PolePrs.md) — pole pairs, required for brushless (3, 4) and closed-loop stepper (7) motors
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — encoder resolution, interpreted per motor type
- [StepBits](StepBits.md) — steps per electrical cycle for stepper motors (6, 7)
- [StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md) — stepper phase currents in motion / at standstill
- [AmpType](AmpType.md) — amplifier mode driving the motor
