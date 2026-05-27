---
keyword: GantryCurrRef
summary: Read-only current (torque) reference of the gantry yaw correction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# GantryCurrRef

Read-only current (torque) reference of the gantry yaw correction.

## Overview

`GantryCurrRef` is a read-only status variable reporting the current (torque) command of a gantry virtual axis before it is recombined into the two physical motors. Read on the master axis it is the **common-mode (linear)** current command; read on the yaw axis it is the **differential (yaw)** current command produced in response to [GantryYawRef](GantryYawRef.md). It therefore shows how hard each virtual loop is working while gantry mode is active (see [GantryOn](GantryOn.md)). It is axis-scoped and not saved to flash. On central-i v5 it is reported as a floating-point value.

## How it works

The two virtual-axis current commands are recombined into the two motor currents each cycle. With the symmetric split (no decoupling map), motor A receives the linear command plus the yaw command and motor B receives the linear command minus the yaw command — so a pure linear move drives both motors together and a pure yaw correction drives them in opposite directions. When the position-dependent decoupling map is enabled ([GantryMapType](GantryMapType.md) = 1) the linear part of the split is weighted by the map ratio ([GantryMapVal](GantryMapVal.md)) instead of being shared 50/50, while the yaw part is still added to one motor and subtracted from the other. `GantryCurrRef` reports the per-virtual-axis command before this recombination.

## Examples

```text
AGantryCurrRef     ; read the common-mode (linear) gantry current command
BGantryCurrRef     ; read the differential (yaw) gantry current command
```

## See also

- [GantryYawRef](GantryYawRef.md) — yaw correction reference that the differential current responds to
- [GantryOn](GantryOn.md) — gantry mode that activates the controller; explains common vs differential mode
- [GantryMapType](GantryMapType.md) / [GantryMapVal](GantryMapVal.md) — decoupling map that can reweight the current split
