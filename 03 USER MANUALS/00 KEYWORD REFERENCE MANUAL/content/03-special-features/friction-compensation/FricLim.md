---
keyword: FricLim
summary: Clamp on the whole friction stage, in % of PeakCL (renamed from StribLim).
availability:
  standalone: []
  central-i:
  - v5
can_code: 925
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 40
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricLim

Clamp on the whole friction stage, in % of PeakCL (renamed from StribLim).

## Overview

`FricLim` limits the friction feedforward current to ±`FricLim` % of [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md). Available on AGM800 and AGM800-EC (central-i v5). It replaces `StribLim` from 5.3.0-rc4 (same CAN code). The range is 0 to 100 and the default is 40. It cannot be changed while the axis is in motion.

## How it works

The clamp acts on the total output of the stage — the selected model plus any quadrant-switching kick — before it is added to the feedforward path. It follows `PeakCL`: if you change `PeakCL`, the clamp changes with it. `FricLim=0` turns the friction output off.

The clamp acts before the feedforward filter. With [FFFiltOn](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltOn.md) = 1 and a filter that peaks above unity gain, the filtered friction can briefly go past `FricLim`.

The firmware does not report when the clamp is limiting. `FricLim` is kept as it is for now; whether the friction stage needs its own clamp at all is an open question (Firmware-Main #1423).

## Examples

```text
AFricLim=40        ; friction current limited to 40 % of PeakCL
```

## See also

- [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md)
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — index 6 shows the clamped friction current
- [Friction feedforward](00-overview.md)
