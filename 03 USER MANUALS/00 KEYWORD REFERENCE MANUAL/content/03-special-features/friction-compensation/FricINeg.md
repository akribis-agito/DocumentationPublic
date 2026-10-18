---
keyword: FricINeg
summary: Coulomb (sliding) friction level for the negative direction, in mA.
availability:
  standalone: []
  central-i:
  - v5
can_code: 929
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
# FricINeg

Coulomb (sliding) friction level for the negative direction, in mA.

## Overview

`FricINeg` is the friction current needed to keep the axis moving in the negative direction once it is past the band. It is in mA. Available on AGM800 and AGM800-EC (central-i v5).

## How it works

Methods 1, 2 and 3 use `FricINeg` as a signed level: normally negative. Methods 4 and 5 use its size only and take the sign from the direction of travel. Quadrant-switching compensation uses it to work out the breakaway excess (|[FricIStatNeg](FricIStatNeg.md)| − |FricINeg|).

Do not use this level to carry gravity or another constant offset; put that in [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md) and keep `FricINeg` for friction only.

The keyword is set separately for each direction, so an axis that is lighter one way than the other can be matched. Values saved under 5.3.0-rc4 are not converted. After upgrading from rc4, re-enter the friction settings.

## Examples

```text
AFricINeg=-120     ; negative-direction Coulomb level, mA
```

## See also

- [FricIPos](FricIPos.md) — the same level for the other direction
- [FricMethod](FricMethod.md)
- [Friction feedforward](00-overview.md) — tuning order
