---
keyword: FricVBandPos
summary: Zero-crossing band on the positive side, in counts/s (renamed from FricVBlindPos).
availability:
  standalone: []
  central-i:
  - v5
can_code: 930
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
# FricVBandPos

> **AGM800-EC** — The keyword conversion uses the 16,000 Hz control rate and an internal-to-external factor of `1.024`. Reads divide by this factor; accepted writes multiply by it, with rounding for integer values. See [AGM800-EC timing and units](../../02-keywords/01-system/03-timing/AGM800-EC-units.md).

Zero-crossing band on the positive side, in counts/s (renamed from FricVBlindPos).

## Overview

`FricVBandPos` sets how far into the positive side the velocity must go before the friction stage gives the full level. It is in counts/s and is entered as a positive number. Available on AGM800 and AGM800-EC (central-i v5). It replaces `FricVBlindPos` from 5.3.0-rc4 (same CAN code).

## How it works

Near zero velocity the direction of travel is uncertain, and this band says how the stage handles it:

| Method | Use of `FricVBandPos` |
|---|---|
| 1 (linear) | Width of the ramp from 0 to the Coulomb level |
| 2 (hysteresis) | Velocity at which the level switches to the positive side |
| 3 (play) | Width of the ramp that leads to the positive-side level |
| 5 (Stribeck) | Width of the smooth (tanh) build-up through zero |
| Quadrant switching | Dead band: no kick until the velocity leaves the band |

LuGre (method 4) does not use the band; it uses [FricVStribPos](FricVStribPos.md). A band of 0 means "switch at zero velocity". Values saved under 5.3.0-rc4 are not converted. After upgrading from rc4, re-enter the friction settings.

## Examples

```text
AFricVBandPos=200      ; full level once the velocity passes 200 counts/s
```

## See also

- [FricVBandNeg](FricVBandNeg.md) — band on the other side
- [FricVStribPos](FricVStribPos.md) — Stribeck velocity (a different thing)
- [Friction feedforward](00-overview.md)
