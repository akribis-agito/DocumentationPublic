---
summary: Intended to zero the axis position error; availability and behaviour unconfirmed.
keyword: ZeroPosErr
availability:
  standalone: []
  central-i:
  - v5
can_code: 669
attributes:
  access: ro
  scope: axis
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
# ZeroPosErr

Intended to zero the axis position error; availability and behaviour are unconfirmed.

## Overview

`ZeroPosErr` is an axis-related parameter intended to zero the axis position error. It is distinct from [SetPosition](SetPosition.md), which redefines the coordinate value rather than clearing the accumulated error.

> **Documentation pending:** `ZeroPosErr` was not found in the firmware parameter table during review. Confirm its availability and intended behaviour (zeroing the position error versus `SetPosition`) before use.

## See also

- [SetPosition](SetPosition.md) — redefine the axis position to a given value
