---
keyword: CiMuxSel
summary: Per-axis array selecting which physical port is routed through the Central-i multiplexer.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 552
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CiMuxSel

Per-axis array selecting which physical port is routed through the Central-i multiplexer.

## Overview

`CiMuxSel` is an axis-related array that selects which physical port is routed through the Central-i multiplexer for each axis. Together with [CiMuxDir](CiMuxDir.md) it determines the complete multiplexer configuration, allowing one controller's Central-i interface to be shared across ports. It is saved to flash.

## Examples

```text
CiMuxSel[1]?        ; read the first multiplexer selection element for this axis
```

## See also

- [CiMuxDir](CiMuxDir.md) — multiplexer direction
- [CIConnect](CIConnect.md) — initiate the link
