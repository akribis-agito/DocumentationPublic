---
keyword: VEncSrc
summary: Selects the source signal used to generate the virtual encoder position.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 614
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncSrc

Selects the source signal used to generate the virtual encoder position.

## Overview

`VEncSrc` selects the source signal used to generate the virtual encoder output. The chosen source is formatted by [VEncType](VEncType.md), scaled by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), and delayed by [VEncDelay](VEncDelay.md) to produce the virtual encoder position used when the virtual encoder is enabled ([VEncOn](VEncOn.md) = 1). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

> **Documentation pending:** the mapping of `VEncSrc` values to specific source signals is not documented here.

## Examples

```text
AVEncSrc            ; query the configured virtual encoder source
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncType](VEncType.md) — output format of the virtual encoder
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
