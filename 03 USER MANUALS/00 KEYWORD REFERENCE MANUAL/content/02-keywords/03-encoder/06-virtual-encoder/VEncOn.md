---
keyword: VEncOn
summary: Enables or disables the software-generated virtual encoder for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 613
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncOn

Enables or disables the software-generated virtual encoder for the axis.

## Overview

`VEncOn` enables or disables the virtual encoder for the axis. When set to 1, the controller uses the software-generated virtual encoder position as the feedback source, where the position is derived from the source selected by [VEncSrc](VEncSrc.md), formatted by [VEncType](VEncType.md), scaled by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), and delayed by [VEncDelay](VEncDelay.md). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

| VEncOn | State |
|---|---|
| 0 | Virtual encoder disabled |
| 1 | Virtual encoder enabled |

## Examples

```text
VEncOn=1            ; enable the virtual encoder
VEncOn=0            ; disable the virtual encoder
```

## See also

- [VEncSrc](VEncSrc.md) — source signal for the virtual encoder
- [VEncType](VEncType.md) — output format of the virtual encoder
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
- [VEncDelay](VEncDelay.md) — delay applied to the virtual encoder output
