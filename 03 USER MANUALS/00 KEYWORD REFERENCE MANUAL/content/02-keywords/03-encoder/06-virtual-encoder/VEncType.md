---
keyword: VEncType
summary: Sets the output format or signal type of the virtual encoder.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 615
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncType

Sets the output format or signal type of the virtual encoder.

## Overview

`VEncType` sets the output format or signal type for the virtual encoder. Different values select the encoding mode used when the virtual encoder position (built from [VEncSrc](VEncSrc.md), [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), and [VEncDelay](VEncDelay.md)) is emitted. The value range is 0 to 1, with a default of 0. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

> **Documentation pending:** the exact behaviour of each option value (0 and 1) is not documented here.

## Examples

```text
AVEncType=0          ; default virtual encoder output format
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source signal for the virtual encoder
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
