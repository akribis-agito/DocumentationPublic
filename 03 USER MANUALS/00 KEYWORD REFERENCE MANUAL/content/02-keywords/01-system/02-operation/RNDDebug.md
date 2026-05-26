---
keyword: RNDDebug
summary: Partially-implemented diagnostic function reserved for Agito R&D.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 1022
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 30
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# RNDDebug

Partially-implemented diagnostic function reserved for Agito R&D.

## Overview

`RNDDebug` is a diagnostic function reserved for Agito internal research and debugging. It is marked **partially implemented** in the firmware: its behaviour depends on the firmware build and its exact semantics may change between versions. It is not intended for use in production applications.

## See also

- [DebugData](../01-status/DebugData.md) — development/test scratch array
