---
keyword: GantryOffset
summary: Read-only initial A/B position offset captured when gantry mode is switched on.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 653
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryOffset

Read-only initial A/B position offset captured when gantry mode is switched on.

## Overview

`GantryOffset` is a read-only parameter. `AGantryOffset` is calculated once when `AGantryOn` is switched by the user from `0` to `1`. It captures the initial offset between the two encoder readings so that this offset is ignored in the [GantryFdbk](GantryFdbk.md) calculation, letting the gantry feedbacks start from a clean reference (see [GantryOn](../01-general-variables/GantryOn.md)).

## How it works

The offset is captured as:

```text
AGantryOffset = APosRef - BPosRef
```

It is then folded into the gantry feedbacks:

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2
BGantryFdbk = (APos - BPos - AGantryOffset)
```

`?GantryOffset` with `?` not equal to `A` has no use and always returns `0`.

## Examples

```text
AGantryOffset      ; read the captured A/B offset
```

## See also

- [GantryFdbk](GantryFdbk.md) — gantry feedbacks that apply this offset
- [GantryOn](../01-general-variables/GantryOn.md) — captures the offset on the 0→1 transition
