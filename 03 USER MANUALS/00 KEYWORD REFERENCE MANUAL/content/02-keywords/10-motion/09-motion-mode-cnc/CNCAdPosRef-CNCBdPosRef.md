---
summary: Derivative of CNCAPosRef — the current vector velocity of the profiler.
---
# CNCAdPosRef/CNCBdPosRef

Derivative of CNCAPosRef — the current vector velocity of the profiler.

## Overview

`CNCAdPosRef` (and its `CNCBdPosRef` counterpart on the second CNC group) reports the per-cycle change of [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md), that is, the **current commanded velocity along the CNC path** (the path/vector speed of the profiler). It is read-only and reflects the active segment's profile in real time.

## How it works

CNC mode advances a single scalar path velocity each control cycle and adds it to the path position. `CNCAdPosRef` is that advance expressed as a velocity: it is computed as the difference between the current and the previous `CNCAPosRef` (the rate of change of the path coordinate). It is therefore the live value that the path-velocity profile produces while ramping between segment-end speeds.

- During the acceleration phase it rises toward the commanded path speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) (after the speed-scaling factors are applied) at the active acceleration [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md).
- During cruise it holds at the scaled commanded speed.
- During the braking phase it falls at the active deceleration [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) toward the segment-end speed [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md), reaching it as the path arrives at the segment length.

On non-motion segment types (delay, wait, set-position, filter-setup) the path does not advance, so `CNCAdPosRef` reads zero while the segment is pending. To suppress velocity spikes at the boundary of a segment whose end speed is zero, the controller may hold this value steady across that boundary rather than report a transient.

`CNCAdPosRef` is the *commanded* **path** (resultant) velocity from the profiler; it is not the velocity of any single member axis. The *actual* resultant velocity measured from the member axes is reported by [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md).

### CNCB note

`CNCBdPosRef` is the identical quantity for the independent second CNC group.

## Examples

```text
ACNCAdPosRef        ; read the current path velocity on group A
ACNCBdPosRef        ; read the current path velocity on group B
```

## See also

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — path position whose rate of change this reports
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed this ramps toward
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — segment-end speed this ramps toward at the end of a segment
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — actual resultant velocity measured from the member axes
