---
keyword: FricQSCHold
summary: Hold-off before the quadrant-switching kick, in µs (renamed from FricQSCDelay, which was in samples).
availability:
  standalone: []
  central-i:
  - v5
can_code: 940
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
  - 250000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricQSCHold

Hold-off before the quadrant-switching kick, in µs (renamed from FricQSCDelay, which was in samples).

## Overview

`FricQSCHold` delays the quadrant-switching kick after the velocity leaves the band, in microseconds. Available on AGM800 and AGM800-EC (central-i v5). The range is 0 to 250 000 µs and the default is 0 (no delay). It replaces `FricQSCDelay` from 5.3.0-rc4 (same CAN code).

## How it works

The velocity right after a zero crossing is the least reliable part of the move; a short hold-off avoids kicking in a direction that is about to change again. The value is rounded to whole control cycles.

**Units changed.** `FricQSCDelay` counted control cycles; `FricQSCHold` is in microseconds, so the setting means the same time on every product. A value saved under rc4 is read as microseconds, which is a different (much shorter) delay: re-enter it. It only matters when [FricQSCOn](FricQSCOn.md) = 1.

## Examples

```text
AFricQSCHold=500   ; wait 0.5 ms after leaving the band before kicking
```

## See also

- [FricQSCOn](FricQSCOn.md)
- [FricQSCTime](FricQSCTime.md)
