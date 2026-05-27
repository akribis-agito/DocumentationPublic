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

`Vc` is the phase C voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000. Phase C is defined in the hardware reference guide. Together with [Va](Va.md) and [Vb](Vb.md) it forms the three-phase voltage commands sent to the modulator. In dq0-domain control these are produced from [Vd](Vd.md)/[Vq](Vq.md) by the inverse Park transform.

## Examples

```text
AVc                 ; read phase C SVM voltage reference
```

## See also

- [Va](Va.md), [Vb](Vb.md) — phase A and B voltage references
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [ControlMode](ControlMode.md) — control-domain and loop-bypass options
