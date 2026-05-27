---
keyword: CurrDir
summary: Flips the direction of motor excitation (0 = normal, 1 = flipped).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 76
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrDir

Flips the direction of motor excitation (0 = normal, 1 = flipped).

## Overview

`CurrDir` configures the direction of motor excitation. It is normally used together with the encoder direction setting [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) to flip the axis into the desired physical direction. Because it changes how current is applied to the motor, it cannot be changed while the axis is in motion or the motor is on.

## How it works

| CurrDir | Effect |
|---------|--------|
| 0 | Motor direction is not flipped. |
| 1 | Motor direction is flipped. |

## Examples

```text
ACurrDir=0           ; normal excitation direction
ACurrDir=1           ; flipped excitation direction
```

## See also

- [EncDir / AuxEncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) — encoder direction, normally set together with CurrDir
- [ControlMode](ControlMode.md) — current/voltage control options
