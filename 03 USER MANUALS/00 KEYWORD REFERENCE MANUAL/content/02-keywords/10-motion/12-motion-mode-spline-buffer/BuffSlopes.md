---
keyword: BuffSlopes
summary: Edge velocity slopes imposed on the spline buffer trajectory when required.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 546
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffSlopes

Edge velocity slopes imposed on the spline buffer trajectory when required.

## Overview

`BuffSlopes` specifies the velocity slope imposed at the edges of the spline-buffer trajectory when [BuffEdgeMode](BuffEdgeMode.md) = 0 (specified-slope edges). It is a three-element array; the edge slope is taken from index `[1]`. The value sets the entry/exit velocity of the spline rather than letting the fit choose it. `BuffSlopes` is read from the relevant member axis when [BuffCalc](BuffCalc.md) runs, is saved to flash, and can be changed at any time, but a change only takes effect after [BuffCalc](BuffCalc.md) is run again.

## How it works

### Units and scaling

The stored value is a slope expressed in **thousandths of a position unit per servo sample**: the controller divides `BuffSlopes[1]` by 1000 to obtain the actual edge derivative. So a stored value of `1000` corresponds to a slope of one position unit per sample, and `500` to half a unit per sample. The factor of 1000 lets you set fractional slopes with an integer keyword.

### When it is used

`BuffSlopes` only affects the fit when **[BuffEdgeMode](BuffEdgeMode.md) = 0** and the curve is a parabolic or cubic spline ([BuffSplineMod](BuffSplineMod.md) = 2 or 3):

- For the **parabolic** fit, `BuffSlopes[1]` sets the initial velocity at the first waypoint; the remaining edge behaviour follows from the segment-by-segment fit.
- For the **cubic** fit, `BuffSlopes[1]` constrains the end derivatives so the spline enters and leaves at the requested slope (a clamped-spline boundary condition).

When [BuffEdgeMode](BuffEdgeMode.md) is 1 (natural) or 2 (multi-cycle), the edge derivatives are determined by those modes and `BuffSlopes` is ignored. Linear interpolation ([BuffSplineMod](BuffSplineMod.md) = 1) also ignores it. Indices `[2]` and `[3]` are reserved; only `[1]` is applied.

## Examples

```text
ABuffEdgeMode=0      ; enable specified-slope edges
ABuffSlopes[1]=0     ; enter/leave at zero velocity (start and stop at rest)
ABuffSlopes[1]=1000  ; edge slope of 1.0 position unit per servo sample
```

## See also

- [BuffEdgeMode](BuffEdgeMode.md) — must be 0 for these slopes to be applied
- [BuffSplineMod](BuffSplineMod.md) — slope applies to the parabolic/cubic fit only
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffCalc](BuffCalc.md) — applies the edge slope when fitting the spline
