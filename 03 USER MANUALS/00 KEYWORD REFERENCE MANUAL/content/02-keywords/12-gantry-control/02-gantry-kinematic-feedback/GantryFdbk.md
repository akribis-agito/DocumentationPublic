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

`GantryFdbk` is a read-only parameter that provides the MIMO gantry control feedbacks. The A-axis value reports the common (mean) gantry position, while the B-axis value reports the differential position (yaw) between the two beam ends. These feedbacks are calculated even when gantry mode is disabled, so they can be monitored at any time. The differential reading drives the yaw correction commanded by [GantryYawRef](../01-general-variables/GantryYawRef.md) when [GantryOn](../01-general-variables/GantryOn.md) is active.

## How it works

The feedbacks include the initial offset captured in [GantryOffset](GantryOffset.md):

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2
BGantryFdbk = (APos - BPos - AGantryOffset)
```

(The simplified forms `AGantryFdbk = (APos + BPos) / 2` and `BGantryFdbk = (APos - BPos)` omit the offset term for clarity.)

`?GantryFdbk` with `?` not equal to `A` or `B` has no use and always returns `0`.

## Examples

```text
AGantryFdbk        ; read the mean (common) gantry position
BGantryFdbk        ; read the differential (yaw) gantry position
```

## See also

- [GantryOffset](GantryOffset.md) — initial A/B offset folded into these feedbacks
- [GantryOn](../01-general-variables/GantryOn.md) — enables gantry MIMO control
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction commanded from the differential feedback
