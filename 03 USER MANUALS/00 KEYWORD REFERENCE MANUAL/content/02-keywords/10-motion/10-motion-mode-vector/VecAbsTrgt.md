---
keyword: VecAbsTrgt
summary: Read-only total vector path distance (always positive) from start to end of motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 642
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VecAbsTrgt

Read-only total vector path distance (always positive) from start to end of motion.

## Overview

`VecAbsTrgt` is a status parameter that reports the target distance, from start of motion to its end, of the vector motion along the vector path. `VecAbsTrgt` is always positive. It is the end value that the running position reference [VecPosRef](VecPosRef.md) climbs toward as the move completes.

`VecAbsTrgt` is not used to *define* the vector motion. The motion is defined using the per-axis target keywords [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) or [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) of the member axes; `VecAbsTrgt` is the resultant path length computed from them.

## Examples

```text
AVecAbsTrgt         ; read the total vector path distance for the move
```

## See also

- [VecPosRef](VecPosRef.md) — running position along the path (ends at `VecAbsTrgt`)
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) / [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — per-axis targets that define the move
- [VecMemberAxes](VecMemberAxes.md) — axes participating in the vector
