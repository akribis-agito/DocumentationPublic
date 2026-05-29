---
keyword: CNCBCumPosRef
summary: "Cumulative commanded path position of CNC group B across all segments since the motion started."
availability:
  standalone: []
  central-i:
  - v5
can_code: 700
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CNCBCumPosRef

Cumulative commanded path position of CNC group B across all segments since the motion started.

## Overview

`CNCBCumPosRef` is the read-only 64-bit cumulative path coordinate of the **second** CNC group (group B). It is the exact counterpart of [CNCACumPosRef](CNCACumPosRef.md) on the independent CNC group A: it reports the **total commanded distance travelled along the CNC path** since the current group-B CNC motion began — the sum of every completed segment's length plus the path position within the segment now executing.

Where [CNCBPosRef](CNCAPosRef-CNCBPosRef.md) restarts from zero at the start of each segment, `CNCBCumPosRef` keeps counting up across segment boundaries, giving one continuously increasing coordinate for the whole programmed path on group B. That makes it convenient for progress tracking and for driving downstream features (for example a virtual encoder or position-based events) from the path position rather than from any single member axis.

Available on central-i (v5).

## How it works

CNC mode advances a single scalar path position each control cycle (see [CNCBPosRef](CNCAPosRef-CNCBPosRef.md)). The controller maintains a running total of the lengths of all group-B segments that have already completed; each cycle it reports:

```text
CNCBCumPosRef = (sum of completed-segment lengths) + (current CNCBPosRef)
```

- When a group-B CNC motion is started, `CNCBCumPosRef` and the completed-segment total are **reset to 0**.
- As the path advances within a segment, `CNCBCumPosRef` rises together with [CNCBPosRef](CNCAPosRef-CNCBPosRef.md).
- When a segment finishes, its full length is added to the completed-segment total and [CNCBPosRef](CNCAPosRef-CNCBPosRef.md) restarts from zero for the next segment, so `CNCBCumPosRef` continues to climb smoothly through the corner with no jump.

The value is the commanded **path** coordinate (the master coordinate that drives all member axes of group B), not the position of any individual axis. Its per-cycle change is the path velocity reported by [CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md).

`CNCBCumPosRef` can be selected as the source of a virtual encoder. If it is being used that way and the CNC source is reset (a new motion is started), the virtual encoder that was emulating it is turned off automatically so it does not track a coordinate that has just jumped back to zero.

## Examples

```text
ACNCBCumPosRef       ; read the total commanded path distance on group B
ACNCACumPosRef       ; read the total commanded path distance on group A
```

## See also

- [CNCACumPosRef](CNCACumPosRef.md) — the same cumulative coordinate on the first CNC group
- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — per-segment path position (restarts each segment)
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — per-cycle change of the path position (path velocity)
- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — active-segment length added to the total when the segment completes
