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

`GantryAccFFW` sets the acceleration feedforward gain for the gantry yaw correction controller. It scales the acceleration reference to produce a feedforward current that reduces yaw lag during dynamic moves. It is an axis-related parameter saved to flash and can be changed at any time. It complements the feedback gains [GantryPosGain](GantryPosGain.md) and [GantryVelGain](GantryVelGain.md) and the velocity feedforward [GantryVelFFW](GantryVelFFW.md). The allowed range is 0 to 500000 (default 0).

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
