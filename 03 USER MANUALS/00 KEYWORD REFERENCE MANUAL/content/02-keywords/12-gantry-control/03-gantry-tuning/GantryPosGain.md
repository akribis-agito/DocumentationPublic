---
keyword: GantryPosGain
summary: Proportional position gain for the gantry yaw correction controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 654
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100000
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    type: array
    array_size: 6
    data_type: float32
    range:
    - 0
    - 1000000
---
# GantryPosGain

Proportional position gain for the gantry yaw correction controller.

## Overview

`GantryPosGain` is the proportional position gain of the gantry yaw correction loop. When gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)), the controller runs a dedicated yaw position/velocity controller in place of the per-axis position/velocity controller for the gantry axes, and `GantryPosGain` takes the role that [PosGain](../../11-control-tuning/03-position-control/00-overview.md) plays in the ordinary loop. It is an axis-related parameter saved to flash and can be changed at any time, including while in motion and with the motor on.

## How it works

In gantry mode the yaw position error is the difference between the shaped/filtered position reference and the gantry (differential) feedback rather than the single-axis feedback:

$$
\text{PosErr} = \text{PosRef}_{\text{shaped}} - \text{GantryFdbk}
$$

`GantryPosGain` then scales this yaw position error to form the velocity command that is passed into the yaw velocity loop (the built-in velocity-tracking feedforward term is added on top, exactly as in the ordinary position loop):

$$
\text{VelRef} = \text{PosErr} \cdot \text{GantryPosGain} + \frac{\text{PosRef} \cdot \text{VelTrackFact}}{1024}
$$

Increasing `GantryPosGain` raises the differential velocity (and hence corrective current) produced per unit of yaw position error. The resulting velocity command feeds the yaw velocity PI loop set by [GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md), whose output becomes the differential portion of the motor current command ([CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)) on the two gantry motors. The yaw correction reference itself is set by [GantryYawRef](../01-general-variables/GantryYawRef.md).

The value is dimensionless. The allowed range is 0 to 100000 with a default of 100 (on controllers where the gantry gains are a 6-element gain-scheduled array the upper range is extended; see the keyword attributes). A value of 0 disables the proportional position action of the yaw loop.

## Examples

```text
AGantryPosGain=200  ; set yaw position proportional gain
AGantryPosGain     ; read the current gain
```

### Edge cases

- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — the yaw loop is not running; writes are accepted but the gain has no effect until gantry mode is engaged.
- **Wrong axis** — on v4, `GantryPosGain` is consulted on the yaw axis (`B`); on v5 it is per-axis with gain-scheduling support. Setting it on the master axis on v4 is accepted but does not change the yaw loop behaviour.
- **Motor off** — accepted; the value persists until gantry is engaged.
- **Out of range** — values outside `0`–`100000` (v4) / `0`–`1000000` (v5) are rejected.
- **Zero gain** — disables the proportional position action; the yaw loop falls back to integral and feedforward only, with poor tracking.
- **Save** — flash-saveable.
- **Platform** — v5 stores as a 6-element `float32` array for gain scheduling; v4 stores as a single `int32`. Both branches use the same formula in the yaw loop.

## See also

- [GantryPosKi](GantryPosKi.md) — yaw position-loop integral gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction reference
