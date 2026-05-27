---
summary: Integral gain for the gantry yaw position loop.
---
# GantryPosKi

Integral gain for the gantry yaw position loop.

## Overview

`GantryPosKi` sets the integral gain for the gantry yaw position controller. It eliminates steady-state yaw position error by integrating the yaw error over time and adding a corrective current. It is an axis-related parameter that complements the proportional term [GantryPosGain](GantryPosGain.md) and the velocity-loop gains [GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryVelKi](GantryVelKi.md) — yaw velocity-loop integral gain
