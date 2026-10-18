---
keyword: FricQSCOn
summary: Enables quadrant-switching compensation (a breakaway kick at reversals and starts).
availability:
  standalone: []
  central-i:
  - v5
can_code: 938
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
# FricQSCOn

Enables quadrant-switching compensation (a breakaway kick at reversals and starts).

## Overview

`FricQSCOn` = 1 adds a short breakaway kick each time the axis starts moving or reverses. Available on AGM800 and AGM800-EC (central-i v5). The default is 0 (off).

## How it works

When the velocity feedback leaves the band ([FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md)) in a new direction, and after the hold-off [FricQSCHold](FricQSCHold.md), the stage adds a kick of about |[FricIStatPos](FricIStatPos.md)| − |[FricIPos](FricIPos.md)| (or the negative-side pair) that decays with the time constant [FricQSCTime](FricQSCTime.md). The kick carries only the breakaway excess; the sliding level comes from the selected [FricMethod](FricMethod.md).

The kick is added on top of methods 0 to 3. It is skipped for methods 4 and 5, which already contain the breakaway level. Its output is part of the stage, so [FricLim](FricLim.md) clamps it too.

## Examples

```text
AFricQSCOn=1       ; add the breakaway kick
```

## See also

- [FricQSCTime](FricQSCTime.md)
- [FricQSCHold](FricQSCHold.md)
- [Friction feedforward](00-overview.md)
