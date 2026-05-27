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
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# Vb

Read-only phase B voltage reference for space-vector modulation (PWM-count fraction ×1000).

## Overview

`Vb` is the phase B voltage reference for space-vector modulation (SVM), expressed as a fraction of the full PWM count times a factor of 1000. Phase B is defined in the hardware reference guide. Together with [Va](Va.md) and [Vc](Vc.md) it forms the three-phase voltage commands sent to the modulator. In dq0-domain control these are produced from [Vd](Vd.md)/[Vq](Vq.md) by the inverse Park transform.

## Examples

```text
AVb                 ; read phase B SVM voltage reference
```

## See also

- [Va](Va.md), [Vc](Vc.md) — phase A and C voltage references
- [Vd](Vd.md), [Vq](Vq.md) — dq0 voltage outputs that form Va/Vb/Vc
- [ControlMode](ControlMode.md) — control-domain and loop-bypass options
