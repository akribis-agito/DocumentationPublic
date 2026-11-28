---
keyword: MagneticPitch
summary: Linear brushless motor travel in millimetres per electrical period.
availability:
- controller
- ci-master
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
  range:
  - 0.0
  - 1000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# MagneticPitch

Linear brushless motor travel in millimetres per electrical period.

## Overview

CAN 849 is a per-axis parameter saved to flash, with a range of 0 to 1000 mm. It is available on Central-i and on standalone drives with the #1594 firmware change. Older standalone parameter files can omit it. The default of zero means the pitch is unconfigured.

For linear brushless motors, counts/mm = EncRes / MagneticPitch when the pitch is positive. For example, 3250 counts per period and 32.5 mm per period gives 100 counts/mm. Rotary and voice-coil encoder conventions are unchanged.

## How it works

The back-EMF feed-forward predicts the voltage needed to overcome the motor's generated voltage, which is proportional to mechanical speed. For a linear motor the back-EMF constant ([BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md)) is specified per metre-per-second, but the controller measures speed in encoder counts per second. `MagneticPitch` together with the encoder resolution [EncRes](../03-encoder/01-general-settings/EncRes.md) provides the conversion:

$$\text{speed in m/s} = \text{speed in counts/s} \cdot \frac{\text{MagneticPitch}\,[\text{mm}] \cdot 10^{-3}}{\text{EncRes}}$$

where [EncRes](../03-encoder/01-general-settings/EncRes.md) is the number of counts per magnetic period. The result feeds the back-EMF voltage term.

## Examples

```text
AMagneticPitch=24       ; linear motor with a 24 mm magnetic pitch
AMagneticPitch          ; read the configured magnetic pitch (mm)
```

## See also

- [MotorType](MotorType.md) — `MagneticPitch` applies only to linear motors
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — counts per magnetic period, paired with `MagneticPitch` in the conversion
- [BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md) — back-EMF constant the converted speed multiplies
