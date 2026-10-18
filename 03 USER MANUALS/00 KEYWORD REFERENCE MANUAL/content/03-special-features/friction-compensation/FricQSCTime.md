---
keyword: FricQSCTime
summary: Decay time constant of the quadrant-switching kick, in µs.
availability:
  standalone: []
  central-i:
  - v5
can_code: 939
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
  - 100
  - 1000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricQSCTime

Decay time constant of the quadrant-switching kick, in µs.

## Overview

`FricQSCTime` sets how quickly the quadrant-switching kick dies away, in microseconds. Available on AGM800 and AGM800-EC (central-i v5). The range is 100 to 1 000 000 µs and the default is 5000 µs (5 ms).

## How it works

After a start or reversal the kick falls by about 63 % every `FricQSCTime`. Keep it short: the kick should be gone before the axis has travelled far, or it turns into an overshoot of its own. It only matters when [FricQSCOn](FricQSCOn.md) = 1.

## Examples

```text
AFricQSCTime=3000  ; kick decays with a 3 ms time constant
```

## See also

- [FricQSCOn](FricQSCOn.md)
- [FricQSCHold](FricQSCHold.md)
