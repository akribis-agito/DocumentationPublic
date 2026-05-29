---
summary: Integral gain for the gantry yaw position loop.
keyword: GantryPosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 715
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryPosKi

Integral gain for the gantry yaw position loop.

## Overview

`GantryPosKi` is the integral gain of the gantry yaw position loop. It is the yaw-loop counterpart of the ordinary position-loop integral gain ([PosKi](../../11-control-tuning/03-position-control/00-overview.md)): while the proportional term [GantryPosGain](GantryPosGain.md) responds to the present yaw position error, `GantryPosKi` acts on the accumulated yaw position error so that residual (steady-state) yaw misalignment is driven out over time. It is an axis-related parameter, readable and writable while in motion and with the motor on, and is one of the gantry tuning gains that the controller substitutes for the normal control gains when gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)).

## How it works

When gantry mode is active the yaw position error is formed as the difference between the shaped/filtered position reference and the gantry (differential) feedback:

$$
\text{PosErr} = \text{PosRef}_{\text{shaped}} - \text{GantryFdbk}
$$

`GantryPosKi` scales the integral (running sum) of this yaw position error. The proportional part ([GantryPosGain](GantryPosGain.md)) and this integral part together form the velocity command sent into the yaw velocity PI loop ([GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md)), whose output becomes the differential current applied to the two gantry motors. `GantryPosKi` belongs to the same gantry gain set as [GantryPosGain](GantryPosGain.md), [GantryVelGain](GantryVelGain.md), [GantryVelKi](GantryVelKi.md), [GantryAccFFW](GantryAccFFW.md) and [GantryVelFFW](GantryVelFFW.md); on controllers that support gantry gain scheduling all six switch together as a set.

The value is dimensionless. A value of 0 disables the integral action of the yaw position loop. Refer to the keyword attributes for the range and default on a given controller.

## Examples

```text
AGantryPosKi[1]=0   ; set yaw position integral gain (first gain set)
AGantryPosKi[1]     ; read the current value
```

### Edge cases

- **Index 0** — invalid; valid indices are `GantryPosKi[1]`–`GantryPosKi[5]` (gain set 1 through 5). The active set is selected by gain scheduling.
- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — writes accepted; the gain has no effect until gantry is engaged.
- **Zero gain** — disables integral action; the yaw position loop runs as P + feedforward only.
- **Wind-up at engagement** — the firmware halves the velocity-loop integral across the master/yaw split when gantry engages; a large `GantryPosKi` can wind up the integral quickly during early settling.
- **Wrong axis** — consulted on the yaw axis of the pair; writes on the master or a non-gantry axis are accepted but not used.
- **Gain set selection** — the active set is chosen by the gain-scheduling subsystem (see [ScheduleMode](../../11-control-tuning/01-general-keywords/ScheduleMode.md)); reads return the value of the active set's storage.
- **Save** — flash-saveable.
- **Platform** — v5 central-i only. There is no `GantryPosKi` on v4.

## See also

- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryVelKi](GantryVelKi.md) — yaw velocity-loop integral gain
