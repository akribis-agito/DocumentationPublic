---
keyword: AccShapeFact
summary: Array of per-segment acceleration scaling factors for the acceleration-shaping profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 164
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeFact

Array of per-segment acceleration scaling factors for the acceleration-shaping profile.

## Overview

`AccShapeFact` is an array (size 11) that defines the acceleration scaling factor for each segment of the acceleration-shaping profile. Each element specifies the fraction of the maximum acceleration applied during the corresponding segment whose extent is set by [AccShapeDist](AccShapeDist.md). The shaping is only applied when [AccShapeOn](AccShapeOn.md) is enabled. It is an axis-related array saved to flash and can be changed at any time.

## Examples

```text
AAccShapeFact[1]=50      ; scaling factor for first segment
AAccShapeFact[2]=100     ; scaling factor for second segment
AAccShapeFact[1]        ; query first segment factor
```

## See also

- [AccShapeOn](AccShapeOn.md) — enables acceleration shaping
- [AccShapeDist](AccShapeDist.md) — per-segment distances
