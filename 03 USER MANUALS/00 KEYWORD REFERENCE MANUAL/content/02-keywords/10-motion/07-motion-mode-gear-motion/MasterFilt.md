---
keyword: MasterFilt
summary: First-order low-pass filter coefficient for the scaled master-position delta (direct gear motion).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 161
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
  - 1
  - 64
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFilt

First-order low-pass filter coefficient for the scaled master-position delta (direct gear motion).

## Overview

`MasterFilt` defines the coefficient of a first-order low-pass filter applied to the scaled delta of [MasterPos](MasterPos.md) since the start of motion. It is only used in direct gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5`); indirect gear motion (`= 6`) has no such filter. It smooths the slave's tracking of the master.

## How it works

The filter formula, where time $t = kT_{s}$ and $T_{s}$ is the controller sampling time (typically 61 µs):

$$
y_{k} = \frac{MasterFilt}{64}u_{k} + \left( 1 - \frac{MasterFilt}{64} \right)y_{k - 1}
$$

By backward-Euler estimation, `MasterFilt` can be chosen from the cut-off frequency $f_{c}$ (in Hz). By default `MasterFilt = 3`, corresponding to a 128.2 Hz cut-off frequency.

$$
MasterFilt = 64\left( \frac{2\pi f_{c}T_{s}}{1 + 2\pi f_{c}T_{s}} \right)
$$

## Examples

```text
AMasterFilt=3        ; default (~128.2 Hz cut-off)
AMasterFilt         ; read current value
```

## See also

- [MasterPos](MasterPos.md) — the signal whose scaled delta is filtered
- [GearMaster](GearMaster.md) — selects the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — `MasterFilt` applies in direct gear motion (`= 5`)
