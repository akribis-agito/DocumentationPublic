---
keyword: GantryCurrRef
summary: Read-only current (torque) reference of the gantry yaw correction.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 651
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
overrides: {}
---
# GantryCurrRef

Read-only current (torque) reference of the gantry yaw correction.

## Overview

`GantryCurrRef` is a read-only, axis-related status variable that reports the current reference (torque command) produced by the gantry yaw controller. It reflects the differential current command applied to the two gantry drive motors to correct yaw, and so tracks how hard the yaw loop is working in response to [GantryYawRef](GantryYawRef.md) while gantry mode is active (see [GantryOn](GantryOn.md)).

## Examples

```text
AGantryCurrRef     ; read the gantry yaw current reference
```

## See also

- [GantryYawRef](GantryYawRef.md) — yaw correction reference that this current responds to
- [GantryOn](GantryOn.md) — gantry mode that activates the yaw controller
