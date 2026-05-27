---
keyword: FWInfo
summary: Read-only command returning firmware version and build information.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 312
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FWInfo

Read-only command returning firmware version and build information.

## Overview

`FWInfo` is a read-only command that returns a block of firmware version and build information for the controller. Host software uses it to identify the firmware revision currently running on the device — for example to confirm a unit is on the expected release before commissioning, or to capture the build for a support report.

## Examples

```text
AFWInfo             ; return the firmware version/build block
```

## See also

- [Identity](Identity.md) — controller identification and implemented features
- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [UnitStat](UnitStat.md) — flags a firmware/FPGA image mismatch
