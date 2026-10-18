---
keyword: FricIStatNeg
summary: Breakaway (static) friction level for the negative direction, in mA.
availability:
  standalone: []
  central-i:
  - v5
can_code: 934
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
  - -64000
  - 64000
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricIStatNeg

Breakaway (static) friction level for the negative direction, in mA.

## Overview

`FricIStatNeg` is the current needed to break the axis free and start it moving in the negative direction. It is an absolute level in mA, not an extra on top of the Coulomb level. Available on AGM800 and AGM800-EC (central-i v5).

## How it works

Methods 4 (LuGre) and 5 (Stribeck) start from this level at low speed and fade to the Coulomb level ([FricINeg](FricINeg.md)) as the speed passes [FricVStribNeg](FricVStribNeg.md). They use its size only. Quadrant-switching compensation ([FricQSCOn](FricQSCOn.md)) uses the difference |`FricIStatNeg`| − |FricINeg| as the size of its kick. Methods 1 to 3 do not use it.

Set it at or above the Coulomb level; a value below the Coulomb level is treated as equal to it.

The keyword is set separately for each direction, so an axis that is lighter one way than the other can be matched. Values saved under 5.3.0-rc4 are not converted. After upgrading from rc4, re-enter the friction settings.

## Examples

```text
AFricIStatNeg=-180  ; negative-direction breakaway level, mA
```

## See also

- [FricIStatPos](FricIStatPos.md) — the same level for the other direction
- [FricMethod](FricMethod.md)
- [Friction feedforward](00-overview.md) — tuning order
