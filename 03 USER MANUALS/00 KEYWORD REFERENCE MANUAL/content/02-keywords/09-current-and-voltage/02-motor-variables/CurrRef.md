---
keyword: CurrRef
summary: Read-only final motor current command after all loops, compensation and injection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 26
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrRef

Read-only final motor current command after all loops, compensation and injection.

## Overview

`CurrRef` is the current reference fed into the current control loop. It is the final motor current command after summing all control efforts (feedback loops and feedforward), plus any current-related compensation and injection that apply. It differs from [CurrRefCtrl](CurrRefCtrl.md), which is the loop-side reference taken *before* the decoupling matrix, current injection and current-related compensation.

See [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md) for where `CurrRef` sits in the signal path.

## Examples

```text
ACurrRef            ; read the final current command (mA)
```

## See also

- [CurrRefCtrl](CurrRefCtrl.md) — loop-side current reference before decoupling/compensation
- [CurrRefOffset](../03-current-compensation/CurrRefOffset.md) — offset added on top of the motor current reference
- [IaRef](IaRef.md), [IbRef](IbRef.md) — per-phase references derived from the current command
