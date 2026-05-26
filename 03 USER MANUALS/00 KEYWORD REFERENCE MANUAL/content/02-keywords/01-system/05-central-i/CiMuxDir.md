---
keyword: CiMuxDir
summary: Sets the direction of the Central-i multiplexer (which port the shared bus routes to).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 551
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
  - 0
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CiMuxDir

Sets the direction of the Central-i multiplexer (which port the shared bus routes to).

## Overview

`CiMuxDir` is a non-axis parameter that controls the direction of the Central-i multiplexer — that is, which physical port the shared Central-i bus is currently routed to. Together with [CiMuxSel](CiMuxSel.md) it lets one controller share its Central-i interface across multiple ports. It is saved to flash.

## Examples

```text
CiMuxDir=1          ; route the shared Central-i bus to the configured port
```

## See also

- [CiMuxSel](CiMuxSel.md) — per-axis multiplexer port selection
- [CIConnect](CIConnect.md) — initiate the link
