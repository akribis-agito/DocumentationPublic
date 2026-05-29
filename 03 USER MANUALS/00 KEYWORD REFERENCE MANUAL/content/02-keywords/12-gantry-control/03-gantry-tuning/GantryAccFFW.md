---
keyword: GantryAccFFW
summary: Acceleration feedforward gain for the gantry yaw correction controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 655
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
  - 500000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    type: array
    array_size: 6
    data_type: float32
    range:
    - 0
    - 50000000
---
# GantryAccFFW

Acceleration feedforward gain for the gantry yaw correction controller.

## Overview

`GantryAccFFW` is the acceleration feedforward gain of the gantry yaw correction loop. When gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)) it takes the role that the ordinary [AccFFW](../../11-control-tuning/05-feedforwards/00-overview.md) plays in the per-axis loop, injecting a current term proportional to the commanded acceleration so the feedback loops are not solely responsible for accelerating the load. It is an axis-related parameter saved to flash and can be changed at any time, including while in motion and with the motor on.

## How it works

Acceleration feedforward is applied only in position operation mode. The controller forms the commanded acceleration from the second difference of the shaped/filtered position reference (the discrete second derivative), scales it by `GantryAccFFW`, and adds the result directly to the velocity PI output when forming the differential motor current command:

$$
\text{CurrRef} = \text{VelPIOutput} + \frac{(\text{PosRef}_{n} - 2\,\text{PosRef}_{n-1} + \text{PosRef}_{n-2}) \cdot \text{GantryAccFFW}}{256}
$$

Because this term is a feedforward, it depends only on the reference trajectory, not on the yaw error, so it can supply the current needed during acceleration without waiting for an error to build up in the [GantryPosGain](GantryPosGain.md) / [GantryVelGain](GantryVelGain.md) feedback loops. Note that in gantry mode the yaw current command uses the acceleration feedforward term only; the velocity feedforward [GantryVelFFW](GantryVelFFW.md) applies on controllers/firmware that include it in the yaw loop.

The value is dimensionless (a feedforward scaling). The allowed range is 0 to 500000 with a default of 0, i.e. acceleration feedforward is off unless configured (on controllers where the gantry gains are a 6-element gain-scheduled array the upper range is extended; see the keyword attributes).

## Examples

```text
AGantryAccFFW=1000  ; set acceleration feedforward gain
AGantryAccFFW      ; read the current gain
```

## See also

- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryVelFFW](GantryVelFFW.md) — velocity feedforward gain
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction reference
