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
actual \mathrel{+}= MapErrOffRamp \times SampleTime \quad \text{(toward the target, clamped on arrival)}
$$

So [MapErrOffRamp](MapErrOffRamp.md) sets the slew rate (counts per second) and `MapErrOffset` sets the destination. Each cycle the *actual* offset is added to the interpolated correction, and the sum is then scaled by the engage ramp (see [MapErrOnStep](MapErrOnStep.md)) before being added to the feedback to form [Pos](../10-motion/01-kinematics-status/Pos.md). Ramping in this way means changing `MapErrOffset` produces a smooth move of the corrected position rather than a jump. The actual offset is reset to 0 whenever mapping is off or in simulation.

## Examples

```text
AMapErrOffset        ; read the offset target
AMapErrOffset=0      ; clear the offset (slews back to 0 at MapErrOffRamp)
AMapErrOffset=500    ; bias the corrected position by 500 counts
```

## See also

- [MapErrOffRamp](MapErrOffRamp.md) — slew rate at which the applied offset converges to this target
- [MapErrOnStep](MapErrOnStep.md) — engage/disengage ramp of the whole correction
- [MapType](MapType.md) — enables the error mapping this offset modifies
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback this offset shifts
