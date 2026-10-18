---
keyword: FricViscous
summary: 'Viscous friction slope: extra current per count/s of velocity feedback.'
availability:
  standalone: []
  central-i:
  - v5
can_code: 932
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
  - -1.0
  - 1.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricViscous

Viscous friction slope: extra current per count/s of velocity feedback.

## Overview

`FricViscous` adds a current proportional to speed, for friction that grows with velocity (lubricant drag, seals). It is in mA per count/s. Available on AGM800 and AGM800-EC (central-i v5).

## How it works

The stage adds `FricViscous` × velocity feedback to methods 1, 2, 3 and 5. It always uses the velocity feedback, whatever [FricVelSrc](FricVelSrc.md) says. LuGre (method 4) uses it as its viscous coefficient (σ2). The default is 0 (no viscous term).

Tune it last, after the offset and the per-direction levels: run the axis at a few constant speeds and set the slope so the remaining current no longer grows with speed.

## Examples

```text
AFricViscous=0.002   ; 2 mA extra per 1000 counts/s
```

## See also

- [FricMethod](FricMethod.md)
- [Friction feedforward](00-overview.md) — tuning order
