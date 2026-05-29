---
keyword: ComtAng
summary: Read-only instantaneous commutation (electrical) angle of the motor, in degrees scaled by 100.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 73
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtAng

Read-only instantaneous commutation (electrical) angle of the motor, in degrees scaled by 100.

## Overview

`ComtAng` reports the instantaneous commutation angle (the motor electrical angle) used by the controller to drive the phase currents of a DC brushless motor. The value is expressed in degrees scaled by 100 and wraps between a lower limit of 0 and an upper limit of 35999 (i.e. 0.00°–359.99°).

Commutation keeps the applied current vector offset from the magnetic field so that force/torque is produced efficiently as the motor moves. `ComtAng` is the angle the controller is currently using; it is established by the commutation process configured through [ComtMode](ComtMode.md) and monitored through [ComtStatus](ComtStatus.md). The angle source depends on the configured method (for example Hall sensors via [HallsAngle](HallsAngle.md) / [HallsValue](HallsValue.md), or encoder-based feedback). Being read-only, axis-scope, and not flash-saved, it can be queried at any time, including while the motor is on or in motion.

## How it works

Each control cycle the controller computes the electrical angle from the active source, then reports it here in hundredths of a degree:

$$
\text{ComtAng} = \mathrm{round}\!\left(\theta_{elec}\;[\text{rad}] \times \frac{360}{2\pi} \times 100\right)
$$

For encoder-based commutation the angle comes from the feedback position within one electrical cycle (counts per electrical cycle = [EncRes](../03-encoder/01-general-settings/EncRes.md) / [PolePrs](../02-motor-and-amplifier/PolePrs.md), see [MotorType](../02-motor-and-amplifier/MotorType.md)); for Hall-based methods it comes from the [HallsValue](HallsValue.md) → [HallsAngle](HallsAngle.md) mapping (optionally smoothed by [HallOnlyFilt](HallOnlyFilt.md)). The reported value is meaningful only once commutation has completed (commutation-complete bit of [StatReg](../07-status-and-faults/StatReg.md), bit 0; [ComtStatus](ComtStatus.md) = `100`). `ComtAng` is reported for brushless motor types only; brush, voice-coil, simulation, and stepper types have no commutation angle.

## Examples

```text
AComtAng            ; query the instantaneous commutation angle (deg x100)
```

## See also

- [ComtMode](ComtMode.md) — commutation settings that determine how the angle is established
- [ComtStatus](ComtStatus.md) — reports the commutation process status
- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [HallsValue](HallsValue.md) — current raw Hall sensor state
- [StatReg](../07-status-and-faults/StatReg.md) — bit 0 reports commutation complete (this angle is valid once set)
