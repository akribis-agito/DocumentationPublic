---
keyword: Lm
summary: Motor inductance measurement, in micro-Henry (updated by PCSuite).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 374
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
  - 1000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# Lm

Motor inductance measurement, in micro-Henry (updated by PCSuite).

## Overview

`Lm` records the motor inductance measurement, in micro-Henry. PCSuite updates this value after running its resistance-and-inductance measurement. Whether the value represents phase or line-to-line data is set by [RLType](RLType.md). It is the inductance counterpart of the resistance measurement [Rm](Rm.md).

## Examples

```text
ALm                 ; read measured motor inductance (µH)
ALm=1200             ; set the inductance value manually (µH)
```

## See also

- [Rm](Rm.md) — measured motor resistance
- [RLType](RLType.md) — selects phase vs line-to-line measurement
