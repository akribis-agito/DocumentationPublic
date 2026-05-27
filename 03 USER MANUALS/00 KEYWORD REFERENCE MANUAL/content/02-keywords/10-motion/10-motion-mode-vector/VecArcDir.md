---
keyword: VecArcDir
summary: Arc sweep direction for vector arc motion (0 = CCW, 1 = CW).
availability:
  standalone:
  - v4
  central-i:
  - v4
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

## Examples

```text
AVecArcDir=0         ; counter-clockwise arc (default)
AVecArcDir=1         ; clockwise arc
```

## See also

- [VecType](VecType.md) — selects linear vs. arc vector
- [VecArcCenter](VecArcCenter.md) — arc center / radius definition
- [Begin](../04-motion-command/Begin.md) — command whose axis selects the active `VecArcDir`
