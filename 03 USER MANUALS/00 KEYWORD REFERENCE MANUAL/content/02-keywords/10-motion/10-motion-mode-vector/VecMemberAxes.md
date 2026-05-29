---
keyword: VecMemberAxes
summary: Bit mask selecting which axes participate in the coordinated vector motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`VecMemberAxes` is a bit mask that defines which axes participate in the coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). Each bit corresponds to one axis, so the controller knows which axes to drive together along the resultant vector path and which to leave out. It is an axis-related parameter saved to flash and cannot be modified while in motion.

## How it works

### Bit-per-axis encoding

The mask is decoded one bit per axis, starting from the lowest-numbered axis at bit 0:

| Bit | Set mask | Axis included |
|----|----|----|
| 0 | 0x01 | first (lowest-numbered) axis |
| 1 | 0x02 | second axis |
| 2 | 0x04 | third axis |
| ... | ... | ... |
| 7 | 0x80 | eighth axis |

Add the masks of the axes you want in the group. For example `3` (`0x01 + 0x02`) selects the first two axes; `7` selects the first three. The range `0`-`255` allows up to eight axes to be selected.

### Which axis you set it on, and group rules

When you command the vector move (with `Begin` on [MotionMode](../02-motion-configuration/MotionMode.md) = 16), the controller reads `VecMemberAxes` from the axis you issued the command on and builds the group from the bits set in that value. At motion start it validates the group and rejects the move if any of these rules are broken:

- The mask must include the axis the command was issued on (its own bit must be set).
- At least two axes must be selected.
- For an arc ([VecType](VecType.md) = 1), exactly two axes must be selected.
- The command must be issued on the **lowest-numbered** axis in the group — that axis becomes the group master that runs the path profiler. Issuing it on any other member is rejected.
- Every member axis must be motor-on, set to [MotionMode](../02-motion-configuration/MotionMode.md) = 16, not already in motion, and commutated.

Once the move starts, the controller copies the master's `VecMemberAxes` value onto every member axis so the whole group reports the same membership. While the group is moving, each member also shows bit 19 (`0x00080000`) set in its [MotionStat](../05-motion-status/MotionStat.md) ("member of a vector-motion group"). When the move ends, `VecMemberAxes` is cleared back to `0` on every member.

## Examples

```text
AVecMemberAxes=3        ; on axis A: include the first two axes (bits 0 and 1) in the vector group
AVecMemberAxes=7        ; include the first three axes (bits 0, 1 and 2)
AVecMemberAxes          ; read the current member-axis mask on axis A
```

## See also

- [VecType](VecType.md) — linear vs. arc vector (arc requires exactly two members)
- [VecAbsTrgt](VecAbsTrgt.md) — resultant path distance over the member axes
- [VecMotionStat](VecMotionStat.md) — vector-group motion status
- [MotionStat](../05-motion-status/MotionStat.md) — bit 19 marks an axis as a vector-group member
