---
keyword: VecMemberAxes
summary: Bit mask selecting which axes participate in the coordinated vector motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 631
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
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecMemberAxes

Bit mask selecting which axes participate in the coordinated vector motion.

## Overview

`VecMemberAxes` is a bit mask that defines which axes participate in the vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). Each bit corresponds to one axis, so the controller knows which axes to coordinate along the vector path and which to leave stationary. It is an axis-related parameter saved to flash and cannot be modified while in motion.

## How it works

Set a bit to include the corresponding axis in the vector. Bit 0 is the lowest-order axis, bit 1 the next, and so on. The range `0`-`255` allows up to eight axes to be selected. For example, the value `3` (bits 0 and 1 set) selects the first two axes.

## Examples

```text
AVecMemberAxes=3     ; include the first two axes (bits 0 and 1) in the vector
AVecMemberAxes      ; read the current member-axis mask
```

## See also

- [VecType](VecType.md) — linear vs. arc vector
- [VecAbsTrgt](VecAbsTrgt.md) — resultant path distance over the member axes
- [VecMotionStat](VecMotionStat.md) — vector motion status
