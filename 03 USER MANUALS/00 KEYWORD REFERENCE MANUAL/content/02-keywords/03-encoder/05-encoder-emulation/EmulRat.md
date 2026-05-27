---
keyword: EmulRat
summary: Ratio between feedback encoder counts and the quadrature pulses emitted on the emulation output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 69
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
  - -65536
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulRat

Ratio between feedback encoder counts and the quadrature pulses emitted on the emulation output.

## Overview

`EmulRat` sets the ratio between the feedback encoder counts and the quadrature pulses output on the encoder emulation interface. Setting this value to N causes the controller to emit one A/B quadrature step for every N feedback encoder counts, allowing the emulated output to match a downstream device's expected resolution. It works together with [EmulFilter](EmulFilter.md) (output filtering) and [EmulIndexType](EmulIndexType.md) (index pulse type), and relates to the feedback resolution set by [EncRes](../01-general-settings/EncRes.md). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## Examples

```text
AEmulRat=4           ; one quadrature step per 4 feedback counts
```

## See also

- [EmulFilter](EmulFilter.md) — filter applied to the emulated output
- [EmulIndexType](EmulIndexType.md) — index pulse type on the emulated output
- [EncRes](../01-general-settings/EncRes.md) — feedback encoder resolution
