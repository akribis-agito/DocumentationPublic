---
summary: Reports the deceleration of the active CNC segment on group A (or B).
---
# CNCADecel/CNCBDecel

Reports the deceleration of the active CNC segment on group A (or B).

## Overview

`CNCADecel` (and its `CNCBDecel` counterpart) is a read-only parameter that reports the deceleration of the path-velocity profile for the currently active CNC segment on group A (or B), in user units per second squared. It reflects the deceleration encoded in the segment that was pushed to the queue. It is a non-axis, read-only parameter that is not saved to flash.

## How it works

As the path approaches the end of the active segment, the controller computes a deceleration limit from the distance still remaining to the segment length [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md), the active deceleration `CNCADecel`, and the target segment-end speed [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md). When the path velocity [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) would exceed that limit, the profiler brakes at `CNCADecel` so the path velocity arrives at the end speed exactly at the segment endpoint. This lookahead is what lets consecutive segments blend at a non-zero corner speed.

If a segment starts at a speed too high to reach its end speed at `CNCADecel` over the remaining distance, the controller raises the deceleration for the rest of that segment (a one-time recalculated higher rate) instead of forcing an abrupt velocity jump.

### Trajectory math

Each control cycle the controller computes the highest path velocity from which it can still brake to the segment-end speed within the distance remaining, using the standard kinematic relation

$$v_{\text{brake}} = -\,a_{\text{eff}}\,T_s + \sqrt{a_{\text{eff}}^{\,2}\,T_s^{\,2} + 2\,a_{\text{eff}}\,(\text{CNCAAbsTrgt} - \text{CNCAPosRef}) + \text{CNCAEndSpeed}^2}$$

where $T_s$ is the control-cycle period and $a_{\text{eff}}$ is the effective deceleration in force this cycle (the reported `CNCADecel` scaled by the square of the time-scaling factor, as described below). When the current path velocity [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) exceeds $v_{\text{brake}}$ the profiler decelerates so that [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) arrives at [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) exactly as [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) reaches [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md).

If a segment is entered at a speed too high to brake to its end speed at the active deceleration over the remaining distance, snapping straight onto $v_{\text{brake}}$ would be a velocity jump. Only when that jump is larger than 1% of the current path velocity does the controller switch, once for the rest of that segment, to a higher recomputed deceleration

$$a_{\text{new}} = \frac{\text{CNCAdPosRef}^2 - \text{CNCAEndSpeed}^2}{2\,(\text{CNCAAbsTrgt} - \text{CNCAPosRef})}$$

so the path still reaches the end speed at the endpoint; a smaller mismatch is simply absorbed by snapping the path velocity onto the deceleration curve.

The effective deceleration used each cycle is the reported segment value scaled by the square of the on-the-fly time-scaling factor [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md): effective decel = `CNCADecel × (CNCAPercents/100)²`. The speed-only override [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) does **not** scale deceleration. This is the *normal* braking rate; a separate, larger rate [CNCAEmrgDec/CNCBEmrgDec](CNCAEmrgDec-CNCBEmrgDec.md) is used for emergency stops.

`CNCADecel` is applied to the **path** (resultant) velocity; the geometry distributes the braking across the member axes.

### CNCB note

`CNCBDecel` reports the identical quantity for the independent second CNC group.

## Examples

```text
ACNCADecel          ; read the active-segment deceleration on group A
ACNCBDecel          ; read it on group B
```

## See also

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active-segment acceleration
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — speed the deceleration lookahead targets
- [CNCAEmrgDec/CNCBEmrgDec](CNCAEmrgDec-CNCBEmrgDec.md) — emergency-stop deceleration (distinct, larger)
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — scales deceleration by the square of its factor
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
