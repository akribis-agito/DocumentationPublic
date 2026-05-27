---
keyword: GantryVelKi
summary: Integral gain for the gantry yaw velocity loop.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 657
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
overrides: {}
---
# GantryVelKi

Integral gain for the gantry yaw velocity loop.

## Overview

`GantryVelKi` sets the integral gain of the gantry yaw velocity loop. The integral term accumulates differential velocity error over time to remove steady-state error left by the proportional gain [GantryVelGain](GantryVelGain.md). It is an axis-related, read/write parameter saved to flash and can be changed at any time. The allowed range is 0 to 100000 (default 100).

> **Note:** The imported source text for this entry was garbled (it read "Gantry Mode Position Loop Integral Gain", apparently a copy-paste from the position-loop entry). The description above is grounded in the keyword's attributes; the detailed loop description should be confirmed against current firmware.

## Examples

```text
AGantryVelKi=50     ; set yaw velocity integral gain
AGantryVelKi?       ; read the current gain
```

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryPosKi](GantryPosKi.md) — yaw position-loop integral gain
