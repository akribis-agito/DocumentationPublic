---
keyword: VecPosFDef
summary: Array defining the position-filter coefficients applied to the vector reference output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 647
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: false
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
# VecPosFDef

Array defining the position-filter coefficients applied to the vector reference output.

## Overview

`VecPosFDef` is a 6-element array that defines the position filter applied to the coordinated vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) reference. It describes the filter that smooths the resultant vector position reference before it is split among the member axes, reducing the jerk transmitted to the mechanics. The filter only takes effect when it is enabled by [VecPosFOn](VecPosFOn.md). It is an axis-related array saved to flash and cannot be changed while the axis is in motion.

## How it works

The array uses the controller's standard customisable position-filter definition: element [1] selects the filter **type** and elements [2]-[5] supply up to four **parameters** for that type. A type of `0` (the default) means no filter, so the reference passes through unchanged. When a filter type is selected and [VecPosFOn](VecPosFOn.md) = 1, the controller derives the working coefficients from these parameters at the start of the vector move and applies a second-order (biquad-style) smoothing filter to the resultant path reference. The same definition convention is used elsewhere on the controller for customisable position filters.

Because the filter acts on the resultant path of the group master (the lowest-numbered member axis — see [VecMemberAxes](VecMemberAxes.md)), define it on the master. The definition is checked when the move starts: an invalid combination of type and parameters causes the move to be rejected, so verify the values before enabling the filter with [VecPosFOn](VecPosFOn.md).

## Examples

```text
AVecPosFDef[1]=0     ; element 1 = filter type (0 = no filter, the default)
AVecPosFDef[1]       ; read the filter-type element
AVecPosFDef[2]       ; read the first filter parameter
```

## See also

- [VecPosFOn](VecPosFOn.md) — enables/disables this position filter
- [VecMemberAxes](VecMemberAxes.md) — defines the group and its master axis
- [VecSpeed](VecSpeed.md) — commanded resultant speed
