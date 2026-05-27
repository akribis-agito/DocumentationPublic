---
keyword: RefOffsetSamp
summary: Number of servo samples over which a reference position offset is ramped in.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 165
attributes:
  access: rw
  scope: axis
  flash: false
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
# RefOffsetSamp

Number of servo samples over which a reference position offset is ramped in.

## Overview

`RefOffsetSamp` sets the number of servo samples over which a reference offset is applied when ramping in a position correction. It works together with [RefOffsetStep](RefOffsetStep.md), which sets the per-sample offset magnitude, so the two together control how gradually a position correction is introduced into the reference trajectory. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## Examples

```text
ARefOffsetSamp=100   ; spread the offset over 100 servo samples
ARefOffsetSamp      ; query current value
```

## See also

- [RefOffsetStep](RefOffsetStep.md) — per-sample offset magnitude
