---
keyword: CNCACumPosRef
summary: "Cumulative commanded path position of CNC group A across all segments since the motion started."
availability:
  standalone: []
  central-i:
  - v5
can_code: 468
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
# CNCACumPosRef

Cumulative commanded path position of CNC group A across all segments since the motion started.

## Overview

`CNCACumPosRef` (and its [CNCBCumPosRef](CNCBCumPosRef.md) counterpart on the second CNC group) reports the **total commanded distance travelled along the CNC path** since the current CNC motion began — that is, the sum of every completed segment's length plus the path position within the segment now executing. It is a read-only 64-bit value.

Where [CNCAPosRef](CNCAPosRef-CNCBPosRef.md) restarts from zero at the start of each segment, `CNCACumPosRef` keeps counting up across segment boundaries, so it gives you one continuously increasing coordinate for the whole programmed path. That makes it convenient for progress tracking and for driving downstream features (for example a virtual encoder or position-based events) from the path position rather than from any single member axis.

Available on central-i (v5).

## How it works

CNC mode advances a single scalar path position each control cycle (see [CNCAPosRef](CNCAPosRef-CNCBPosRef.md)). The controller maintains a running total of the lengths of all segments that have already completed; each cycle it reports:

```text
CNCACumPosRef = (sum of completed-segment lengths) + (current CNCAPosRef)
```

- When a CNC motion is started, `CNCACumPosRef` and the completed-segment total are **reset to 0**.
- As the path advances within a segment, `CNCACumPosRef` rises together with [CNCAPosRef](CNCAPosRef-CNCBPosRef.md).
- When a segment finishes, its full length is added to the completed-segment total and [CNCAPosRef](CNCAPosRef-CNCBPosRef.md) restarts from zero for the next segment, so `CNCACumPosRef` continues to climb smoothly through the corner with no jump.

The value is the commanded **path** coordinate (the master coordinate that drives all member axes), not the position of any individual axis. Its per-cycle change is the path velocity reported by [CNCAdPosRef](CNCAdPosRef-CNCBdPosRef.md).

`CNCACumPosRef` can be selected as the source of a virtual encoder. If it is being used that way and the CNC source is reset (a new motion is started), the virtual encoder that was emulating it is turned off automatically so it does not track a coordinate that has just jumped back to zero.

## Examples

```text
ACNCACumPosRef       ; read the total commanded path distance on group A
ACNCBCumPosRef       ; read the total commanded path distance on group B
```

## See also

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — per-segment path position (restarts each segment)
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — per-cycle change of the path position (path velocity)
- [CNCBCumPosRef](CNCBCumPosRef.md) — the same cumulative coordinate on the second CNC group
- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — active-segment length added to the total when the segment completes
