---
summary: Current reference offset (mA) applied on top of the motor's current reference.
keyword: CurrRefOffset
availability:
  standalone: []
  central-i:
  - v5
can_code: 599
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -6400
  - 6400
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrRefOffset

Current reference offset (mA) applied on top of the motor's current reference.

## Overview

`CurrRefOffset` is the current reference offset, in milliamperes, applied on top of the motor's current reference. Because it is added on the motor side (after the decoupling matrix), it is the motor-side counterpart of the loop-side torque compensation [TorqCompMode](TorqCompMode.md)/[TorqCompFix](TorqCompFix.md). See [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md) for its application point.

## Examples

```text
ACurrRefOffset=500   ; add a 500 mA offset to the motor current reference
ACurrRefOffset      ; read the present offset
```

## See also

- [CurrRef](../02-motor-variables/CurrRef.md) — final motor current command the offset is applied to
- [TorqCompMode](TorqCompMode.md), [TorqCompFix](TorqCompFix.md) — loop-side current compensation
