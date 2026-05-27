---
keyword: AccelFact
summary: Scaling factor applied to Accel to adjust effective acceleration without changing Accel.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 168
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 40
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccelFact

Scaling factor applied to `Accel` to adjust effective acceleration without changing `Accel`.

## Overview

`AccelFact` is a multiplier on the base [Accel](Accel.md) value, so the effective acceleration used for motion is `Accel × AccelFact`. This lets you scale acceleration by a ratio (1 to 40) without disturbing the stored `Accel` parameter, which is convenient when one base profile must be sped up or slowed down. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

Effective acceleration = `Accel × AccelFact`.

## Examples

```text
AAccelFact=2         ; double the effective acceleration
AAccelFact          ; query current factor
```

## See also

- [Accel](Accel.md) — base acceleration that this factor multiplies
- [Decel](Decel.md) — deceleration rate
- [Speed](Speed.md) — target velocity
