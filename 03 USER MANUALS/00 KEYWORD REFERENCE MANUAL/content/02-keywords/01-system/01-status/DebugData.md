---
keyword: DebugData
summary: Array reserved for Agito feature development and testing.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 224
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 200
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
# DebugData

Array reserved for Agito feature development and testing.

## Overview

`DebugData` is a 200-element scratch array reserved for Agito feature development and testing. Its contents and meaning are not fixed and may change between firmware builds, so it should not be used in production integrations.

## See also

- [RNDDebug](../02-operation/RNDDebug.md) — related development/debug command
