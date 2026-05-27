---
summary: Read-only loop-side current reference, taken before the decoupling matrix, injection and compensation.
keyword: CurrRefCtrl
availability:
  standalone: []
  central-i:
  - v5
can_code: 717
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrRefCtrl

Read-only loop-side current reference, taken before the decoupling matrix, injection and compensation.

## Overview

`CurrRefCtrl` is the loop's current reference (as distinct from the motor's current reference [CurrRef](CurrRef.md)). It is the value just before the decoupling matrix, current injection and current-related compensation. Its meaning depends on the operation mode:

- **Position, velocity and force operation mode:** `CurrRefCtrl` is the sum of the current reference from the feedback loop, the feedforwards and the loop compensation.
- **Current operation mode:** `CurrRefCtrl` is the current reference from the source defined by [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) (analog input, [CurrCmdVal](../../08-axis-operation/03-current-operation-mode/CurrCmdVal.md) array, etc.).

See [Control tuning – Velocity control](../../11-control-tuning/04-velocity-control/00-overview.md), [Control tuning – Feedforwards](../../11-control-tuning/05-feedforwards/00-overview.md) and [Control tuning – Force control](../../11-control-tuning/07-force-control/00-overview.md) for where `CurrRefCtrl` sits in the signal path.

## Examples

```text
ACurrRefCtrl        ; read the loop-side current reference
```

## See also

- [CurrRef](CurrRef.md) — final motor current command after decoupling/compensation
- [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) — current-command source in current operation mode
- [IqRef](IqRef.md), [IaRef](IaRef.md) — references derived from CurrRefCtrl after direction correction
