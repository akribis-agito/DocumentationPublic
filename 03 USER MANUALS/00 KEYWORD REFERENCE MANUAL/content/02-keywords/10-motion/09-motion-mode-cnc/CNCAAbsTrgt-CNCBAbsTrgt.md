---
summary: Distance to move along the CNC path for the currently active segment.
---
# CNCAAbsTrgt/CNCBAbsTrgt

Distance to move along the CNC path for the currently active segment.

## Overview

`CNCAAbsTrgt` (and its `CNCBAbsTrgt` counterpart on the second CNC group) reports the length of the **currently active CNC segment**, measured along the path, in user units. The path-position reference [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) advances from zero at the start of a segment up to `CNCAAbsTrgt` at the end of that segment, so this value is the running endpoint of the active segment's velocity profile.

CNC mode runs coordinated multi-axis motion along a path that is streamed to the controller as a list of segments (a FIFO). `CNCAAbsTrgt` is read-only and reflects whichever segment is being executed now; it changes each time the path advances to the next segment.

## How it works

When a new segment becomes active, the controller resolves its path length from the segment data and the member-axis endpoints:

- **Linear segment** — the controller computes the per-axis travel (segment endpoint minus the axis's start position for each member axis) and takes the Euclidean (straight-line) length of that displacement vector. With a single member axis this reduces to the absolute travel of that axis.
- **Arc segment** — the path length is the arc length swept between the start and end angles around the programmed center.

That resolved length is `CNCAAbsTrgt`. The path-velocity profile (see [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md), [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md), [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)) is generated against this length: the deceleration point for the segment is derived from the distance still remaining to `CNCAAbsTrgt` and the active deceleration, so the path speed reaches the segment-end speed exactly as `CNCAPosRef` arrives at `CNCAAbsTrgt`.

Internally the path coordinate is accumulated at higher precision than user units (a fixed-point value scaled by `2^14`) so that fractional path motion carried over between segments does not drift; any fraction of `CNCAAbsTrgt` not consumed at the end of one segment is passed to the start of the next so the path stays continuous across a blended corner.

Non-motion segment types (delay, wait, set-position, filter-setup) do not advance the path and report a zero-length effective move while they are pending.

### CNCB note

`CNCBAbsTrgt` is the identical mechanism applied to the second CNC group. The two groups are fully independent: each tracks its own active-segment length, path reference, and profile.

## Examples

```text
ACNCAAbsTrgt        ; active-segment path length on group A
ACNCBAbsTrgt        ; active-segment path length on group B
```

## See also

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — path position that advances from 0 to `CNCAAbsTrgt`
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — per-cycle change of the path position (path velocity)
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed for the active segment
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
