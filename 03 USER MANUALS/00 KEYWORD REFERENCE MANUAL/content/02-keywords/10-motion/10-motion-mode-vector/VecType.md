---
keyword: VecType
summary: Selects the vector motion geometry (0 = linear, 1 = arc).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 630
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecType

Selects the vector motion geometry (0 = linear, 1 = arc).

## Overview

`VecType` defines whether the requested vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) is linear (`VecType = 0`) or an arc (`VecType = 1`). It selects the geometry of the coordinated path; when arc is chosen, the move is further described by [VecArcCenter](VecArcCenter.md), [VecArcDir](VecArcDir.md) and [VecNumCircles](VecNumCircles.md). It is saved to flash and cannot be modified while in motion.

> **Note:** A combined arc (main motion) plus linear (other axes) mode, `VecType = 2`, is identified as a near-future need but is outside the current range (0-1).

## How it works

`VecType` is read once, when the move is started, and selects which geometry the controller uses to convert a single path position into per-axis position references each control cycle:

| Value | Geometry | Member axes | How the path maps to the axes |
|----|----|----|----|
| 0 | Linear | 2 or more | The path is the straight line from the start point to the per-axis end points. The total path length [VecAbsTrgt](VecAbsTrgt.md) is the root-sum-of-squares of the individual per-axis distances. Each axis is driven to a fixed fraction of the path: its position is the start point plus (path fraction × that axis's total distance), so all axes start and finish together. |
| 1 | Arc | exactly 2 | The path is a circular arc in the plane of the two member axes. The controller derives the radius from [VecArcCenter](VecArcCenter.md) and the start point, finds the start and end angles, and each cycle converts the path position into a swept angle (path distance ÷ radius), then into the two axis positions on the circle. [VecArcDir](VecArcDir.md) sets the sweep direction and [VecNumCircles](VecNumCircles.md) adds full revolutions. |

For both geometries a single path-velocity profile (shaped by [VecSpeed](VecSpeed.md), [VecAccel](VecAccel.md), [VecDecel](VecDecel.md) and [VecJerk](VecJerk.md)) advances the path position; the geometry selected by `VecType` decides how that one number is split across the member axes. A linear move accepts any number of member axes (2+); an arc move requires exactly two, and the start/end radii derived from the center must agree within a few counts or the move is rejected.

## Examples

```text
AVecType=0           ; linear vector (default)
AVecType=1           ; arc vector
```

### Walk-through: run a linear-then-arc path on axes A and B

Vector motion is set per move and runs once `Begin` is issued on the lowest-numbered member axis. The recipe below runs a straight line first, then a circular arc, on a two-axis group `{A, B}`. Each move is configured, started, and allowed to finish before the next move is set up; `VecType` cannot be changed while in motion.

```text
; ===== Move 1: linear from current point to (15000, 5000) =====
; --- 1) Configure the group on the lowest-numbered axis (A) ---
AVecMemberAxes=3              ; bit 0 (A) + bit 1 (B) = 3
AVecType=0                    ; 0 = linear

; --- 2) Set the per-axis end points using AbsTrgt ---
AAbsTrgt=15000                ; axis A end point
BAbsTrgt=5000                 ; axis B end point

; --- 3) Set the path-velocity profile on the master (axis A) ---
AVecSpeed=8000
AVecAccel=20000
AVecDecel=20000

; --- 4) Arm the vector move ---
AMotionMode=16                ; 16 = vector
ABegin                        ; controller computes VecAbsTrgt and runs the path

; --- 5) Observe the path while it runs ---
AVecPosRef                    ; running position along the path (0 -> VecAbsTrgt)
AVecAbsTrgt                   ; total path distance (here sqrt(dA^2 + dB^2))
; ... wait for in-motion to clear ...

; ===== Move 2: clockwise arc, one extra full revolution =====
AVecType=1                    ; 1 = arc (requires exactly two member axes)
AVecArcCenter=15000           ; arc-centre coordinate on axis A (per-axis scalar)
BVecArcCenter=10000           ; arc-centre coordinate on axis B (per-axis scalar)
AVecArcDir=1                  ; sweep direction (see VecArcDir)
AVecNumCircles=1              ; one extra full revolution added to the swept angle
AAbsTrgt=20000                ; arc end point, axis A
BAbsTrgt=10000                ; arc end point, axis B
ABegin
```

If the move is rejected at `Begin`, check that `VecMemberAxes` includes the issuing axis, that the master axis is the lowest-numbered member, and (for arcs) that the start and end points sit on the same radius from `VecArcCenter`.

## See also

- [VecArcCenter](VecArcCenter.md) — arc center / radius (arc type)
- [VecArcDir](VecArcDir.md) — arc sweep direction (arc type)
- [VecMemberAxes](VecMemberAxes.md) — axes forming the vector
