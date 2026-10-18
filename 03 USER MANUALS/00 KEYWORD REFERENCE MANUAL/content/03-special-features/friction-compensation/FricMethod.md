---
keyword: FricMethod
summary: Selects the friction feedforward model (0 = off, 1 to 5).
availability:
  standalone: []
  central-i:
  - v5
can_code: 926
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
  - 0
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricMethod

Selects the friction feedforward model (0 = off, 1 to 5).

## Overview

`FricMethod` selects how the friction feedforward stage turns velocity into a current. Available on AGM800 and AGM800-EC (central-i v5). It is one stage: whichever model you choose, its output goes through the same clamp ([FricLim](FricLim.md)) and the same feedforward path (see [Friction feedforward](00-overview.md)).

| `FricMethod` | Model | What it does |
|---|---|---|
| 0 | Off (default) | No friction feedforward. |
| 1 | Linear | Ramps from 0 to the Coulomb level across the band, then holds the level. No memory. |
| 2 | Hysteresis | Switches between the two Coulomb levels when the velocity leaves the band. Remembers the last level inside the band. |
| 3 | Play | Like 2, but the switch is a ramp across the band instead of a jump. |
| 4 | LuGre | A bristle model with internal state. Uses the Coulomb and breakaway levels, the Stribeck velocities and the bristle parameters. |
| 5 | Stribeck | A smooth Coulomb level plus a breakaway hump that fades with speed. No memory. |

## How it works

Method 5 computes, for velocity $v$:

$$
I = \operatorname{sign}(v)\cdot\tanh\!\left(\frac{|v|}{V_{band}}\right)\cdot\left(F_c + (F_s - F_c)\,e^{-(v/V_s)^2}\right) + \text{FricViscous}\cdot v_{fb}
$$

with, for the direction of travel:

- $F_c$ = Coulomb level: [FricIPos](FricIPos.md) or [FricINeg](FricINeg.md) (as a magnitude)
- $F_s$ = breakaway level: [FricIStatPos](FricIStatPos.md) or [FricIStatNeg](FricIStatNeg.md) (as a magnitude)
- $V_{band}$ = [FricVBandPos](FricVBandPos.md) or [FricVBandNeg](FricVBandNeg.md): how quickly the output builds up through zero velocity
- $V_s$ = [FricVStribPos](FricVStribPos.md) or [FricVStribNeg](FricVStribNeg.md): the speed over which the breakaway hump fades to the Coulomb level
- $v$ comes from [FricVelSrc](FricVelSrc.md); $v_{fb}$ is always the velocity feedback.

Method 5 replaces the separate Stribeck feedforward of 5.3.0-rc4 (`StribOn` and the `Strib*` keywords). Quadrant-switching compensation ([FricQSCOn](FricQSCOn.md)) is added on top of methods 0 to 3 only; methods 4 and 5 already contain the breakaway level.

The range is 0 to 5. Values saved under 5.3.0-rc4 are not converted. After upgrading from rc4, re-enter the friction settings.

## Examples

```text
AFricMethod=5      ; Stribeck model
AFricMethod=0      ; friction feedforward off
```

## See also

- [Friction feedforward](00-overview.md) — the whole stage, tuning order and rc4 changes
- [FricLim](FricLim.md) — clamp on the stage output
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — read back the friction current (index 6)
