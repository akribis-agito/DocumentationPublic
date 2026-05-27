---
keyword: InTargetStat
summary: Reports the motion and settling state of the axis (disabled, moving, settling, reached).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 268
attributes:
  access: ro
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
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetStat

Reports the motion and settling state of the axis (disabled, moving, settling, reached).

## Overview

`InTargetStat` reports the motion and settling state of the axis. The exact meaning of each value depends on the `OperationMode`: in position/velocity control the settling check uses [PosErr](../01-kinematics-status/PosErr.md) against [InTargetTol](InTargetTol.md), while in current/force control it uses [Vel](../01-kinematics-status/Vel.md) `[1]` against [InTargetVelTh](InTargetVelTh.md). In all cases the in-window condition must persist for at least [InTargetTime](InTargetTime.md) before the axis reports "target reached" (`InTargetStat = 4`).

## How it works

| InTargetStat | OperationMode = 2 (Velocity control) OperationMode = 3 (Position control) Keyword to monitor: PosErr Settling window: InTargetTol | OperationMode = 1 (Current control) OperationMode = 4 (Force control) Keyword to monitor: Vel[1] Settling window: InTargetVelTh |
|---|---|---|
| 0 | **Motor disabled** | **Motor disabled** |
| 1 | **Motor enabled** | **Motor enabled** |
| 2 | **In motion** | **Velocity out of range** *a**b**s*(*V**e**l*[1]) > *I**n**T**a**r**g**e**t**V**e**l**T**h* |
| 3 | **Settling** Axis is settling / axis has settled but is pending InTargetTime to elapse. | **Velocity within range** *a**b**s*(*V**e**l*[1]) ≤ *I**n**T**a**r**g**e**t**V**e**l**T**h*, but is pending InTargetTime to elapse. |
| 4 | **Target reached** Axis has settled within InTargetTol for at least InTargetTime. Once InTargetStat = 4, it will remain so until the next motion is commanded/ axis is disabled, even if position error exits the settling window, where *a**b**s*(*P**o**s**E**r**r*) > *I**n**T**a**r**g**e**t**T**o**l*. | **Target reached** *a**b**s*(*V**e**l*[1]) ≤ *I**n**T**a**r**g**e**t**V**e**l**T**h* for at least InTargetTime. |

## Examples

<img alt="A screenshot of a graph AI-generated content may be incorrect." src="image29.png" style="width:5.40395in;height:5.06583in"/>

The example shows how InTargetStat changes with different motion phases, under position control operation mode (OperationMode=3).

| Time \[s\] | InTargetStat | Descriptions |
|----|----|----|
| 0 to 0.1 | 0 | Motor disabled. |
| 0.1 to 0.2 | 1 | Motor enabled. |
| 0.2 to 0.27 | 2 | In motion (where dPosRef!=0). |
| 0.27 to 0.42 | 3 | InTargetStat=3 after motion, until the absolute value of PosErr is less than InTargetTol for at least InTargetTime. |
| 0.42 to 1.17 | 4 | Target reached. InTargetStat=4 even when absolute value PosErr is more than InTargetTol. |
| 1.17 to 1.24 | 2 | In motion (where dPosRef!=0). |
| 1.24 to 1.39 | 3 | Settling and waiting for InTargetTime to elapse. |
| 1.39 to 1.73 | 4 | Target reached. |

```text
InTargetStat?       ; read the current settling state
```

## See also

- [InTargetTol](InTargetTol.md) — settling window (position/velocity control)
- [InTargetVelTh](InTargetVelTh.md) — settling window (current/force control)
- [InTargetTime](InTargetTime.md) — minimum dwell time inside the window
- [MotionStat](MotionStat.md) — detailed bit-mapped motion status
