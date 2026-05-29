---
keyword: MapErrOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 411
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Current position-error offset applied on top of the map correction.
---
# MapErrOffset

Current position-error offset applied on top of the map correction.

## Overview

`MapErrOffset` is a **target** position-error offset (in encoder counts) added to the interpolated map correction. It lets you bias the corrected position by a constant on top of whatever the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) produces — for example to trim a residual offset without re-measuring the map. The mapping itself is enabled by [MapType](MapType.md).

It is an axis-scoped parameter, not saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

The value you write is the **target**; the firmware does not apply it as a step. Internally it keeps a separate *actual* offset that slews toward `MapErrOffset` by a fixed amount each control cycle:

$$
\text{actual} \mathrel{+}= \text{MapErrOffRamp} \cdot \text{SampleTime} \quad \text{(toward the target, clamped on arrival)}
$$

So [MapErrOffRamp](MapErrOffRamp.md) sets the slew rate (counts per second) and `MapErrOffset` sets the destination. Each cycle the *actual* offset is added to the interpolated correction, and the sum is then scaled by the engage ramp (see [MapErrOnStep](MapErrOnStep.md)) before being added to the feedback to form [Pos](../10-motion/01-kinematics-status/Pos.md). Ramping in this way means changing `MapErrOffset` produces a smooth move of the corrected position rather than a jump. The actual offset is forced to 0 only once the internal mapping type has fully reverted to off (the disengage ramp complete) or in simulation — *not* during the disengage ramp-down itself.

## Examples

```text
AMapErrOffset        ; read the offset target
AMapErrOffset=0      ; clear the offset (slews back to 0 at MapErrOffRamp)
AMapErrOffset=500    ; bias the corrected position by 500 counts
```

### Edge cases

- **Motor on / in motion at write** — rejected while the motor is on or the axis is in motion; use [MapErrOffRamp](MapErrOffRamp.md) to control the slew instead.
- **Mapping off** ([MapType](MapType.md) = 0) — the **actual** internal offset is forced to `0` only after the disengage ramp has fully completed (internal type reverted to off). *During* the disengage ramp-down the actual offset keeps slewing toward its target as normal; what fades it out of the feedback is the engage ramp counter (the whole correction is scaled by `counter / 16384`; see [MapErrOnStep](MapErrOnStep.md)), not a forced-zero of the offset. Once off, writes to `MapErrOffset` are stored but do not affect the feedback until mapping is re-engaged.
- **Simulation motor** — mapping is skipped entirely in simulation, so the actual offset is held at `0` regardless.
- **`MapErrOffRamp = 0`** — the actual offset never slews; changing `MapErrOffset` has no effect until `MapErrOffRamp` is non-zero.
- **Save** — not flash-saveable; reset to `0` on every boot.

## See also

- [MapErrOffRamp](MapErrOffRamp.md) — slew rate at which the applied offset converges to this target
- [MapErrOnStep](MapErrOnStep.md) — engage/disengage ramp of the whole correction
- [MapType](MapType.md) — enables the error mapping this offset modifies
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback this offset shifts
