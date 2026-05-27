---
summary: Electrical angle at which commutation switches from Hall-based to encoder-based feedback during startup.
keyword: HallsAngleSw
availability:
  standalone: []
  central-i:
  - v5
can_code: 679
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsAngleSw

Electrical angle at which commutation switches from Hall-based to encoder-based feedback during startup.

## Overview

`HallsAngleSw` sets the electrical angle at which commutation switches from Hall-sensor-based to encoder-based feedback during startup. Below this angle threshold the controller uses the Hall sensors ([HallsValue](HallsValue.md), [HallsAngle](HallsAngle.md)) for commutation; above it, it transitions to encoder-based commutation. It is described as an axis-related parameter.

> **Documentation pending:** `HallsAngleSw` was not found in the AG300_CTL01Params.c firmware parameter table. Its availability and parameter attributes (including frontmatter) are unverified and must be confirmed before use.

## See also

- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [HallsValue](HallsValue.md) — current raw Hall sensor state
- [HallOnlyFilt](HallOnlyFilt.md) — filter for the Hall-based commutation angle
