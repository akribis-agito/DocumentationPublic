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

`MapErrOnStep` controls the **engage/disengage ramp** of the error-mapping correction — how the whole correction (table value plus the [MapErrOffset](MapErrOffset.md) component) fades in when [MapType](MapType.md) becomes non-zero and fades out when it returns to zero. Ramping prevents a position step in the feedback at the moment mapping is switched on or off. It is separate from [MapErrOffRamp](MapErrOffRamp.md), which slews only the offset. The valid range is `0` to `16384`.

It is an axis-scoped parameter saved to flash and can be changed at any time, including during motion.

## How it works

The controller maintains a ramp **counter** that runs from `0` (correction off) up to a full-scale value equal to the controller's samples-per-second. The applied correction is scaled by `counter / (samples per second)`, so the counter is effectively a 0…1 blend factor between the uncorrected feedback and the fully-corrected feedback. `MapErrOnStep` is the amount the counter changes **per control cycle**:

- **Engaging** ([MapType](MapType.md) set 1/2/3): the counter increments by `MapErrOnStep` each cycle until it saturates at full scale.
- **Disengaging** ([MapType](MapType.md) set 0): the counter decrements by `MapErrOnStep` each cycle; when it reaches 0 the internal mapping type reverts to off.
- **`MapErrOnStep = 0` (default):** the counter jumps straight to full scale on engage / to 0 on disengage — an immediate, single-cycle switch (no ramp).

Larger steps engage faster; the maximum (`16384`) at the base sample rate fully engages in roughly one second. Because full scale equals samples-per-second, a step of `N` engages over about `(samples per second) / N` cycles.

## Examples

```text
AMapErrOnStep=0      ; default: switch correction in/out immediately
AMapErrOnStep=16     ; gentle fade-in over ~ (samples/s)/16 cycles
AMapErrOnStep        ; read the current step size
```

## See also

- [MapErrOffset](MapErrOffset.md) — constant offset added to the correction
- [MapErrOffRamp](MapErrOffRamp.md) — slew rate of that offset
- [MapType](MapType.md) — enables the error mapping (its change drives this ramp)
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback that ramps in/out
