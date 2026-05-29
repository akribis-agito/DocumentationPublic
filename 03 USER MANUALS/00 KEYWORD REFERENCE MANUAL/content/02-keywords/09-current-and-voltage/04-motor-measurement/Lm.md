---
keyword: Lm
summary: Motor inductance measurement, in micro-Henry (updated by PCSuite).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# Lm

Motor inductance measurement, in micro-Henry (updated by PCSuite).

## Overview

`Lm` records the motor inductance measurement, in micro-Henry. PCSuite updates this value after running its resistance-and-inductance measurement. Whether the value represents phase or line-to-line data is set by [RLType](RLType.md). It is the inductance counterpart of the resistance measurement [Rm](Rm.md).

## How it works

`Lm` is a stored, flash-backed axis parameter holding an inductance value in micro-Henry (valid range 1 to 1000000 µH, default 1000 µH). The resistance-and-inductance measurement (run from PCSuite) writes the measured value here, and it can also be read or set over the command interface. The value is the recorded measurement result, interpreted together with [RLType](RLType.md) (phase vs line-to-line) and paired with [Rm](Rm.md).

On v4 `Lm` is a stored measurement the control loop does not use. On central-i v5 the stored `Lm` value is also used to compute the inductive (L·dI/dt) voltage feed-forward term and a cross-coupling compensation term that are added to the current-loop output when voltage feed-forward is enabled. See [LmFFWLevel](../../11-control-tuning/05-feedforwards/LmFFWLevel.md) and [VoltageFFWOn](../../11-control-tuning/05-feedforwards/VoltageFFWOn.md).

## Examples

```text
ALm                 ; read measured motor inductance (µH)
ALm=1200             ; set the inductance value manually (µH)
```

## See also

- [Rm](Rm.md) — measured motor resistance
- [RLType](RLType.md) — selects phase vs line-to-line measurement
