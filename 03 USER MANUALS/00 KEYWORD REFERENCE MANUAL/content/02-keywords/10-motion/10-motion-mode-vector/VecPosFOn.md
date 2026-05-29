---
keyword: VecPosFOn
summary: Enables (1) the position filter defined by VecPosFDef on the vector reference output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 648
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
# VecPosFOn

Enables (1) the position filter defined by VecPosFDef on the vector reference output.

## Overview

`VecPosFOn` enables the position filter on the coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) reference. When set to `1`, the filter defined by [VecPosFDef](VecPosFDef.md) is applied to smooth the resultant vector position reference before it is split among the member axes; when `0` (the default), the reference passes through unfiltered. Smoothing the vector reference reduces the jerk transmitted to the mechanics on every member axis at once. It is an axis-related parameter saved to flash and cannot be changed while the axis is in motion.

## How it works

The filter operates on the **resultant path** reference computed by the group master (the lowest-numbered member axis — see [VecMemberAxes](VecMemberAxes.md)), so configure and enable it on the master. Because the filtered resultant is what gets distributed to each member axis, enabling it smooths all members together and keeps the coordinated path consistent.

The enable flag is validated when the vector move starts: if it is set to `1`, the controller checks that [VecPosFDef](VecPosFDef.md) describes a valid filter and rejects the move if it does not. Set up [VecPosFDef](VecPosFDef.md) first, then set `VecPosFOn = 1`. Only the values `0` (off) and `1` (on) are accepted.

## Examples

```text
AVecPosFOn=0         ; position filter disabled on axis A (default)
AVecPosFOn=1         ; apply the VecPosFDef position filter to the vector reference
```

## See also

- [VecPosFDef](VecPosFDef.md) — filter definition applied when enabled
- [VecMemberAxes](VecMemberAxes.md) — defines the group and its master axis
- [VecSpeed](VecSpeed.md) — commanded resultant speed
