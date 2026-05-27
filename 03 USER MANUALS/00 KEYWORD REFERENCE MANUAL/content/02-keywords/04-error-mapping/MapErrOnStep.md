---
keyword: MapErrOnStep
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 476
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
  - 16384
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Step size used to apply the map correction when mapping engages.
---
# MapErrOnStep

Step size used to apply the map correction when mapping engages.

## Overview

`MapErrOnStep` sets the incremental step size used when the error-mapping correction is brought in gradually instead of in a single jump. This smooths the transition when mapping is activated, controlling how quickly the correction converges. It complements [MapErrOffRamp](MapErrOffRamp.md) (ramp rate of the applied offset) and acts on [MapErrOffset](MapErrOffset.md) (the offset currently in effect). The mapping itself is enabled by [MapType](MapType.md). The valid range is `0` to `16384`, where `0` (the default) applies no incremental stepping.

It is an axis-scoped parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
AMapErrOnStep=0      ; default: no incremental stepping
AMapErrOnStep=1000   ; bring the correction in 1000 counts at a time
AMapErrOnStep       ; query the current step size
```

## See also

- [MapErrOffset](MapErrOffset.md) — the offset that steps in
- [MapErrOffRamp](MapErrOffRamp.md) — ramp rate of the applied offset
- [MapType](MapType.md) — enables the error mapping
