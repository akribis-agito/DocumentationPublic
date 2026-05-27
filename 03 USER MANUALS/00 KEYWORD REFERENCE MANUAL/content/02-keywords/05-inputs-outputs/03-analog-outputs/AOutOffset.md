---
keyword: AOutOffset
summary: Offset (mV) added to the analog output, used to calibrate/zero it.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 227
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -500
  - 500
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - -700
    - 700
---
# AOutOffset

Offset (mV) added to the analog output, used to calibrate/zero it.

## Overview

`AOutOffset` adds a fixed offset, in millivolts, to the analog output — applied after scaling but before the millivolt-to-DAC-code conversion of the [analog-output signal path](00-overview.md). The array index is the analog-output number (1-based: `AOutOffset[1]` is analog output 1). Use it to calibrate or zero the output of a channel.

## How it works

`AOutOffset` is applied in both output modes, before the value is converted to a DAC code and clamped:

- **Direct mode:** `DAC code = (AOutPort + AOutOffset) × (mV-to-DAC factor)`.
- **Monitoring mode:** `DAC code = ((parameter << AOutShifts) + AOutOffset) × (mV-to-DAC factor)`.

Because the offset is added in the same millivolt units as the (scaled) value and only then scaled by the mV-to-DAC factor (−2.752457 LSB/mV), one unit of `AOutOffset` shifts the output by 1 mV. The narrow range (±500 mV on v4) is enough for calibration/zeroing, not for large signal offsets.

## Examples

```text
AAOutOffset[1]=-12   ; trim analog output 1 by -12 mV to zero it
AAOutOffset[1]        ; read back the offset
```

## Changes between versions

On Central-i v5 `AOutOffset` is a `float32` and the range widens to ±700 mV (v4 / standalone: `int32`, ±500 mV). The role and signal-path position are unchanged.

## See also

- [AOutPort](AOutPort.md) — commanded value (direct mode); offset is added to it
- [AOutShifts](AOutShifts.md) — scaling applied before the offset (monitoring mode)
- [analog-output overview](00-overview.md) — full signal path
