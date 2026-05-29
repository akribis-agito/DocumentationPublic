---
keyword: FIFOPosType
summary: Selects the operating mode of the FIFO position-tracking feature.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 659
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
# FIFOPosType

Selects the operating mode of the FIFO position-tracking feature.

## Overview

`FIFOPosType` selects how the position points streamed through the FIFO position-tracking queue are interpolated between successive cycles. It is the interpolation-mode setting for the position-tracking subsystem, which is enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md) and fed by [FIFOPosPush](FIFOPosPush.md).

Unlike the main FIFO motion mode (see [FIFOType](FIFOType.md)), which builds a trajectory from velocity-type and acceleration-type *segments*, position tracking streams a series of absolute **position targets**. The controller takes one new target per cycle and produces the motion reference by interpolating between consecutive targets. `FIFOPosType` chooses the interpolation rule used for that fill-in.

It is saved to flash and cannot be changed while the axis is in motion.

## How it works

A new position target is taken from the queue at the first sample of every cycle (the cycle length, in servo samples, is set by [FIFOPosCycle](FIFOPosCycle.md)). Between cycles, the position reference is computed from the surrounding targets according to the selected mode:

| Value | Mode | Behavior |
|-------|------|----------|
| 0 | Linear interpolation (default) | The reference moves in a straight line between the target at the start of the current cycle and the target at its end. Two targets are needed. |
| 1 | Cubic-spline interpolation | The reference follows a smooth cubic curve fitted through four consecutive targets (the previous start, the current start, the current end, and the next end). This produces continuous velocity across cycle boundaries at the cost of one extra cycle of look-ahead latency. |

In both modes the interpolated reference is shifted by [FIFOPosPosOf](FIFOPosPosOf.md) before it is used, and the resulting reference is still clamped by the software position limits.

When the axis enters position-tracking mode, the working target and all internal control points are initialized to the current position reference, so tracking starts smoothly from where the axis already is. At the same time the three position-tracking offsets [FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosVelOf](FIFOPosVelOf.md), and [FIFOPosCurrOf](FIFOPosCurrOf.md) are all reset to 0, so each run starts from a clean, un-offset reference.

### Interpolation math

The reference is recomputed every sample from an in-cycle sample counter that runs from 0 up to [FIFOPosCycle](FIFOPosCycle.md) − 1 and wraps back to 0 at the first sample of the next cycle (this counter is reported by `FIFOPosStatus[6]`). Writing `k` for that counter and `N` for `FIFOPosCycle`, the in-cycle interpolation factor is `k / N`, which therefore ranges over `0, 1/N, 2/N, …, (N−1)/N` and reaches a maximum of `(N − 1) / N` — always strictly less than 1.

**Linear mode (`FIFOPosType=0`).** Writing `T_start` for the target at the start of the current cycle and `T_end` for the target at its end (`FIFOPosStatus[2]` and `FIFOPosStatus[3]`), the reference at sample `k` is

$$\text{PosRef}(k) = T_\text{start} + (T_\text{end} - T_\text{start})\,\frac{k}{N} + \text{FIFOPosPosOf}$$

**Cubic mode (`FIFOPosType=1`).** Cubic mode uses a Catmull-Rom cubic spline. With the four control points `P1` = previous-cycle start, `P2` = current-cycle start, `P3` = current-cycle end, `P4` = next-cycle end (reported as `FIFOPosStatus[1]` through `FIFOPosStatus[4]`), the reference over the current cycle is

$$\text{PosRef}(t) = P_2 + c_1 t + c_2 t^2 + c_3 t^3 + \text{FIFOPosPosOf}, \qquad t = \frac{k}{N} \in [0, 1)$$

$$c_1 = \frac{P_3 - P_1}{2}$$
$$c_2 = (P_1 - P_2) + 2(P_3 - P_2) - 0.5\,(P_4 - P_2)$$
$$c_3 = -0.5\,(P_1 - P_2) - 1.5\,(P_3 - P_2) + 0.5\,(P_4 - P_2)$$

(the coefficients are formed from the targets measured relative to `P2`, and `k` is the in-cycle sample index reported by `FIFOPosStatus[6]`). The curve passes exactly through `P2` at `t = 0` and through `P3` at the next cycle start; `P1` and `P4` only set the tangents, which is what makes the velocity continuous across cycle boundaries. `P4` is the most recently popped target, so cubic mode renders one cycle behind the queue head — the one-cycle look-ahead latency.

**Reaching each target.** Because the in-cycle factor `k / N` never reaches 1, the end-of-cycle target is not produced on the last sample of its own cycle. Instead, at the first sample of the next cycle the start-of-cycle control point is advanced to the previous end-of-cycle control point and the reference is set exactly to that value plus `FIFOPosPosOf`. The trajectory therefore passes precisely through each pushed target one cycle after it is consumed, in both linear and cubic modes.

## Examples

```text
AFIFOPosType=0       ; linear interpolation between targets
AFIFOPosType=1       ; smooth cubic-spline interpolation
```

## See also

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosCycle](FIFOPosCycle.md) — samples per target (cycle length)
- [FIFOPosStatus](FIFOPosStatus.md) — position-tracking queue status
- [FIFOType](FIFOType.md) — the main (segment-based) FIFO motion mode
