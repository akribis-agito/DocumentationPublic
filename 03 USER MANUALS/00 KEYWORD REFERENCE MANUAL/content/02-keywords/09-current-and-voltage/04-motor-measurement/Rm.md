---
keyword: Rm
summary: Motor resistance measurement, in milliohms (updated by PCSuite).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 373
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
  - 100000
  default: 1000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# Rm

Motor resistance measurement, in milliohms (updated by PCSuite).

## Overview

`Rm` records the motor resistance measurement, in milliohms. PCSuite updates this value after running its resistance-and-inductance measurement. Whether the value represents phase or line-to-line data is set by [RLType](RLType.md). It is the resistance counterpart of the inductance measurement [Lm](Lm.md).

## How it works

`Rm` is a stored, flash-backed axis parameter holding a resistance value in milliohms (valid range 1 to 100000 mΩ, default 1000 mΩ). In the firmware it is a plain storage register: the resistance-and-inductance measurement (run from PCSuite) writes the measured value here, and it can also be read or set over the command interface. The firmware control loop does not read `Rm` to drive the current loop directly — it is the recorded measurement result, interpreted together with [RLType](RLType.md) (phase vs line-to-line) and paired with [Lm](Lm.md).

## Examples

```text
ARm                 ; read measured motor resistance (mΩ)
ARm=1500             ; set the resistance value manually (mΩ)
```

## See also

- [Lm](Lm.md) — measured motor inductance
- [RLType](RLType.md) — selects phase vs line-to-line measurement
