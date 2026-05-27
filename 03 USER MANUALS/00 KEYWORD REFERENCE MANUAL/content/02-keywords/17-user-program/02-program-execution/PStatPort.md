---
keyword: PStatPort
summary: Selects the communication port used for parameter-statistics streaming.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 481
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatPort

Selects the communication port used for parameter-statistics streaming.

## Overview

`PStatPort` selects the communication port over which parameter-statistics data is transmitted while streaming is enabled by [PStatOn](PStatOn.md). The valid range is `1`–`3`. It works with [PStatParams](PStatParams.md) (what is sent) and [PStatInterval](PStatInterval.md) (how often). It is a non-axis parameter and is saved to flash.

## Examples

```text
APStatPort=1         ; stream statistics over port 1 (range 1-3)
```

## See also

- [PStatOn](PStatOn.md) — enable/disable periodic statistics streaming
- [PStatParams](PStatParams.md) — parameters included in each transmission
- [PStatInterval](PStatInterval.md) — interval between transmissions
