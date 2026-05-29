---
summary: Velocity feedforward gain for the gantry yaw correction controller.
keyword: GantryVelFFW
availability:
  standalone: []
  central-i:
  - v5
can_code: 678
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
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryVelFFW

Velocity feedforward gain for the gantry yaw correction controller.

## Overview

`GantryVelFFW` is the velocity feedforward gain of the gantry yaw correction loop. It is the yaw-loop counterpart of the ordinary velocity feedforward ([VelFFW](../../11-control-tuning/05-feedforwards/00-overview.md)): it injects a current term proportional to the commanded velocity so the load can be moved without waiting for the yaw velocity error to build up in the feedback loop. It is an axis-related parameter, readable and writable while in motion and with the motor on, and is one of the gantry tuning gains the controller substitutes for the normal control gains when gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)).

## How it works

Velocity feedforward is applied only in position operation mode. The controller scales the commanded velocity (the rate of change of the position reference) by `GantryVelFFW` and adds the result, together with the acceleration feedforward term ([GantryAccFFW](GantryAccFFW.md)), to the velocity PI output when forming the differential motor current command ([CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)):

$$
\text{CurrRef} = \text{VelPIOutput} + (\text{AccFFW term}) + \frac{\text{dPosRef} \cdot \text{GantryVelFFW}}{65536}
$$

Because this term depends only on the reference trajectory and not on the yaw error, it supplies anticipatory current during motion that the [GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md) feedback loop would otherwise have to develop from accumulated error.

The value is dimensionless. The default is 0 (velocity feedforward off unless configured); refer to the keyword attributes for the range on a given controller. `GantryVelFFW` belongs to the same gantry gain set as the other gantry tuning gains and is switched together with them on controllers that support gantry gain scheduling.

## Examples

```text
AGantryVelFFW[1]=0  ; set yaw velocity feedforward gain (first gain set)
AGantryVelFFW[1]    ; read the current value
```

### Edge cases

- **Index 0** — invalid; valid indices are `GantryVelFFW[1]`–`GantryVelFFW[5]` (gain sets). The active set is selected by gain scheduling.
- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — writes accepted; the gain has no effect until gantry is engaged.
- **Wrong mode** — feedforward is applied only when the position-loop reference advances; in current/force-only modes the term contributes nothing.
- **Zero gain** — disables yaw velocity feedforward.
- **Wrong axis** — consulted on the yaw axis of the pair; writes on the master or a non-gantry axis are accepted but not used.
- **Out of range** — values outside `0`–`50000` per-element are rejected.
- **Save** — flash-saveable.
- **Platform** — v5 central-i only. There is no `GantryVelFFW` on v4.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
