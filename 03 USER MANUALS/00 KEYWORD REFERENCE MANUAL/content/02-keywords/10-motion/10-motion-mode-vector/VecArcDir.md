---
keyword: VecArcDir
summary: Arc sweep direction for vector arc motion (0 = CCW, 1 = CW).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 634
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
# VecArcDir

Arc sweep direction for vector arc motion (0 = CCW, 1 = CW).

## Overview

For an arc vector ([VecType](VecType.md) = 1), `VecArcDir` defines the direction of the arc: `0` for counter-clockwise (CCW), `1` for clockwise (CW). Like all vector-motion keywords it is per axis, but only the `VecArcDir` of the axis used for the [Begin](../04-motion-command/Begin.md) command takes effect. It works together with [VecArcCenter](VecArcCenter.md), which fixes the center and radius.

It is saved to flash and cannot be modified while in motion.

## How it works

Two axes are defined for an arc motion. The arc is performed in the plane of these two axes, with the third axis not moving. The two axes are defined in a significant order; for example, `B, C` is not the same as `C, B`:

- The first axis is the **X** axis.
- The second axis is the **Y** axis.
- CCW motion is then around the "Z" axis, with the X axis moving toward the Y axis.

`VecArcDir` decides which way the swept angle moves from the start point to the end point, and therefore how much of the circle is covered:

- **CCW (`0`)** — the angle increases from the start angle to the end angle. The path length is the increasing angular gap (plus any full turns from [VecNumCircles](VecNumCircles.md)) times the radius.
- **CW (`1`)** — the angle decreases. The path length is the complementary gap (a full turn minus the CCW gap, plus any extra turns) times the radius.

So with the same start point, end point and center, switching `VecArcDir` selects the "short way" versus the "long way" round the circle. When the start and end points coincide (a full circle), both CCW and CW sweep exactly one complete turn (2π) on their own; use [VecNumCircles](VecNumCircles.md) to add further revolutions in either direction. The resulting arc length is stored as [VecAbsTrgt](VecAbsTrgt.md).

## Examples

```text
AVecArcDir=0         ; counter-clockwise arc (default)
AVecArcDir=1         ; clockwise arc
```

## See also

- [VecType](VecType.md) — selects linear vs. arc vector
- [VecArcCenter](VecArcCenter.md) — arc center / radius definition
- [Begin](../04-motion-command/Begin.md) — command whose axis selects the active `VecArcDir`
