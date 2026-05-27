---
keyword: PStatInterval
summary: Time between successive parameter-statistics transmissions, in milliseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 482
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
  - 2
  - 10000
  default: 1000
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatInterval

Time between successive parameter-statistics transmissions, in milliseconds.

## Overview

`PStatInterval` sets the time interval, in milliseconds, between successive parameter-statistics transmissions while streaming is enabled by [PStatOn](PStatOn.md). The valid range is `2`–`10000` ms (default `1000`). It governs how often the parameters listed in [PStatParams](PStatParams.md) are sampled and sent over the port chosen by [PStatPort](PStatPort.md). It is a non-axis parameter and is saved to flash.

## Examples

```text
PStatInterval=500   ; transmit parameter statistics every 500 ms
```

## See also

- [PStatOn](PStatOn.md) — enable/disable periodic statistics streaming
- [PStatPort](PStatPort.md) — communication port used for streaming
- [PStatParams](PStatParams.md) — parameters included in each transmission
