---
keyword: About
summary: Internal command (Agito PCSuite) that returns all controller parameters.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`About` is a read-only function that dumps the full set of parameters held in the controller in one operation. It is intended for **Agito PCSuite internal use only** and is not part of the normal user command set: PCSuite calls it to populate its parameter and data-view panels. To inspect an individual parameter's range and default from host software, use [ParamAbout](ParamAbout.md) instead; to read the firmware build information use [FWInfo](FWInfo.md).

## How it works

`About` is implemented as a non-axis function (it has no stored value of its own). When called, the firmware iterates the controller's keyword table and streams back the current value of every parameter to the requesting communication channel, using the bulk reply path. Because it is meant to be issued and parsed by PCSuite, the response layout is tied to the PCSuite/firmware contract rather than documented for general scripting; user integrations should read individual keywords (or use [ParamAbout](ParamAbout.md) for limits) instead.

## See also

- [ParamAbout](ParamAbout.md) — range and default of a single parameter
- [FWInfo](FWInfo.md) — firmware build-info strings
- [Identity](Identity.md) — controller identification and features
