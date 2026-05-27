---
keyword: RNDDebug
summary: Partially-implemented diagnostic function reserved for Agito R&D.
availability:
  standalone:
  - v4
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

## How it works

In a released firmware image `RNDDebug` is effectively a placeholder: it carries out no externally visible action and simply returns the standard acknowledgement. The accompanying value (within its declared range) selects an internal diagnostic action only in development builds — in production firmware the value has no documented effect. Any behaviour beyond a normal acknowledgement should be treated as build-specific and unsupported.

Because its meaning is reserved and may differ between builds, do not rely on `RNDDebug` in application code. Use the dedicated status and diagnostic keywords instead.

## See also

- [DebugData](../01-status/DebugData.md) — development/test scratch array
- [DoNothing](DoNothing.md) — supported no-op for communication checks
