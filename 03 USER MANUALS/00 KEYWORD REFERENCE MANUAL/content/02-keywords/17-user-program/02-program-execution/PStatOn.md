---
keyword: PStatOn
summary: Enables or disables periodic parameter-statistics streaming.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 480
attributes:
  access: rw
  scope: non-axis
  flash: false
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
  implemented: partial
overrides: {}
---
# PStatOn

Enables or disables periodic parameter-statistics streaming.

## Overview

`PStatOn` enables or disables the periodic parameter-statistics streaming feature. When set to `1`, the controller transmits the parameters listed in [PStatParams](PStatParams.md) over the port configured by [PStatPort](PStatPort.md), at the interval set by [PStatInterval](PStatInterval.md). It is the master switch for the whole `PStat` group. It is a non-axis parameter and is not saved to flash.

## Examples

```text
APStatOn=1           ; start periodic statistics streaming
APStatOn=0           ; stop streaming
```

## See also

- [PStatParams](PStatParams.md) — parameters included in each transmission
- [PStatPort](PStatPort.md) — communication port used for streaming
- [PStatInterval](PStatInterval.md) — interval between transmissions
