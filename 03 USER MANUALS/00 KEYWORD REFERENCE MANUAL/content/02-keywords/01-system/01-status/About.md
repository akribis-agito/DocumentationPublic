---
keyword: About
summary: Internal command (Agito PCSuite) that returns all controller parameters.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 223
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
# About

Internal command (Agito PCSuite) that returns all controller parameters.

## Overview

`About` is a read-only command that returns the full set of parameters held in the controller. It is intended for **Agito PCSuite internal use only** and is not part of the normal user command set; to inspect an individual parameter's metadata from host software, use [ParamAbout](ParamAbout.md) instead.

## See also

- [ParamAbout](ParamAbout.md) — metadata for a single parameter
- [FWInfo](FWInfo.md) — firmware version and build information
- [Identity](Identity.md) — controller identification and features
