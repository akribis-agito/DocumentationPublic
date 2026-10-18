---
keyword: FricVStribNeg
summary: Stribeck velocity for the negative direction, in counts/s (methods 4 and 5).
availability:
  standalone: []
  central-i:
  - v5
can_code: 922
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricVStribNeg

> **AGM800-EC** — The keyword conversion uses the 16,000 Hz control rate and an internal-to-external factor of `1.024`. Reads divide by this factor; accepted writes multiply by it, with rounding for integer values. See [AGM800-EC timing and units](../../02-keywords/01-system/03-timing/AGM800-EC-units.md).

Stribeck velocity for the negative direction, in counts/s (methods 4 and 5).

## Overview

`FricVStribNeg` is the speed, in the negative direction, over which the breakaway level fades down to the Coulomb level. It is in counts/s and is entered as a positive number. Available on AGM800 and AGM800-EC (central-i v5). It is new in 5.3.0 (CAN code 922, which carried `StribEps` in rc4).

## How it works

Methods 4 (LuGre) and 5 (Stribeck) use the curve

$$
F_c + (F_s - F_c)\,e^{-(v/V_s)^2}
$$

where $V_s$ is `FricVStribNeg`, $F_s$ is [FricIStatNeg](FricIStatNeg.md) and $F_c$ is [FricINeg](FricINeg.md). At $v = V_s$ about 37 % of the breakaway excess is left; by $2V_s$ it is under 2 %. A small value gives a short, sharp breakaway; a large value keeps the extra current on for longer. A value of 0 removes the hump (the output is the Coulomb level as soon as the axis moves).

The band ([FricVBandNeg](FricVBandNeg.md)) and the Stribeck velocity are separate settings: the band covers the zero crossing, the Stribeck velocity covers the breakaway. Methods 1 to 3 do not use `FricVStribNeg`.

## Examples

```text
AFricVStribNeg=3000     ; breakaway hump fades over about 3000 counts/s
```

## See also

- [FricVStribPos](FricVStribPos.md) — Stribeck velocity for the other direction
- [FricMethod](FricMethod.md) — method 5 equation
- [Friction feedforward](00-overview.md)
