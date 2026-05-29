---
keyword: MagneticPitch
summary: "Linear-motor magnetic pitch in millimetres, used to convert speed from counts/s to m/s for the back-EMF feed-forward."
availability:
  standalone: []
  central-i:
  - v5
can_code: 849
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
# MagneticPitch

Linear-motor magnetic pitch in millimetres, used to convert speed from counts/s to m/s for the back-EMF feed-forward.

## Overview

`MagneticPitch` is the magnetic pitch of a **linear** motor — the physical distance, in millimetres, of one magnetic period of the motor's magnet track. The controller uses it only to relate the motor's mechanical speed to its encoder count rate, which is needed when the back-EMF feed-forward is enabled. It has no effect on rotary motors.

It is a per-axis parameter saved to flash. The value is in millimetres, with a usable range of 0 to 1000 mm and a default of 0. A value of 0 means the conversion is effectively not configured, so set it to the motor's actual magnetic pitch when using a linear motor with back-EMF feed-forward.

> Available from v5 (Central-i) only.

## How it works

The back-EMF feed-forward predicts the voltage needed to overcome the motor's generated voltage, which is proportional to mechanical speed. For a linear motor the back-EMF constant ([BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md)) is specified per metre-per-second, but the controller measures speed in encoder counts per second. `MagneticPitch` together with the encoder resolution [EncRes](../03-encoder/01-general-settings/EncRes.md) provides the conversion:

$$\text{speed in m/s} = \text{speed in counts/s} \cdot \frac{\text{MagneticPitch}\,[\text{mm}] \cdot 10^{-3}}{\text{EncRes}}$$

where [EncRes](../03-encoder/01-general-settings/EncRes.md) is the number of counts per magnetic period. The result feeds the back-EMF voltage term. Because it only scales that term, `MagneticPitch` matters only when the back-EMF feed-forward is in use on a linear motor; it is ignored for other [MotorType](MotorType.md) settings (rotary and voice-coil motors use their own conversions).

## Examples

```text
AMagneticPitch=24       ; linear motor with a 24 mm magnetic pitch
AMagneticPitch          ; read the configured magnetic pitch (mm)
```

## See also

- [MotorType](MotorType.md) — `MagneticPitch` applies only to linear motors
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — counts per magnetic period, paired with `MagneticPitch` in the conversion
- [BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md) — back-EMF constant the converted speed multiplies
