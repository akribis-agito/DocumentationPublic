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

`CurrRefOffset` is the current reference offset, in milliamperes, applied on top of the motor's current reference. Because it is added in the current loop (not in the position/velocity loop), it is the current-loop counterpart of the loop-side torque compensation [TorqCompMode](TorqCompMode.md)/[TorqCompFix](TorqCompFix.md). See [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md) for its application point.

## How it works

In the current control loop, while the motor is enabled and commutation (auto-phasing) is complete, the firmware **adds** `CurrRefOffset` directly to the current reference each control cycle:

$$
CurrRef \mathrel{+}= CurrRefOffset
$$

The offset is applied after the brushless anti-cogging term ([UPMVelTable](UPMVelTable.md)) and before the current limitations and saturation handling, so it is a constant bias on the current reference that is still subject to the current limits downstream. The firmware deliberately applies it only after commutation is complete: any current injection that introduces a DC offset must wait for phasing, otherwise an enabled-but-unphased motor could run away.

This keyword exists only on central-i v5, where the current reference is floating-point. Its range is bounded by the current-command range (its limits are derived from the drive's maximum current command).

## Examples

```text
ACurrRefOffset=500   ; add a 500 mA offset to the motor current reference
ACurrRefOffset      ; read the present offset
```

## See also

- [CurrRef](../02-motor-variables/CurrRef.md) — final motor current command the offset is applied to
- [TorqCompMode](TorqCompMode.md), [TorqCompFix](TorqCompFix.md) — loop-side current compensation
