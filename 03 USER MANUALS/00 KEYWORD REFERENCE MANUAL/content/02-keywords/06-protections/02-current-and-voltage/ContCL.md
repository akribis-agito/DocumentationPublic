---
keyword: ContCL
summary: Continuous current limit used in the I²t power-limitation scheme.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 51
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
  - 10
  - 32000
  default: 32000
  scaling: 1.0
  implemented: final
overrides: {}
---
# ContCL

Continuous current limit used in the I²t power-limitation scheme.

## Overview

`ContCL` is the continuous current limit of the amplifier. Together with [PeakCL](PeakCL.md) (the peak limit) and [PeakTime](PeakTime.md) (the time allowed at peak), it defines the **I²t** scheme that lets the drive deliver brief bursts of peak current while protecting the motor and amplifier from sustained overheating.

## How it works

![I²t tripping mechanism](I2t-tripping-mechanism.svg)

The drive may run up to `PeakCL` for up to `PeakTime`; sustained current is then limited toward `ContCL`.

> **Note:** if `ContCL` is set equal to or higher than `PeakCL`, the controller internally uses a continuous limit of `PeakCL / 2` instead. The stored `ContCL` value is not changed automatically.

## Examples

```text
AContCL=16000        ; continuous current limit (mA)
```

## See also

- [PeakCL](PeakCL.md) — peak current limit
- [PeakTime](PeakTime.md) — time allowed at peak current
