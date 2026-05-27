---
keyword: MapErrOffRamp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 454
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
  - 1
  - 2147483647
  default: 16384
  scaling: 1.0
  implemented: final
overrides: {}
summary: Rate at which the map error offset ramps toward its target.
---
# MapErrOffRamp

Rate at which the map error offset ramps toward its target.

## Overview

`MapErrOffRamp` sets the slew rate at which the *applied* offset converges to the [MapErrOffset](MapErrOffset.md) target. Slewing the offset rather than applying it as a step avoids an abrupt position jump in the corrected feedback. A higher value converges faster. It is distinct from [MapErrOnStep](MapErrOnStep.md), which controls the separate engage/disengage ramp of the whole correction, and [MapType](MapType.md), which enables the mapping.

It is an axis-scoped parameter saved to flash and can be changed at any time, including during motion.

## How it works

The rate is in **encoder counts per second**. Each control cycle the controller moves the applied offset toward the [MapErrOffset](MapErrOffset.md) target by `MapErrOffRamp × SampleTime` counts (i.e. `MapErrOffRamp / (samples per second)` counts per cycle), clamping exactly onto the target on the cycle it would overshoot. The default `16384` equals one sampling-rate unit, so at the base sample rate the offset moves about 16384 counts per second. Setting a small value makes a deliberate, slow trim; a large value approaches a step.

## Examples

```text
AMapErrOffRamp=16384 ; default slew rate (~16384 counts/s at base rate)
AMapErrOffRamp       ; read the current slew rate
```

## See also

- [MapErrOffset](MapErrOffset.md) — the target offset this keyword slews toward
- [MapErrOnStep](MapErrOnStep.md) — separate engage/disengage ramp of the whole correction
- [MapType](MapType.md) — enables the error mapping
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback affected by the offset
