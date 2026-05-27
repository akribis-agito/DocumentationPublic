---
keyword: VEncDelay
summary: Fixed delay between the source signal and the virtual encoder output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 616
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
  - 25
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncDelay

Fixed delay between the source signal and the virtual encoder output.

## Overview

`VEncDelay` introduces a fixed delay between the source signal ([VEncSrc](VEncSrc.md)) and the virtual encoder output. It can be used to compensate for latency in the feedback path or to synchronise the virtual encoder with an external process. The value range is 0 to 25, with a default of 0 (no delay). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## Examples

```text
AVEncDelay=0         ; no delay
AVEncDelay=5         ; apply a fixed delay
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source signal that is delayed
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
