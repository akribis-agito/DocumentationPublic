---
summary: Enables dual-loop (position + yaw) gantry control mode.
keyword: GantryDLoopOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 675
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryDLoopOn

Enables dual-loop (position + yaw) gantry control mode.

## Overview

`GantryDLoopOn` selects whether the gantry closes its common (linear) position loop on the two motor encoders or on a separate load-side feedback:

| Value | Mode | Linear position loop closes on |
|:-----:|------|-------------------------------|
| 0 | Single-loop gantry (default) | The common-mode (mean) of the two motor encoders. |
| 1 | Dual-loop gantry | The feedback selected by [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) (typically a direct load measurement), with the two motor encoders kept as the auxiliary/velocity feedback. |

It is set per axis, saved to flash, and can be changed only with the motor off and not in motion (configure it before turning the motors on and enabling [GantryOn](GantryOn.md)). In both modes the **yaw** (differential) loop continues to run from the two motor encoders, so the controller still drives a yaw-correction current into the two motors to keep the beam square; the dual-loop setting only changes how the *linear* position is measured.

This is the gantry counterpart of the single-axis dual-loop feature: the linear loop is closed on the load while the motor encoders stabilise the inner loop and measure yaw. The dual-loop scaling between load units and motor units uses the same dual-loop factor as single-axis dual loop.

## How it works

In single-loop mode the controller forms the common-mode position from the two motor encoders (the mean), so [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) on the master axis is the position the linear loop follows. In dual-loop mode the controller instead uses the load feedback selected by [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) for the linear loop and reports the motor-encoder mean as the auxiliary feedback [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md); the velocity loop runs on the auxiliary (motor-encoder) velocity [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md), scaled by the dual-loop factor. The controller also adjusts the internal position-limit and following-error bounds by the dual-loop factor, and captures an offset at engagement so the reported linear position does not step. See the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) for the full per-mode feedback and velocity sourcing table.

## Examples

```text
AGantryDLoopOn=1     ; close the linear gantry loop on the load feedback (dual-loop)
AGantryDLoopOn=0     ; close the linear loop on the motor encoders (single-loop)
AGantryDLoopOn       ; read the configured mode
```

### Edge cases

- **Motor on / in motion at write** — rejected (`NOMOTN`, `NOMTRON`). Configure the dual-loop mode before enabling either gantry member.
- **Out of range** — values outside `0`–`1` are rejected.
- **Set on wrong axis** — the engine reads `GantryDLoopOn` on the **master** axis (the same axis where [GantryOn](GantryOn.md) is set). Writes on a yaw or non-gantry axis are accepted but never consulted.
- **`GantryDLoopOn = 1` without a valid [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md)** — the load-feedback pointer falls back to zero and the linear loop has no live reference; configure `GantryFdbkSrc` before enabling gantry.
- **Yaw loop is unchanged** — the differential (yaw) loop still runs on the motor encoders in both modes; only the linear measurement source changes.
- **Save** — flash-saveable; reloaded at boot.
- **Platform** — v5 central-i only. There is no dual-loop gantry on v4.

## See also

- [GantryOn](GantryOn.md) — enables gantry MIMO control
- [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) — load feedback source used when this is 1
- [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — auxiliary (motor-encoder) feedback and velocity in dual-loop mode
- [GantryYawRef](GantryYawRef.md) — yaw correction reference
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — yaw position-loop gain
