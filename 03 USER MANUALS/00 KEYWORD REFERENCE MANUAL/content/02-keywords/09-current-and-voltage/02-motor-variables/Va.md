---
keyword: Va
summary: Read-only phase A voltage reference for space-vector modulation (PWM-count fraction ×1000).
availability:
  standalone:
  - v4
  central-i:
  - v4
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
  scaling: 1.0
  implemented: final
overrides: {}
---
# Va

Read-only phase A voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Va` is the phase A voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000. Phase A is defined in the hardware reference guide. Together with [Vb](Vb.md) and [Vc](Vc.md) it forms the three-phase voltage commands sent to the modulator. In dq0-domain control these are produced from [Vd](Vd.md)/[Vq](Vq.md) by the inverse Park transform; if the current loop is bypassed (see [ControlMode](ControlMode.md) bit 2), `Va` and `Vb` equal [IaRef](IaRef.md) and [IbRef](IbRef.md).

## Examples

```text
AVa                 ; read phase A SVM voltage reference
```

## See also

- [Vb](Vb.md), [Vc](Vc.md) — phase B and C voltage references
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [ControlMode](ControlMode.md) — control-domain and loop-bypass options
