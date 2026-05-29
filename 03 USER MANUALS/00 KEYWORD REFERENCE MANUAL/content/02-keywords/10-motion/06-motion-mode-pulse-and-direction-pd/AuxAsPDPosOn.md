---
keyword: AuxAsPDPosOn
summary: "Routes the pulse-and-direction inputs into the auxiliary encoder feedback (dual-loop), instead of the default cross-axis auxiliary source."
availability:
  standalone: []
  central-i:
  - v5
can_code: 686
attributes:
  access: rw
  scope: non-axis
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
# AuxAsPDPosOn

Routes the pulse-and-direction inputs into the auxiliary encoder feedback (dual-loop), instead of the default cross-axis auxiliary source.

## Overview

`AuxAsPDPosOn` selects where each axis's **auxiliary** position and velocity come from. It enables a dual-loop configuration in which the **pulse-and-direction (P/D) inputs are read as an incremental auxiliary encoder**, so the axis can close its loop on the motor feedback while a second sensor is wired to the P/D inputs.

It is a single, controller-wide (non-axis) setting saved to flash, valued 0 or 1 (default 0). It cannot be changed while a motor is on or in motion. It is supported on multi-axis units with P/D inputs.

> Available from v5 (Central-i) only.

## How it works

| Value | Auxiliary feedback source for each axis |
|---|---|
| 0 (default) | The auxiliary feedback of each axis is taken from another axis's main feedback (the default cross-axis mapping). |
| 1 | The auxiliary feedback ([AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md)) of each axis is taken from **that axis's own P/D input counter** ([PDPos](PDPos.md) / [PDVel](PDVel.md)). |

When set to 1, the controller copies the per-axis P/D counter and its rate into that axis's auxiliary position and velocity each control cycle. The P/D inputs therefore act as the auxiliary incremental encoder for a dual-loop scheme (e.g. motor encoder on the main loop, an external scale on the P/D inputs as the auxiliary). When set to 0, the auxiliary feedback keeps its default behaviour and the P/D inputs remain available for P/D motion.

Because the flag changes the auxiliary feedback wiring for all axes, configure it once during setup (motor off, no motion). Scale and direction of the P/D counter are set with the usual P/D scaling and direction keywords before it is used as auxiliary feedback.

> **Note on the name:** the keyword reads as "auxiliary as P/D position." The actual data flow is P/D inputs → auxiliary feedback: when enabled, the per-axis P/D counter supplies [AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md), i.e. the P/D inputs are used **as** the auxiliary encoder. The wording above follows that behaviour.

## Examples

```text
AAuxAsPDPosOn=1          ; use the P/D inputs as the auxiliary encoder (dual loop)
AAuxAsPDPosOn=0          ; default auxiliary feedback source
AAuxAsPDPosOn            ; read the current setting
```

(`AuxAsPDPosOn` is a controller-wide setting; the axis-letter prefix is still required by the command syntax.)

## See also

- [PDPos](PDPos.md) / [PDVel](PDVel.md) — the P/D counter and its rate, copied into the auxiliary feedback when enabled
- [AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md) — the auxiliary feedback this setting redirects
