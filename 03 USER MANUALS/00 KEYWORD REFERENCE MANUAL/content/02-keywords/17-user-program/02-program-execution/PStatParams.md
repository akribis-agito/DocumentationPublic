---
keyword: PStatParams
summary: Lists the parameters included in each periodic statistics transmission.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 483
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatParams

Lists the parameters included in each periodic statistics transmission.

## Overview

`PStatParams` is an array parameter that specifies which controller parameters are included in each periodic statistics transmission. Each element identifies one parameter to sample and send at the interval set by [PStatInterval](PStatInterval.md), over the port chosen by [PStatPort](PStatPort.md), whenever streaming is enabled by [PStatOn](PStatOn.md). It is a non-axis parameter and is saved to flash.

## Examples

```text
APStatParams[1]=<CAN code of parameter to stream>    ; first streamed parameter
```

## See also

- [PStatOn](PStatOn.md) — enable/disable periodic statistics streaming
- [PStatPort](PStatPort.md) — communication port used for streaming
- [PStatInterval](PStatInterval.md) — interval between transmissions
