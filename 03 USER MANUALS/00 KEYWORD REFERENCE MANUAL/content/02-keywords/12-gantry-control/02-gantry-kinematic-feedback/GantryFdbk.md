---
keyword: GantryFdbk
summary: Read-only MIMO gantry feedbacks; A reports the mean position, B the differential.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 652
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# GantryFdbk

Read-only MIMO gantry feedbacks; A reports the mean position, B the differential.

## Overview

`GantryFdbk` is a read-only parameter that provides the two MIMO gantry feedbacks — the inputs to the common-mode and differential-mode loops described under [GantryOn](../01-general-variables/GantryOn.md). The master-axis value reports the common (mean) gantry position, which the linear position loop follows; the yaw-axis value reports the differential position (yaw) between the two beam ends, which the yaw loop holds at the [GantryYawRef](../01-general-variables/GantryYawRef.md) target. These feedbacks are calculated every cycle even when gantry mode is disabled, so they can be monitored at any time. Reported in user units; on central-i v5 they are 64-bit values.

## How it works

The feedbacks combine the two motor positions and fold in the initial offset captured in [GantryOffset](GantryOffset.md):

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2     ; common (mean) - linear position
BGantryFdbk = (APos - BPos - AGantryOffset)         ; differential - yaw
```

(The simplified forms `AGantryFdbk = (APos + BPos) / 2` and `BGantryFdbk = (APos - BPos)` omit the offset term for clarity.)

The differential value is deliberately **not** divided by two: keeping the full `APos - BPos` difference preserves measurement resolution for the yaw loop, which only needs to drive the difference to its target rather than report a true mid-scaled angle.

When the position-dependent decoupling map is enabled ([GantryMapType](../01-general-variables/GantryMapType.md) = 1) the common-mode feedback is no longer a plain 50/50 mean: the two motor positions are blended using the map ratio ([GantryMapVal](../01-general-variables/GantryMapVal.md)) so the effective linear measurement point can be moved along the beam. In dual-loop gantry mode ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1) the master value instead reflects the load feedback selected by [GantryFdbkSrc](GantryFdbkSrc.md), and the motor-encoder mean is reported separately as [GantryAuxFdbk](GantryAuxFdbk.md).

Reading `GantryFdbk` on an axis that is neither a gantry master nor a gantry yaw axis has no use and always returns `0`.

## Examples

```text
AGantryFdbk        ; read the mean (common) gantry position
BGantryFdbk        ; read the differential (yaw) gantry position
```

## See also

- [GantryOffset](GantryOffset.md) — initial A/B offset folded into these feedbacks
- [GantryOn](../01-general-variables/GantryOn.md) — enables gantry MIMO control; explains common vs differential mode
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction commanded from the differential feedback
- [GantryMapType](../01-general-variables/GantryMapType.md) — decoupling map that reweights the common-mode feedback
- [GantryAuxFdbk](GantryAuxFdbk.md) — motor-encoder feedback when dual-loop gantry is used
