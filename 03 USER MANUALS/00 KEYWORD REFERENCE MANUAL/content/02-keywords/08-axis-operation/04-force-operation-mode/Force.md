---
keyword: Force
summary: Force feedback obtained from the analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 582
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
    data_type: float32
---
# Force

Force feedback obtained from the analog input.

## Overview

`Force` is the force feedback obtained from the analog input. It has the same value as the corresponding `AInPort` linked to the force-feedback feature (configured via [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)). It is the measured quantity that the force loop drives toward [ForceRef](ForceRef.md), with the difference reported as [ForceErr](ForceErr.md).

## Examples

```text
AForce              ; read the force feedback
```

## See also

- [ForceRef](ForceRef.md) — force reference the loop tracks
- [ForceErr](ForceErr.md) — ForceRef minus Force
- [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) — configures the analog force-feedback input
