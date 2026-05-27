---
keyword: ControlMode
summary: Bit-packed selection of current/voltage control options (SVM limit, vector vs phase, loop bypass, I2T action).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 109
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
  - 15
  default: null
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ControlMode

Bit-packed selection of current/voltage control options (SVM limit, vector vs phase, loop bypass, I2T action).

## Overview

`ControlMode` selects the current- and voltage-control options through individual bit assignments. It determines whether current control runs in the dq0 domain (vector control) or the abc domain (phase control), how much of the bus voltage the space-vector modulator may use, whether the current loop is bypassed, and what action the I2T protection takes when triggered. It works together with [MotorType](../../02-motor-and-amplifier/MotorType.md) and the current-control tuning (see [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md)). The dq0 outputs [Vd](Vd.md)/[Vq](Vq.md) versus abc outputs [Va](Va.md)/[Vb](Vb.md)/[Vc](Vc.md) depend on the bit 1 setting.

> **Documentation pending:** this keyword is marked `partial`; the default value is unspecified and behavior may change. Confirm bit defaults against firmware before relying on them.

## How it works

The bits are 0-based. Each bit defaults to 0 (reset).

| Bit | Function |
|---|---|
| 0 | **Space-vector modulation limit (enhanced speed range).** Default 0. If reset (0), the maximum line-to-line voltage is up to 0.75·VBus. If set (1), the maximum line-to-line voltage is up to 0.866·VBus. |
| 1 | **Vector control.** Default 0. If reset (0), current control is in the dq0 domain (vector control). If set (1), current control is in the abc domain (phase control). |
| 2 | **Current control loop bypass.** Default 0. If reset (0), the current control loop is used. If set (1), the loop is bypassed and the phase voltage references (for SVM) equal the phase current references — that is, [Va](Va.md) and [Vb](Vb.md) equal [IaRef](IaRef.md) and [IbRef](IbRef.md) respectively. |
| 3 | **Action taken for I2T protection.** Default 0. If reset (0), triggering I2T protection clamps the current reference at [ContCL](../../06-protections/02-current-and-voltage/ContCL.md) until the filtered I² value falls below (ContCL)². If set (1), triggering I2T protection disables the motor, reports an error code and records it to ErrLog. If the current control loop is bypassed (bit 2 set), triggering I2T protection always disables the motor regardless of this bit. |

## Examples

```text
ControlMode=2       ; bit 1 set: abc-domain (phase) current control
ControlMode=1       ; bit 0 set: allow line-to-line voltage up to 0.866*VBus
ControlMode?        ; read the current configuration
```

## See also

- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines applicable control domains
- [ContCL](../../06-protections/02-current-and-voltage/ContCL.md) — continuous current limit used by I2T protection
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs
- [Va](Va.md), [Vb](Vb.md), [Vc](Vc.md) — phase voltage commands
